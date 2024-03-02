import sys
import numpy as np
import pandas as pd
import openpyxl
import os
import re

# <item_file.txt>
item_file = open("items.txt", "r", encoding='utf-8')
items = []
while True:
    content = item_file.readline().strip()
    if not content:
        break
    items.append(content)
# print(items)
items_regex = "|".join(items)

# <input folder>
input_files = os.listdir('input')
print(input_files)
for input_file in input_files:
    df = pd.read_excel(f'input/{input_file}')
    df = df.assign(상품명=df['내용'].str.findall(items_regex))
    df = df.assign(금액=df['내용'].str.findall('\d{1,3}(?:,\d{3})*\s*만원|\d{1,3}(?:,\d{3})*\s*원'))
    export_df = df.drop(columns=["내용"])
    input_file = input_file.rstrip('.xlsx') # rename
    export_df.to_excel(f'output/{input_file}_output.xlsx')
    