import yfinance as yf
import os


filePath = 'closing_prices.csv'
if os.path.exists(filePath):
    os.remove(filePath)

tickers = []
data = {}

file = open('tickers.csv', 'r')
for line in file.readlines():
    line = line.replace('\n', '')
    tickers.append(line)
file.close()

years = 10
year_start = 2010

for tick in tickers:
    if tick not in data:
        data[tick] = []

    print(f"getting values for {tick}...")
    close = yf.download(tick, 
                    start=f'{year_start}-01-01', 
                    end=f'{year_start+years}-01-01', 
                    progress=False,
                )['Close'].to_list()
    data[tick].append(close)
    print(len(close))

    commas = ""
    lst = data[tick][0]
    for price in lst:
        if len(commas) != 0:
            commas = commas+','+str(price)
        else:
            commas = str(price)
    
    file = open('closing_prices.csv','a')
    file.write(tick+','+commas+'\n')
    file.close()
    print(f"{tick} written to csv...")
