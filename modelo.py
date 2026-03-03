import pandas as pd # type: ignore
import sqlite3

df = pd.read_csv("datosvalidados.csv")

conn = sqlite3.connect("analitica.db")
df.to_sql("ventas", conn, if_exists="replace", index=False)

query = """
SELECT region, SUM(ventas) as total_ventas
FROM ventas
GROUP BY region
"""

result = pd.read_sql(query, conn)
print(result)