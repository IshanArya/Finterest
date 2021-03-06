import requests
import json
import csv
import pickle
import os
from .blackrock import generateReport

dirname = os.path.dirname(__file__)

def get_analysis(ticker):
    return generateReport(ticker)

def is_ticker(ticker):
    with open(str(dirname)+'/data/stocks/stocks.pickle', 'rb') as stocks:
        stocks = pickle.load(stocks)
    return ticker in stocks

def get_ticker(name):
    name = name.lower()
    with open(str(dirname)+'/data/stocks/tickers.pickle', 'rb') as stocks:
        tickers = pickle.load(stocks)
    tickers['netflix'] = 'NFLX'
    tickers['google'] = 'GOOG'
    tickers['microsoft'] = 'MSFT'
    tickers['amazon.com'] = "AMZN"
    tickers['amazon'] = "AMZN"

    if name not in tickers:
        return None
    return tickers[name]

def parse_stock_tickers():
    with open("data/stocks/companylist.csv") as stocks:
        csv_reader = csv.reader(stocks, delimiter=',')
        is_first = True
        stocks = []
        for row in csv_reader:
            if is_first:
                is_first = False
                continue
            stocks.append(row[0].upper())

        stocks = set(stocks)

        with open('data/stocks/stocks.pickle', 'wb') as handle:
            pickle.dump(stocks, handle)

        return stocks

def parse_company_and_ticker():
    with open("/Users/brianmodel/Desktop/HackGT2018/flaskapp/utils/data/stocks/companylist.csv", 'r') as stocks:
        csv_reader = csv.reader(stocks, delimiter=',')
        is_first = True
        stocks = {}
        for row in csv_reader:
            if is_first:
                is_first=False
                continue
            company_name = row[1]
            stocks[company_name.lower()] = row[0]

        with open(dirname+'/Users/brianmodel/Desktop/HackGT2018/flaskapp/utils/data/stocks/tickers.pickle', 'wb') as handle:
            pickle.dump(stocks, handle)

    return stocks

# if __name__ == '__main__':
    # ticker = get_ticker('amazon')
    # print(ticker)
    # print(dirname)
    # is_ticker('AMZN')
    # parse_company_and_ticker()
    