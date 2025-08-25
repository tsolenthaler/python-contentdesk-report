import json
import os
from datetime import datetime

class Load:
    
    def __init__(self, products, projectPath, organization, name, website, organization_website, email, region):
        self.products = products
        self.projectPath = projectPath
        self.organization = organization
        self.name = name
        self.website = website
        self.organization_website = organization_website
        self.email = email
        self.region = region
        #self.checks = checks
        self.countProducts = len(self.products)
        self.typesClass = self.loadAllTypes()
        self.loadProducts = self.setLoadProducts()
        #self.loadChecks = self.setLoadChecks()
        self.createMarkDownFileIndex()
               
    def getLoadProducts(self):
        return self.loadProducts
    
    #def setLoadChecks(self):
    #    self.loadProductsToFile(self.checks.ResultCheckUrl, "checkUrl")

    def setLoadProducts(self):
        # All Products to api/products.json
        self.loadProductsToFile(self.products, "products")
        
        self.createProductListbyParentTyp("Place")
        self.createProductListbyParentTyp("Accommodation")
        self.createProductListbyParentTyp("CivicStructure")
        self.createProductListbyParentTyp("AdministrativeArea")
        self.createProductListbyParentTyp("TransportationSystem")
        self.createProductListbyParentTyp("LocalBusiness")
        self.createProductListbyParentTyp("FoodEstablishment")
        self.createProductListbyParentTyp("LodgingBusiness")
        self.createProductListbyParentTyp("Tour")
        self.createProductListbyParentTyp("Webcam")
        self.createProductListbyParentTyp("Event")
        self.createProductListbyParentTyp("Product")
        self.createProductListbyParentTyp("CreativeWork")
        self.createProductListbyParentTyp("MediaObject")
    
        return self.products
    
    def loadProductsToFile(self, products, fileName):        
        # Check if folder exists
        # TODO: Fix Folder Path by Settings
        print("Folder Path: ", self.projectPath+"/api/"+fileName+".json")
        if not os.path.exists(self.projectPath+"/api/"):
            os.makedirs(self.projectPath+"/api/")
        
        with open(self.projectPath+"/api/"+fileName+".json", "w", encoding="utf-8") as file:
            file.write(json.dumps(products))

    def createProductListbyParentTyp(self, typeClass):
        types = self.setTypesListbyParent(typeClass)
        products = self.getProductsbyTypes(types)
        self.loadProductsToFile(products, typeClass)
        return products
    
    def setTypesListbyParent(self, parentType):
        types = []
        for typeClass in self.typesClass:
            if self.typesClass[typeClass]['parent'] == parentType:
                types.append(typeClass)
            elif typeClass == parentType:
                types.append(typeClass)
        return types
    
    def getProductsbyTypes(self, types):
        products = []
        for product in self.products:
            if product.get("family") in types:
                products.append(product)
                
        return products
        
    def debugToFile(products, fileName, projectPath):
         # get current date and time
        current_datetime = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        #print("Current date & time : ", current_datetime)
        
        # convert datetime obj to string
        str_current_datetime = str(current_datetime)
        # Check if folder exists
        print("Folder Path: ", projectPath+"/debug/"+str_current_datetime)
        if not os.path.exists(projectPath+"/debug/"+str_current_datetime):
            os.makedirs(projectPath+"/debug/"+str_current_datetime+"/")
        
        with open(projectPath+"/debug/"+str_current_datetime+"/"+fileName+".json", "w") as file:
            file.write(json.dumps(products))
    
    def createMarkDownString(self, name, filename, count):
        string = ""
        
        #string += "["+name+" ("+str(count)+")](/api/"+filename+".json)\n\n"

        string += "| ["+name+" ("+str(count)+")](/api/"+filename+".json)       | [:material-code-json:](/api/"+filename+".json){ .md-button } [:fontawesome-solid-file-csv:](/api/"+filename+".csv){ .md-button } [:simple-rss:](/api/"+filename+".rss){ .md-button }  |\n"
        
        return string
    
    def checkLengthinFile(self, fileName):
        # load the JSON file to check the Objekt lenght in de File
        file_path = os.path.join(self.projectPath, "api", fileName + ".json")
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                data = json.load(file)
                # Check the length of the JSON object
                if isinstance(data, list):
                    length = len(data)
                    print(f"Length of {fileName}: {length}")
                    return length
                else:
                    print(f"{fileName} is not a list.")
                    return 0
    
    def splitStringtoList(self, string):
        newstring = ''
        # Split the string by commas and strip whitespace
        items = [item.strip() for item in string.split(',') if item.strip()]
        for item in items:
            if item:
                newstring += '* '+item + '\n'
        return newstring
            
    
    def createMarkDownFileIndex(self):
        # create a markdown file with the name "data.md" in the projectPath
        markdown_file_path = os.path.join(self.projectPath, "index.md")
        with open(markdown_file_path, "w", encoding='utf-8') as file:
            file.write("---\n")
            file.write("hide:\n")
            file.write("  - navigation\n")
            file.write("  - toc\n")
            file.write("---\n")
            file.write("# Report Portal\n\n")
            
            file.write("## Checks\n\n")
            file.write("| Check       | Export       |\n")
            file.write("| ----------- | ------------ |\n")
            file.write("| Check URL Exist   | /check/urlExist             |\n")
            file.write("| Check URL Valid   | /check/urlValid             |\n")
            file.write("\n\n")
            
            file.write("## Objekte nach Typ\n\n")
            file.write("| Daten      | Format                           | Ansehen\n")
            file.write("| ----------- | --------------------------------| ----------- |\n")
            dataset = self.createMarkDownString("Alle Produkte", "products", self.checkLengthinFile("products"))
            if self.checkLengthinFile("Place") > 0:
                dataset += self.createMarkDownString("Orte", "Place", self.checkLengthinFile("Place"))
            if self.checkLengthinFile("Accommodation") > 0:
                dataset += self.createMarkDownString("Unterkünfte", "Accommodation", self.checkLengthinFile("Accommodation"))
            if self.checkLengthinFile("CivicStructure") > 0:
                dataset += self.createMarkDownString("Öffentliche Anlage/Einrichtung", "CivicStructure", self.checkLengthinFile("CivicStructure"))
            if self.checkLengthinFile("AdministrativeArea") > 0:
                dataset += self.createMarkDownString("Verwaltungsgebiet", "AdministrativeArea", self.checkLengthinFile("AdministrativeArea"))
            if self.checkLengthinFile("TransportationSystem") > 0:
                dataset += self.createMarkDownString("Transportsystemstation", "TransportationSystem", self.checkLengthinFile("TransportationSystem"))
            if self.checkLengthinFile("LocalBusiness") > 0:
                dataset += self.createMarkDownString("Lokale Geschäfte / Freizeit / Dienstleistung", "LocalBusiness", self.checkLengthinFile("LocalBusiness"))
            if self.checkLengthinFile("FoodEstablishment") > 0:
                dataset += self.createMarkDownString("Gastronomie", "FoodEstablishment", self.checkLengthinFile("FoodEstablishment"))
            if self.checkLengthinFile("LodgingBusiness") > 0:
                dataset += self.createMarkDownString("Beherbergungsbetrieb", "LodgingBusiness", self.checkLengthinFile("LodgingBusiness"))
            if self.checkLengthinFile("Tour") > 0:
                dataset += self.createMarkDownString("Tour", "Tour", self.checkLengthinFile("Tour"))
            if self.checkLengthinFile("Webcam") > 0:
                dataset += self.createMarkDownString("Webcam", "Webcam", self.checkLengthinFile("Webcam"))
            if self.checkLengthinFile("Event") > 0:
                dataset += self.createMarkDownString("Event", "Event", self.checkLengthinFile("Event"))
            if self.checkLengthinFile("Product") > 0:
                dataset += self.createMarkDownString("Produkte", "Product", self.checkLengthinFile("Product"))
            if self.checkLengthinFile("CreativeWork") > 0:
                dataset += self.createMarkDownString("Kreative Arbeit", "CreativeWork", self.checkLengthinFile("CreativeWork"))
            if self.checkLengthinFile("MediaObject") > 0:
                dataset += self.createMarkDownString("Medienobjekt", "MediaObject", self.checkLengthinFile("MediaObject"))
            file.write(dataset)
            file.write("\n\n")

        print(f"Markdown file created at: {markdown_file_path}")
        
    def loadAllTypes(self):
        types_file_path = os.path.join(self.projectPath, "types.json")
        print("Types File Path: ", types_file_path)
        if os.path.exists(types_file_path):
            with open(types_file_path, "r") as file:
                types = json.load(file)
            return types
        else:
            print(f"File {types_file_path} does not exist.")
            return []