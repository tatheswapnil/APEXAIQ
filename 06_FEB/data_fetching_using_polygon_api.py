"""
Program to get the data of stocks from the polygon api and store the information in the json file.
Problem statement is mentioned in the README file
"""
import requests
import json
import time

#polygon api

API_KEY = "sgDQ1rgpcPvQl2hM_fheY_sobQqpe_FJ"  
symbols = [
    'AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA', 'NVDA', 'BRK.B', 'JNJ', 'V', 'PG',
    'UNH', 'MA', 'HD', 'XOM', 'KO', 'PEP', 'DIS', 'CSCO', 'ADBE', 'NFLX',
    'CRM', 'ABT', 'CMCSA', 'TMO', 'ACN', 'AVGO', 'COST', 'CVS', 'DHR', 'NKE',
    'MDT', 'TXN', 'NEE', 'QCOM', 'PM', 'HON', 'LIN', 'AMGN', 'SBUX', 'IBM',
    'LMT', 'INTC', 'GE', 'MMM', 'CAT', 'GS', 'BA', 'SPGI', 'RTX', 'PYPL'
]

data = {}

for symbol in symbols:
    url = f"https://api.polygon.io/v1/open-close/{symbol}/2024-02-01?apiKey={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        result = response.json()
        if result.get("status") == "OK":
            data[symbol] = result
    time.sleep(0.5)  

# Save to a JSON file
with open("nifty50_stock_data.json", "w") as file:
    json.dump(data, file, indent=4)

print("Data saved to nifty50_stock_data.json.")
