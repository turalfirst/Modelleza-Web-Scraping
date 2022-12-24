from bs4 import BeautifulSoup
import requests
import lxml
import pandas as pd
import re
import json
import itertools

n = 0
total_pages = 10
listings = []

while n <= total_pages:
    url = f'https://v-tylu.work/uk/?transaction_type=offering-with-online-payment&page={total_pages}'
    response = requests.get(url)
    page = BeautifulSoup(response.content, 'lxml')
    n += 1
    listings.append(re.findall(r"/uk/listings/[0-9]+", str(page)))

merged_listings = list(itertools.chain.from_iterable(listings))

ids = set()

for id_no in merged_listings:
    ids.add(id_no[-7:])

ids = list(ids)

language = "uk"

endpoint = 'https://listing-service.v-tylu.com/work/listings'

objects = {"ids": ids,
           "language": language}

x = requests.post(endpoint, json=objects)

items = x.json()

columns = items[0].keys()
values = []

for item in items:
    values.append(item.values())

df = pd.DataFrame(columns=columns, data=values)

df.to_excel('BeautifulSoupScrapingTask.xlsx', sheet_name='v-tylu.work data')
df.to_csv('BeautifulSoupScrapingTask.csv', sep=',', index=False, encoding='utf8')