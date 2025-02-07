"""
Program to test the json file created by the data fetched from the polygon api
"""
import pytest
import json

def test_check_open_less_than_or_equal_to_close():
    with open('E:/ApexaIQ/APEXA_PART2/Finhub_API/nifty50_stock_data.json', 'r') as file:
        stock_data = json.load(file)
    
    for symbol, data in stock_data.items():
        open_price = data['open']
        close_price = data['close']
        high_price = data['high']
        condition = open_price <= close_price
        
        assert condition, f"Test failed for {symbol}: Open price is > close price. Hence loss making"

def test_check_difference_at_least_4():
    with open('E:/ApexaIQ/APEXA_PART2/Finhub_API/nifty50_stock_data.json', 'r') as file:
        stock_data = json.load(file)
    
    for symbol, data in stock_data.items():
        open_price = data['open']
        close_price = data['close']
        high_price = data['high']
        condition = close_price - open_price >= 4
        
        assert condition, f"Test failed for {symbol}: The stock move positive by >=4 points"
