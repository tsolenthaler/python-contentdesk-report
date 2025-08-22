import requests

def checkUrl(products):
    results = []
    checkProperty = 'url'
    for product in products:
        print(f"Checking Objekt: {product['identifier']}")
        if checkProperty in product:
            results.append({'sku': product['identifier'], 'uuid': product['uuid'], 'url': product['url']})
        else:
            print(f"No URL found for product: {product['identifier']}")
    return results