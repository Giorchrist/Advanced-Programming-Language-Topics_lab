#pip install pandas
#pip install bs4

import requests
import matplotlib.pyplot as plt



import pandas as pd
fromfile = pd.read_excel('sneakers.xlsx')
 
print(fromfile)

# ������� null �����
fromfile.isna().sum()

# ����������� ����� ����� ��� ����� ������� reviews
meanprice = fromfile['Prices'].mean()
print('meanprice:'+str(meanprice))
meanreviews = fromfile['Reviews'].mean()
print('meanreviews:'+str(meanreviews))
# ������������� null �����
fromfile['Prices'].fillna(meanprice)
fromfile['Reviews'].fillna(meanreviews)
print(fromfile)
npprices = fromfile['Prices'].to_numpy()
npreviews = fromfile['Reviews'].to_numpy()
plt.scatter(npprices, npreviews)
plt.show()