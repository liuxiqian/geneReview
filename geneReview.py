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


def read_excel():
    workbook = xlrd.open_workbook('/home/liuxi/Desktop/NBKid_shortname_genesymbol_UniProt.xlsx')
    sheet_names = workbook.sheet_names()
    # print(sheet_names)
    for sheet_name in sheet_names:
        # print(sheet_name)
        if sheet_name == 'NBKid_shortname_genesymbol_UniP':
            sheet_xls = workbook.sheet_by_name(sheet_name)
            col = sheet_xls.col_values(0)  # 获取第一列内容
            col.pop(0)
            gene_review_page_parse(col)


def gene_review_page_parse(col):
    row_count = 1
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet("Sheet Name1")
    sheet.write(0, 0, '#NBK_id')
    for columns in col:
        sheet.write(row_count, 0, columns)
        # URL地址
        test_url = 'https://www.ncbi.nlm.nih.gov/books/' + columns
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
        req = requests.get(test_url, headers=headers)
        # 抓取页面数据
        html_data = req.text
        soup = BeautifulSoup(html_data, 'html.parser')
        key_word_array = soup.find_all(text=(u"In this GeneReview"))
        # 搜索关键字是否存在
        if key_word_array:
            key_word = key_word_array[0]
            # print(key_word)
            table = key_word.find_next('ul')
            # print(table)
            column_count = 1
            for child in table.childGenerator():
                delimiter = '!@#$%'
                name = child.getText(delimiter).split(delimiter)[0]
                print(name)
                sheet.write(row_count, column_count, name)  # row, column, value
                column_count = column_count+1
        else:
            sheet.write(row_count, 1, '')
        row_count = row_count+1
        time.sleep(3)
    workbook.save('test_gene_review_page.xls')
    print(os.getcwd())


read_excel()
# gene_review_page_parse(cols)
