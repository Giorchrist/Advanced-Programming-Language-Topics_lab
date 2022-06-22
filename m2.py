#pip install pandas
#pip install bs4

import requests
import matplotlib.pyplot as plt



import pandas as pd
fromfile = pd.read_excel('sneakers.xlsx')
 
print(fromfile)

# μέτρηση null τιμών
fromfile.isna().sum()

# υπολογισμός μέσης τιμής και μέσου αριθμού reviews
meanprice = fromfile['Prices'].mean()
print('meanprice:'+str(meanprice))
meanreviews = fromfile['Reviews'].mean()
print('meanreviews:'+str(meanreviews))
# αντικατάσταση null τιμών
fromfile['Prices'].fillna(meanprice)
fromfile['Reviews'].fillna(meanreviews)
print(fromfile)
npprices = fromfile['Prices'].to_numpy()
npreviews = fromfile['Reviews'].to_numpy()
plt.scatter(npprices, npreviews)
plt.show()