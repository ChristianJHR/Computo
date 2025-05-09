from elasticsearch import Elasticsearch
import pandas as pd
import matplotlib.pyplot as plt

# Conectar a Elasticsearch
es = Elasticsearch("http://localhost:9200")

# Obtener datos del índice "digimon"
results = es.search(index="digimon", size=1000, query={"match_all": {}})
data = [hit["_source"] for hit in results["hits"]["hits"]]

# Crear DataFrame
df = pd.DataFrame(data)

# Asegurar que las columnas necesarias existan
if "Lv50_HP" in df.columns and "Digimon" in df.columns:
    # Convertir a numérico por si hay errores o valores vacíos
    df["Lv50_HP"] = pd.to_numeric(df["Lv50_HP"], errors="coerce")

    # Eliminar filas sin datos válidos
    df = df.dropna(subset=["Lv50_HP", "Digimon"])

    # Ordenar por HP para mejor visualización
    df = df.sort_values("Lv50_HP", ascending=False).head(20)

    # Gráfica de barras
    plt.figure(figsize=(12, 8))
    plt.bar(df["Digimon"], df["Lv50_HP"], color='royalblue')
    plt.xticks(rotation=75, ha='right')
    plt.title("Top 20 Digimon por HP al Nivel 50")
    plt.xlabel("Digimon")
    plt.ylabel("Lv50_HP")
    plt.tight_layout()

    # Guardar imagen
    plt.savefig("docs/digimon_plot.png")
    plt.close()
    print("Gráfica guardada como docs/digimon_plot.png")
else:
    print("Las columnas necesarias no se encontraron en los datos.")
