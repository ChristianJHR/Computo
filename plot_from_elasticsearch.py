from elasticsearch import Elasticsearch
import pandas as pd
import matplotlib.pyplot as plt

es = Elasticsearch("http://localhost:9200")
query = {"query": {"match_all": {}}}
results = es.search(index="digimon", size=150, body=query)

data = [doc["_source"] for doc in results["hits"]["hits"]]
df = pd.DataFrame(data)
print(df.columns)
df["Lv50_HP"] = pd.to_numeric(df["Lv50_HP"], errors="coerce")
df["Lv50_Atk"] = pd.to_numeric(df["Lv50_Atk"], errors="coerce")

plt.figure(figsize=(8,6))
plt.scatter(df["Lv50_HP"], df["Lv50_Atk"], alpha=0.7)
plt.xlabel("HP at Level 50")
plt.ylabel("Attack at Level 50")
plt.title("Digimon: HP vs Attack at Level 50")
plt.grid(True)
plt.savefig("docs/digimon_plot.png")
