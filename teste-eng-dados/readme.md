# Cognitiv0AI

Este projeto é parte do processo para uma vaga de consultor na empresa CognitivoAI

O objetivo do projeto é realizar um processamento de dados no software Apache Spark baseado em alguns requisitos:

- Conversão do arquivo CSV para um formato colunar
- Deduplicação de dados
- Conversão do tipo de dados do schema

### Pré-requisitos

Processo de ETL:
- Python 3.5+ : json, jupyter
- Apache Spark 2.2+
- cluster Cloud Dataproc no GCP
- Uma conta ativa na GCP com um usuário administrador (utilização da KEY e da SECRET para automatização do processo de criação do cluster)

Todos os arquivos foram do github foram colocados em um Bucket no Google Storage criado com nome de `gs://cognitivo-ai-db/teste-eng-dados` com processo de ETL, é possível extrair os dados diretamente do Bucket e realizar a ingestão desses dados no Cluster que será criado.

Para executar o processo de ETL. Utilize o seguinte comando no terminal:
```
bash_automated_etl.sh
```

Esse comando irá executar os arquivos na seguinte ordem:
- Criar um cluster Google Dataproc (spark)
- enviar o job dataproc.py, que é o mesmo do exploracao.ipynb (notebook)
- criar um dataset no BigQuery
- criar uma tabela no BigQuery
- fazer o carregamento do arquivo load.parquet na pasta output para a tabela no Bigquery terminando o processo ETL e disponibilizando para uso da equipe.
- deletar o cluster criado para não incorrer em custos extras.

O processo ETL resultou no caminho BUCKET => SPARK => BQ.

o arquivo .sh também poderá ser feito na maquina local baixando o google cloud SDK, ou usando o próprio terminal dentro do console GCP.
Ou no próprio windows da máquina local.
https://cloud.google.com/storage/docs/gsutil_install?hl=pt-br#windows

```
bash_automated_etl.bat
```

Com o intuito de limitar um pouco os gastos, optei pela configuração de um cluster com apenas um Node, no entanto, isso pode ser alterado no script do google cloud

O processo de criação do cluster e realização do ETL dura em torno de 90 segundos, variando conforme a capacidade de processamento do clusters.