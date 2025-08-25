import os
import requests
import json

class CheckUrlExist:
    def __init__(self, projectPath, productsUrl):
        self.projectPath = projectPath
        self.productsUrl = productsUrl
        self.startCheck()

    def checkUrl(self, products):
        results = []
        checkProperty = 'url'
        for product in products:
            print(f"Checking Objekt: {product['identifier']}")
            if checkProperty in product:
                print(f"Found URL: {product[checkProperty]} for product: {product['identifier']}")
                results.append({'identifier': product['identifier'], 'uuid': product['uuid'], 'url': product['url']})
            else:
                print(f"No URL found for product: {product['identifier']}")
        return results

    def loadProducts(self):
        product_file_path = os.path.join(self.projectPath, "api", "LodgingBusiness.json")
        print("Product File Path: ", product_file_path)
        if os.path.exists(product_file_path):
            with open(product_file_path, "r") as file:
                products = json.load(file)
            return products
        else:
            print(f"File {product_file_path} does not exist.")
            return []
        
    def loadProductsToFile(self, products, fileName):        
        # Check if folder exists
        # TODO: Fix Folder Path by Settings
        print("Folder Path: ", self.projectPath+"/api/check/"+fileName+".json")
        if not os.path.exists(self.projectPath+"/api/check/"):
            os.makedirs(self.projectPath+"/api/check/")

        with open(self.projectPath+"/api/check/"+fileName+".json", "w", encoding="utf-8") as file:
            file.write(json.dumps(products))

    def loadProductsFromUrl(self):
        try:
            response = requests.get(self.productsUrl+"/api/LodgingBusiness.json")
            response.raise_for_status()  # Raise an error for HTTP errors
            products = response.json()
            return products
        except requests.RequestException as e:
            print(f"Error loading products from URL: {e}")
            return []

    def startCheck(self):
        print ("Load Products from URL "+ self.productsUrl+"/api/LodgingBusiness.json")
        products = self.loadProductsFromUrl()
        print("Check Produkte by URL exist")
        results = self.checkUrl(products)
        print("Add Result to File")
        self.loadProductsToFile(results, "checkUrlExist")