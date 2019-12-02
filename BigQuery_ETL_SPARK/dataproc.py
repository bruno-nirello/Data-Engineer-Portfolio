import pyspark
from pyspark.sql import SparkSession
sc = pyspark.SparkContext.getOrCreate()
spark = SparkSession.builder.getOrCreate()
df2 = spark.read.csv("gs://cognitivo-ai-db/teste-eng-dados/data/input/users/load.csv", header=True)
from pyspark.sql.types import *
import json
schema_json = df2.schema.json()
schema_json2 = eval(schema_json.replace("true", "True"))
with open('gs://cognitivo-ai-db/teste-eng-dados/config/types_mapping.json') as f:
    data = json.load(f)
data.update(id = 'integer')
for field in schema_json2['fields']:
    if field['name'] in data.keys():
        field['type'] = data[field['name']]
schema_json2 = json.dumps(schema_json2)
new_schema = StructType.fromJson(json.loads(schema_json2))
df2 = spark.read.csv("gs://cognitivo-ai-db/teste-eng-dados/data/input/users/load.csv", header=True, schema=new_schema)
df_drop = df2.orderBy(df2.update_date.desc()).dropDuplicates(['id'])
df_renamed = df_drop.withColumnRenamed("name", "e_mail").withColumnRenamed("email", "name").withColumnRenamed("e_mail", "email")
df_renamed.write.parquet("gs://cognitivo-ai-db/teste-eng-dados/data/output/load.parquet", mode="overwrite")