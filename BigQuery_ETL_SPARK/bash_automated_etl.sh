#!/bin/bash

gcloud init

gcloud dataproc clusters create my-cluster --single-node --bucket=cognitivo-ai-db --master-machine-type=n1-standard-2

gcloud dataproc jobs submit pyspark --cluster my-cluster2 gs://cognitivo-ai-db/teste-eng-dados/dataproc.py

bq --location=US mk -d --default_table_expiration 360000 --description "Este é o cognitivo-ai dataset." cognitivoai

bq mk -t --expiration 360000 --description "This is my table" --label organization:development cognitivoai.lista-cliente 

bq load --project_id=feisty-access-259014 --autodetect --source_format=PARQUET cognitivoai.lista_cliente "gs://cognitivo-ai-db/teste-eng-dados/data/output/*.parquet"

gcloud dataproc clusters delete my-cluster