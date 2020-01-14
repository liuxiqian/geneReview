# %%
import os
import requests
import xlrd
import xlwt
from bs4 import BeautifulSoup
import time


GHR_BASE_URL = 'https://ghr.nlm.nih.gov'
GHR_GENE_BASE_URL = 'https://www.ncbi.nlm.nih.gov/books/'

# %% page test
# NBK_id = 'NBK1363'
# test_url = 'https://www.ncbi.nlm.nih.gov/books/' + NBK_id
# headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'}
# url = Request(test_url, headers=headers)
data = []
path = '/home/liuxi/Desktop/text.txt'
convert_path = '/home/liuxi/Desktop/convert_text.txt'
test_path = '/home/liuxi/Desktop/test.txt'
test_convert_path = '/home/liuxi/Desktop/test_convert_text.txt'

def change_to_lower():
    with open(path) as txtfile:
        line = txtfile.readlines()
        for i, rows in enumerate(line):
            if i in range(2, len(line)):  # 指定数据哪几行
                print(rows)
                data.append(rows)
        print("length", len(data))
    with open(convert_path, "w") as f:
        for i in range(len(data)):
            data[i] = data[i].replace(':', '')
            data[i] = data[i].replace('-', '_')
            data[i] = data[i].replace('/', '_')
            data[i] = data[i].replace('textfield', 'TextField')
            print(data[i])
            f.writelines(data[i])
    f.close()


# change_to_lower()

def duplicate_removal():
    with open(test_path) as txtfile:
        line = txtfile.readlines()
        for i, rows in enumerate(line):
            if i in range(len(line)):  # 指定数据哪几行
                print(rows)
                data.append(rows)
        print("length", len(data))
    new_data = list(set(data))
    with open(test_convert_path, "w") as f:
        for i in range(len(new_data)):
            print(new_data[i])
            f.writelines(new_data[i])
    f.close()


duplicate_removal()