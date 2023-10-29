## todo get data for k'se
## make graph with commshort
## make graph with osz

## get html for one url
## get data from html
## structure data into graph

## data for input:
#   {name:{date:data, date:data, }

# TODO oszilator repair
# TODO database with all parsed da

import requests
import html
import re
import xlsxwriter

from xml.etree import ElementTree as ET
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

#from suricate_url import url_list
from testing_urls_suricate import url_list

names = []
dates = []
data = {}

def get_data_from_url(url):
    html_raw = str(BeautifulSoup(html.unescape(requests.get(url).text), features='html.parser').find('table', id="exceltable"))

    date = re.findall('[0-9]{4}-[0-9]{2}-[0-9]{2}', string=str(url))[0]
    print(date)
    date = int(date.replace('-', '')) - 20000000
    dates.append(date)

    a = []
    table = ET.XML(html_raw)
    rows = iter(table)
    headers = [col.text for col in next(rows)]

    for row in rows:
        values = [col.text for col in row]
        a.append(dict(zip(headers, values)))

    for i in a:
        if int(i['CommShort']) < 0:
            #i['CommShort'] = int(i['CommShort'])*-1
            pass

        if i['Name'] in data:
            data[i['Name']][date] = {'OpenInterest': int(i['OpenInterest']), 'CommLong':int(i['CommLong']), 'CommShort':int(i['CommShort'])}
        else:
            data[i['Name']] = {}
            data[i['Name']][date] = {'OpenInterest': int(i['OpenInterest']), 'CommLong':int(i['CommLong']), 'CommShort':int(i['CommShort'])}

def oszilator(name='Gold'):
    #aus 25 zeilen das maximum
    dates_list = list(data[name].keys())
    dates_list.sort()
    y_oszilator_values = []
    data_for_equation = {}
    comm_nettos = []
    used_dates = []

    for date in dates_list:
        print(date)
        if dates_list.index(date) > 24:
            nettos_for_date = []
            index_int = dates_list.index(date)
            print(index_int)
            twentysix_dates = dates_list[index_int-25:index_int+1]
            print(len(twentysix_dates))

            for i in twentysix_dates:
                netto = data[name][i]['CommLong'] - data[name][i]['CommShort']
                print(data[name][i]['CommLong'], data[name][i]['CommShort'], i, netto)
                nettos_for_date.append(netto)

            max_netto = max(nettos_for_date)
            min_netto = min(nettos_for_date)
            current_netto = data[name][date]['CommLong'] - data[name][date]['CommShort']

            print(max_netto, min_netto, current_netto)

            current_min = current_netto - min_netto
            max_min = max_netto - min_netto
            osz = current_min/max_min
            osz = osz*100
            y_oszilator_values.append(osz)
            used_dates.append(date)
            print(current_min, max_min, osz)

    return used_dates, y_oszilator_values

def build_graph(name='Gold'):
    dates_list = list(data[name].keys())
    dates_list.sort()
    x_axis_dates = []
    x_used_dates = []
    y_axis_data = []
    x_counter = 1

    for i in dates_list:
        print(i, data[name][i]['CommShort'])
        x_used_dates.append(i)
        x_axis_dates.append(x_counter)
        x_counter += 1
        y_axis_data.append(int(data[name][i]['CommShort']))

    osz = oszilator(name=name)
    x_osz = []
    x_counter = 1
    for i in osz[1]:
        x_osz.append(x_counter)
        x_counter += 1

    return x_axis_dates, y_axis_data, x_osz, osz[1], osz[0], x_used_dates

    ##    plt.plot(x_axis_dates, y_axis_data, label = name)
    ##    plt.plot(x_osz, osz[1], label = 'osz')
    ##    plt.show()

for url in url_list:
    get_data_from_url(url)


#build_graph()