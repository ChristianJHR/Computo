from elasticsearch import Elasticsearch
import csv

es = Elasticsearch("http://localhost:9200")

with open("DigiDB_digimonlist.csv", newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for i, row in enumerate(reader):
        es.index(index="digimon", id=i, document=row)
