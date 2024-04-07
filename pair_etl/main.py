#%%
import soporte_etl1 as sop1
import pandas as pd

#%%
with open("../files/ETL/in/productos.csv", 'r') as file:

    lines = file.readlines()
# %%
sop1.unificar(lines)

#%%
sales = pd.read_csv("../files/ETL/in/ventas.csv")
customers = pd.read_csv("../files/ETL/in/clientes.csv")
items = pd.read_csv("../files/ETL/out/productos1.csv")
# %%

sop1.exploracion_datos(sales)
sop1.exploracion_datos(customers)
sop1.exploracion_datos(items)
# %%
items.rename(columns = {"ID" : "ID_Producto"}, inplace = True)

# %%
customers.rename(columns = {
        'id': 'ID_Cliente',
        'first_name': 'nombre',
        'last_name': 'apellido',
        'email': 'correo',
        'gender': 'género',
        'City': 'Ciudad',
        'Country': 'País',
        'Address': 'Dirección'
    }, inplace = True)
# %%
first_uni= sales.merge(items, on="ID_Producto", how="left")
#%%
data_final = first_uni.merge(customers, on="ID_Cliente")
# %%
sop1.exploracion_datos(data_final)
# %%
sop1.unificacion_columnas(data_final)
# %%
data_final.to_csv("../files/ETL/out/data_final.csv")
# %%
