import requests
import html
import re
import xlsxwriter

from xml.etree import ElementTree as ET
from bs4 import BeautifulSoup

import suricate_url

class Table:
    def __init__(self, urls):
        self.row = self.Row()
        self.col = self.Col()

        self.date = None
        self.raw = None
        self.data = {}
        self.names = []
        self.locations = {}

        self.workbook = xlsxwriter.Workbook('suricate_output.xlsx')
        self.worksheet = self.workbook.add_worksheet("tbl")

        self.get_names()
        self.write_names()

        for url in urls:
            self.get_date(url)
            self.get_html(url)
            self.get_data()
            #print(self.data)
            self.set_date()
            self.write_open_interest()
            self.write_commercial_long()
            self.write_commercial_short()
            self.row.add_1()

        self.workbook.close()


    def get_html(self, url):
        self.raw = str(BeautifulSoup(html.unescape(requests.get(url, verify=False).text), features='html.parser').find('table', id="exceltable"))

    def get_date(self, url):
        date = re.findall('[0-9]{4}-[0-9]{2}-[0-9]{2}', string=str(url))[0]
        print(date)
        self.date = int(date.replace('-', '')) - 20000000

    def get_data(self):
        a = []
        table = ET.XML(self.raw)
        rows = iter(table)
        headers = [col.text for col in next(rows)]

        for row in rows:
            values = [col.text for col in row]
            print(headers, values)
            a.append(dict(zip(headers, values)))

        for i in a:
            print(i)
            self.data[i['Name']] = {'OpenInterest': i['OpenInterest'], 'CommLong':i['CommLong'], 'CommShort':i['CommShort']}


    def get_names(self):
        with open('names_table.txt') as names_table:
            for i in names_table.readlines():
                if 'Ã¤' in i: i = i.replace('Ã¤', 'ä')
                if 'Ã–' in i: i = i.replace('Ã–', 'Ö')
                if 'Ã¶' in i: i = i.replace('Ã¶', 'ö')
                self.names.append(i.strip())

    def set_date(self):
        self.col.set_col(0)
        self.worksheet.write(self.row.row, self.col.col, self.date)
        self.col.add_1()

    def write_names(self):
        self.col.add_1()

        for name in self.names:
            self.locations[name] = {'open_interest': '', 'commercial_long':'', 'commercial_short':''}
            self.worksheet.write(self.row.row, self.col.col, name)
            self.locations[name]['open_interest'] = self.col.col
            self.col.add_1()

        self.worksheet.write(self.row.row, self.col.col, '')
        self.col.add_1()

        for name in self.names:
            self.worksheet.write(self.row.row, self.col.col, name)
            self.locations[name]['commercial_long'] = self.col.col
            self.col.add_1()

        self.worksheet.write(self.row.row, self.col.col, '')
        self.col.add_1()

        for name in self.names:
            self.worksheet.write(self.row.row, self.col.col, name)
            self.locations[name]['commercial_short'] = self.col.col
            self.col.add_1()

        self.col.set_col_0()
        self.row.set_row(1)

    def write_open_interest(self):
        for name in self.data:
            if name in self.locations and self.data[name]['OpenInterest'] != '-':
                needed_col = self.locations[name]['open_interest']
                self.worksheet.write(self.row.row, needed_col, int(self.data[name]['OpenInterest']))

    def write_commercial_long(self):
        for name in self.data:
            if name in self.locations and self.data[name]['OpenInterest'] != '-':
                needed_col = self.locations[name]['commercial_long']
                self.worksheet.write(self.row.row, needed_col, int(self.data[name]['CommLong']))

    def write_commercial_short(self):
        for name in self.data:
            if name in self.locations and self.data[name]['OpenInterest'] != '-':
                needed_col = self.locations[name]['commercial_short']
                self.worksheet.write(self.row.row, needed_col, int(self.data[name]['CommShort'])*-1)


    class Row:
        def __init__(self):
            self.row = 0

        def set_row_0(self):
            self.row = 0

        def add_1(self):
            self.row += 1

        def set_row(self, row):
            self.row = row

        def current_row(self):
            return self.row

    class Col:
        def __init__(self):
            self.col = 0

        def set_col_0(self):
            self.col = 0

        def add_1(self):
            self.col += 1

        def set_col(self, col):
            self.col = col

        def current_col(self):
            return self.col


def main(urls):
    Table(urls)

#TODO sort urls via function
main(suricate_url.url_list)