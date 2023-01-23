import pandas as pd
import numpy as np
from google.colab import drive
import re
drive.mount('/content/drive')


petrol_df = pd.read_excel('/content/drive/My Drive/petrol_prices/preciosEESS_es.xls')


service_type = []

for i in petrol_df['Tipo servicio']:
  st = i[i.find("(")+1:i.find(")")]
  service_type.append(st)
petrol_df['Service Type'] = service_type

petrol_df.to_excel('/content/drive/My Drive/petrol_prices/petrol_prices_wc.xls')

petrol_df['count'] = 1
filt_df = petrol_df[['Service Type','count', 'Precio gasolina 95 E5', 'Precio gasolina 98 E5', 'Precio gasóleo A', 'Precio biodiésel']]
filt_dfx = filt_df[filt_df['Service Type'] != 'Sin dato']
filt_dfx['Service Type'] = filt_dfx['Service Type'].map({"P":"Servei assistit per personal",
                             "D":"Autoservei sense personal auxiliar",
                             "A":"Autoservei amb personal auxiliar"},
                             na_action=None)

price_by_type = filt_dfx.groupby('Service Type').mean()
print(price_by_type)

price_by_type.to_excel('/content/drive/My Drive/petrol_prices/price_by_type.xls')

dnt_by_n = filt_dfx.groupby('Service Type')['count'].sum()
print(dnt_by_n)
dnt_by_n.to_excel('/content/drive/My Drive/petrol_prices/dnt_by_n.xls')


prices_df = petrol_df[['Precio gasolina 95 E5', 'Precio gasolina 95 E10', 
                       'Precio gasolina 98 E5', 'Precio gasolina 98 E10', 
                       'Precio gasóleo A', 'Precio gasóleo Premium', 
                       'Precio bioetanol', 'Precio biodiésel',
                       'Precio gases licuados del petróleo', 'Precio gas natural comprimido','Precio gas natural licuado']]

prices_df_mean = prices_df.mean()    
print(prices_df_mean) 
prices_df_mean.to_excel('/content/drive/My Drive/petrol_prices/prices_df_mean.xls')
             
             
petrol_map = petrol_df[['Provincia', 'Precio gasolina 95 E5']]
petrol_df_nn = petrol_map.dropna()

petrol_df_grp = petrol_df_nn.groupby('Provincia')["Precio gasolina 95 E5"].mean()
petrol_df_grp
petrol_df_grp.to_excel('/content/drive/My Drive/petrol_prices/petrol_df_grp.xls')
