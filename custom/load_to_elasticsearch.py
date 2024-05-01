from elasticsearch import Elasticsearch
from biostudies.utils.load_step.db import *
from pymongo import MongoClient

if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom

@custom
def transform_custom(*args, **kwargs):
    ELASTICSEARCH_URI = kwargs["ELASTICSEARCH_URI"]
    MONGO_URI = kwargs["MONGO_URI"]

    es = Elasticsearch(hosts=ELASTICSEARCH_URI)
    mongoClient = MongoClient(MONGO_URI)

    try:
        es.delete_by_query(index="biostudies_column_name", body={"query": {"match_all": {}}})
    except:
        pass

    timestamp = read_fetching_date(mongoClient)

    column_count, mapping_schema = read_count_header_file("/home/src/data/count_header.txt")

    load_elasticsearch_index(es, "biostudies", mapping_schema)
    load_column_name(es, column_count)
    
    file_list = os.listdir("/home/src/data/sdrf_cleaned_depth")

    for file in file_list:
        load_csv_to_elasticsearch(es, f'/home/src/data/sdrf_cleaned_depth/{file}', column_count, timestamp)
        print(f"File {file} has been loaded to Elasticsearch")
    