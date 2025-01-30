from elasticsearch import Elasticsearch
import os 

ELASTICSEARCH_HOST = os.getenv("ELASTICSEARCH_HOST", "http://localhost:9200")

es = Elasticsearch(ELASTICSEARCH_HOST)


def create_indice():
    if not es.indices.exists(index="products"):
        es.indices.create(index="products", body={
            "settings": {"number_of_shards": 1},
            "mappings": {
                "properties": {
                    "name": {"type": "text"},
                    "description": {"type": "text"},
                    "price": {"type": "float"}
                }
            }
        })

create_indice()
