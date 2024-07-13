import requests, testify
import logging

logging.basicConfig(filename='test.csv',level=logging.INFO)

def get_links():
    resp = requests.get('http://py-api-srv:5000/')
    data = resp.json()
    return data['links']

def main():
    """assert that endpoint is valid"""
    
    BASE = 'http://java-srv:8080'
    with open('test.csv', 'w+') as f:
        for url in get_links():
            resp = requests.get(f'{BASE}/{url}')
            line = f'{url},{resp.status_code}'
            f.write(line)
            # if testify.assert_equal(resp.status_code, 200):
            #     logging.info(f'{url},pass')
            # else:
            #     logging.info(f'{url},failed')

    print('Done')
    
if __name__ == '__main__':
    main()