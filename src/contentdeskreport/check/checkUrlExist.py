import os
import requests
import json

class CheckUrlExist:
    def __init__(self, projectPath):
        self.projectPath = projectPath
        self.startCheck()

    def checkUrl(self, products):
        results = []
        checkProperty = 'url'
        for product in products:
            print(f"Checking Objekt: {product['identifier']}")
        if checkProperty in product:
            results.append({'sku': product['identifier'], 'uuid': product['uuid'], 'url': product['url']})
        else:
            print(f"No URL found for product: {product['identifier']}")
        return results

    def loadProducts(self):
        product_file_path = os.path.join(self.projectPath, "products.json")
        print("Product File Path: ", product_file_path)
        if os.path.exists(product_file_path):
            with open(product_file_path, "r") as file:
                products = json.load(file)
            return products
        else:
            print(f"File {product_file_path} does not exist.")
            return []
        
    def loadProductsToFile(self, products, fileName, projectpath):        
        # Check if folder exists
        # TODO: Fix Folder Path by Settings
        print("Folder Path: ", projectpath+"/check/"+fileName+".json")
        if not os.path.exists(projectpath+"/check/"):
            os.makedirs(projectpath+"/check/")

        with open(projectpath+"/check/"+fileName+".json", "w", encoding="utf-8") as file:
            file.write(json.dumps(products))

    def startCheck(self):
        products = self.loadProducts()
        results = self.checkUrl(products)

        self.loadProductsToFile(results, "checkUrlExist", self.projectPath)