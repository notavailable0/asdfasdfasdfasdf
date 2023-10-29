import requests
import html
import re
import xlsxwriter

from xml.etree import ElementTree as ET
from bs4 import BeautifulSoup
from datetime import datetime

from used_names_dir import local_used, used_local

class Table:
    def __init__(self, urls):
        self.row = self.Row()
        self.col = self.Col()

        self.date = None
        self.raw = None
        self.data = {}
        self.names = []
        self.locations = {}

        self.workbook = xlsxwriter.Workbook('cftc-from-source.xlsx')
        self.worksheet = self.workbook.add_worksheet("tbl")

        self.get_names()
        self.write_names()

        for url in urls:
            print(url)
            self.get_html(url)
            self.get_date()
            self.get_data()

        self.set_date()
        self.write_open_interest()
        self.write_commercial_long()
        self.write_commercial_short()

        self.workbook.close()


    def get_html(self, url):
        self.raw = html.unescape(requests.get(url).text).replace(',', '')

    def format_letters(self):
        pass

    def get_date(self):
        if self.raw.count('Code') != 0:
            print(self.raw.count('Code'))
            date = re.findall(r'[0-9]+/[0-9]+/[0-9]+', self.raw)[0]
            self.date = datetime.strptime(date, '%m/%d/%y').strftime('%y%m%d')

    def get_data(self):
        if self.raw.count('Code') == '0':
            return

        Commercials_str = self.raw.replace('\n', '').replace('\r', '')

        names = [i.strip() for i in re.findall(r'.+?(?=Code)', self.raw)]
        OpenInterests = [i[0] for i in re.findall(r'  OPEN INTEREST: +([+-]?(?=\.\d|\d)(?:\d+)?(?:\.?\d*))(?:[eE]([+-]?\d+))?', self.raw)]
        CommLong = [re.sub(r'\s+', '|', i[0]).split('|')[4] for i in re.findall(r'COMMITMENTS(\s+([0-9]+\s+)+)', Commercials_str)]
        CommShort = [re.sub(r'\s+', '|', i[0]).split('|')[5] for i in re.findall(r'COMMITMENTS(\s+([0-9]+\s+)+)', Commercials_str)]

        for i in tuple(zip(names, OpenInterests, CommLong, CommShort)):
            self.data[i[0]] = {'OpenInterest': i[1], 'CommLong':i[2], 'CommShort':i[3]}


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
            if name in used_local:
                table_name = used_local[name]
                if table_name in self.locations and self.data[name]['OpenInterest'] != '-':
                    needed_col = self.locations[table_name]['open_interest']
                    self.worksheet.write(self.row.row, needed_col, int(self.data[name]['OpenInterest']))

    def write_commercial_long(self):
        for name in self.data:
            if name in used_local:
                table_name = used_local[name]
                if table_name in self.locations and self.data[name]['OpenInterest'] != '-':
                    needed_col = self.locations[table_name]['commercial_long']
                    self.worksheet.write(self.row.row, needed_col, int(self.data[name]['CommLong']))

    def write_commercial_short(self):
        for name in self.data:
            if name in used_local:
                table_name = used_local[name]
                if table_name in self.locations and self.data[name]['OpenInterest'] != '-':
                    needed_col = self.locations[table_name]['commercial_short']
                    self.worksheet.write(self.row.row, needed_col, int(self.data[name]['CommShort']))


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


def logging_to_bot():
    url = f'https://api.telegram.org/bot5110727680:AAExTv4NWs_JerI7lcYSMYjqcYRC4VfHJKA/sendMessage?chat_id=953941448&text=LAUNCHED IT AND DONE&parse_mode=markdown'
    requests.get(url)

def main(urls):
    Table(urls)
    logging_to_bot()

url_list = ['https://www.cftc.gov/dea/futures/deanybtsf.htm', 'https://www.cftc.gov/dea/futures/deaiceusf.htm', 'https://www.cftc.gov/dea/futures/deaifedsf.htm', 'https://www.cftc.gov/dea/futures/deacbtsf.htm', 'https://www.cftc.gov/dea/futures/deacmesf.htm', 'https://www.cftc.gov/dea/futures/deacboesf.htm', 'https://www.cftc.gov/dea/futures/deaccxsf.htm', 'https://www.cftc.gov/dea/futures/deakcbtsf.htm', 'https://www.cftc.gov/dea/futures/deamgesf.htm', 'https://www.cftc.gov/dea/futures/deacmxsf.htm', 'https://www.cftc.gov/dea/futures/deanymesf.htm', 'https://www.cftc.gov/dea/futures/deanylsf.htm', 'https://www.cftc.gov/dea/futures/deanypcsf.htm', 'https://www.cftc.gov/dea/futures/deanodxsf.htm', 'https://www.cftc.gov/dea/futures/deadumxsf.htm', 'https://www.cftc.gov/dea/futures/deapbotsf.htm', 'https://www.cftc.gov/dea/futures/deaerissf.htm']

main(url_list)