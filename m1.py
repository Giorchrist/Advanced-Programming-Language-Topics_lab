#pip install pandas
#pip install bs4

import requests

r = requests.get('https://www.skroutz.gr/c/3363/sneakers.html')

c = r.content
#print(c)


#from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

#from selenium.webdriver.common.keys import Keys

#driver = webdriver.Chrome("C:\Users\VICKY\Downloads\chromedriver_win32")

soup = BeautifulSoup(c)

main_content = soup.find_all('ol', attrs = {'id': "sku-list"})
main_content

internal_content = main_content[0].find_all('li', attrs = {'class': "cf card"})

import re
import matplotlib.pyplot as plt
import numpy as np





titlespattern = '[A-Z][A-Za-z0-9]* '
colourspattern = '(Μαύρα)|(Λευκά)|(Πολύχρωμα)|(Μπεζ)|(Μπλε)|(Μπορντό)|(Ροζ)|(Γκρι)'
fylopattern = '(Unisex)|(Γυναικεία)|(Ανδρικά)'
#oloklpattern = '[A-Z][A-Za-z0-9](\s[A-Z][A-Za-z0-9])*'
pricespattern = '(\d+),(\d+) €+'
urlpattern = 'data-e2e-testid="sku-price-link" href=\"([^"]+)'
reviewpattern = '\"reviewCount\">([0-9]+)'
urls = re.findall(urlpattern,r.text)
Titles = []
Prices = []
Colours = []
Fylo = []
#Olokl = []
Reviews = []
for i,content_ in enumerate(internal_content):
    match = re.search(titlespattern, content_.text)
    if match:
        Titles.append(match.group())
    else:
        Titles.append(None)
    match = re.search(pricespattern, content_.text)
    if match:
        Prices.append(match.group())
    else:
        Prices.append(None)
    match = re.search(colourspattern, content_.text)
    if match:
        Colours.append(match.group())
    else:
        Colours.append(None)
    match = re.search(fylopattern, content_.text)
    if match:
        Fylo.append(match.group())
    else:
        Fylo.append(None)
    #match = re.search(oloklpattern, content_.text)
    #if match:
    #    Olokl.append(match.group())
    #else:
    #    Olokl.append(None)
    # 2ου επιπέδου στην σελίδα του προιόντος
    r = requests.get('https://www.skroutz.gr/'+urls[i])
    #print(r.text)
    review = re.findall(reviewpattern, r.text)
    if match:
        Reviews.append(review[0])
    else:
        Reviews.append(None)
    if (i==2):
        break
# αφαίρεση σήματος ευρώ από τις τιμές. μετατροπή σε float
Prices = [float(p[:-2].replace(',','.')) for p in Prices]
# μετατροπή reviews σε ακέραιο
Reviews = [int(r) for r in Reviews]
#print(len(urls))
#print(urls)
#print(len(Titles))
#print(Titles)
#print("===========================================")
#print(len(Prices))
#print(Prices)
#print("===========================================")
#print(len(Colours))
#print(Colours)
#print("===========================================")
#print(len(Fylo))
#print(Fylo)
#print("===========================================")
#print(len(Reviews))
#print(Reviews)

alldict = {'Titles': Titles, 'Prices': Prices, 'Colours': Colours,'Fylo': Fylo,'Reviews': Reviews}
tofile = pd.DataFrame.from_dict(alldict)
print(tofile)
tofile.to_excel("sneakers.xlsx",
             sheet_name='sneakers') 
#χρωμα, id, κωδ. χωρας, φυλο(unisex), ολοκληρο ονομα
