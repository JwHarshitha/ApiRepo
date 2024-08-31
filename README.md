# ApiRepo
##### API Exploration and Understanding Project
### Project Purpose
The purpose of this project is to explore and understand how to interact with APIs, specifically using the CoinGecko API. The project involves making GET requests to an API endpoint, inspecting JSON responses, and extracting specific data using Python.

### API Used
This project uses the CoinGecko API to retrieve market data for cryptocurrencies. The endpoint used provides information about the top cryptocurrencies by market cap.

### Endpoint
## URL:
 https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false

### Tools and Libraries
## Postman: 
Used to make GET requests to the API and inspect the JSON response structure.

## Python: 
The project uses Python to interact with the API and extract data.

## Requests Library: 
A Python library used to make HTTP requests.

You can install it using:-
pip install requests

### Steps Taken
## 1. Making an API Request with Postman
Use Postman to send a GET request to the CoinGecko API endpoint.
Example URL: https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false
Inspect the JSON response returned by the API to understand its structure.

## 2. Making an API Request in Python
Use the requests library to make the same API call in Python.

## 3. Inspecting the JSON Response
Analyze the JSON response structure to identify key data points such as cryptocurrency names, prices, and market caps.

## 4. Extracting Data Using Python Dictionaries
Extract specific data points from the JSON response using Python dictionaries.

## 5. Practicing Data Extraction
Practice extracting different types of data (e.g., strings, numbers, lists) from the JSON response.
Experiment with extracting and printing various pieces of information to deepen your understanding.

### Conclusion
This project provides a hands-on approach to learning how to interact with APIs, use Postman for testing, and extract meaningful data using Python. It’s a valuable exercise for anyone interested in understanding cryptocurrency market data and API interactions.