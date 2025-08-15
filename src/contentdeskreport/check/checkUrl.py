import requests

def checkUrl(self, products):
    results = []
    checkProperty = 'url'
    checkObjectColumn = 'name'
    for product in products:
        print(f"Checking Objekt: {product['identifier']}")
        if checkProperty in product['values']:
            url = product['values'][checkProperty][0]['data']
            try:
                response = requests.head(url, timeout=5, allow_redirects=True)
                if response.status_code < 400:
                    status = 'OK'
                else:
                    status = f'Error {response.status_code}'
            except Exception as e:
                status = f'Failed ({e.__class__.__name__})'
            results.append({'sku': product['identifier'], 'uuid': product['uuid'], 'url': url, 'status': status})
        else:
            status = 'No URL'
            
    return results