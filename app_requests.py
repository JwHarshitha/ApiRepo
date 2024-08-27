import requests

# url = 'http://127.0.0.1:5000/items'
url='https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false'

def get_request():
    response = requests.get(url)
    # Check the status code (200 indicates success)
    if response.status_code == 200:
        # Convert the response to JSON format
        data = response.json()
        print(data)
    else:
        # print(f'Failed to retrieve data: {response.status_code}')
        data=f'Failed to retrieve data: {response.status_code}'
    return data

def post_request():
    data = {
        'name': 'foo moon & stars Projector',
        'artist': 'xin chaun bar',
        'id': 10
    }

    # Make the POST request
    response = requests.post(url, json=data)
    # Check the status code (201 indicates resource created successfully)
    if response.status_code == 201:
        # Convert the response to JSON format
        data = response.json()
        print(data)
    else:
        # print(f'Failed to create data: {response.status_code}')
        data=f'Failed to retrieve data: {response.status_code}'
    return data

if __name__=='__main__':
    get_request()