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
        #self.countProducts = len(self.checks)
        #self.typesClass = self.loadAllTypes()
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
    
        return self.products
    
    def loadProductsToFile(self, products, fileName):        
        # Check if folder exists
        # TODO: Fix Folder Path by Settings
        print("Folder Path: ", self.projectPath+"/api/"+fileName+".json")
        if not os.path.exists(self.projectPath+"/api/"):
            os.makedirs(self.projectPath+"/api/")
        
        with open(self.projectPath+"/api/"+fileName+".json", "w", encoding="utf-8") as file:
            file.write(json.dumps(products))

        
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
            file.write("# OpenData Portal - "+self.organization+"\n\n")
            #file.write(str(self.countProducts)+ " freie Datensätze\n\n")
            file.write("Die hier veröffentlichten Daten stehen kostenlos zur Verfügung und können mit einer [CC BY-SA](https://creativecommons.org/licenses/by-sa/4.0/deed.de) Lizenz frei wiederverwendet werden. \n\n")
            #file.write("[Dokumentation](documentation)\n\n")
            file.write("## Was ist Open Data?\n\n")
            file.write("„Open Data“ bedeutet: Daten, die frei zugänglich, kostenlos nutzbar und von jedem weiterverwendet werden dürfen – ganz ohne komplizierte Bedingungen.\n\n")
            file.write("## Wozu dient dieses Portal?\n")
            
            file.write("Dieses Portal richtet sich an:\n\n")
            file.write(" * **Reiseveranstalter, Hotels und Touristiker**, die aktuelle Informationen zu Veranstaltungen, Ausflugszielen oder Unterkünften suchen,\n")
            file.write(" * **Medien, Entwickler oder Startups**, die auf Basis der Daten neue Anwendungen oder Angebote entwickeln möchten,\n")
            file.write(" * **interessierte Bürgerinnen und Bürger**, die einen Einblick in die touristische Vielfalt der Region erhalten möchten.\n\n")
         
            file.write("## Was finde ich hier?\n\n")
            file.write("Sie finden unter anderem Daten zu:\n\n")
            file.write("* 📍 **Punkten**, wie Unterkünfte, Restaurants oder Ausflugsziele\n")
            file.write("* 🗺️ **Linien**, wie Routen und Touren\n")
            file.write("* 📅 **Events**, wie Messen, Sportveranstaltungen, uvm.\n")
            file.write("* 📰 **Artikel**, wie News, Produkte o.ä.\n")
            file.write("* 📷 **Medien**, wie Webcams, Bilder, Videos o.ä.\n")
            file.write("Diese Daten stammen direkt von unseren touristischen Partnern und werden regelmässig aktualisiert.\n\n")
            
            file.write("## Wie kann ich die Daten nutzen?\n\n")
            file.write("* Wenn Sie möchten, können Sie die Daten herunterladen.\n")
            file.write("* Sie dürfen die Daten in eigene Projekte, Websites oder Broschüren einbauen - die Daten dürfen:\n\n")
            file.write("✅ vervielfältigt, verbreitet und öffentlich zugänglich gemacht werden\n\n")
            file.write("✅ angereichert und bearbeitet werden\n\n")
            file.write("✅ kommerziell genutzt werden\n\n")

            #file.write("## Lizenz\n")
            #file.write(self.splitStringtoList(self.license))
            #file.write("\n\n")
            #file.write("## "+str(self.countProducts)+" freie Datensätze\n")

            file.write("| Daten      | Format                           | Ansehen\n")
            file.write("| ----------- | --------------------------------| ----------- |\n")

            
            file.write("\n\n")
            file.write("### Haftungsausschluss\n\n")
            file.write("* "+self.organization+" schliesst jede Haftung für direkte und indirekte Schäden durch die Datennutzung aus. Es wird keine Garantie für die Aktualität, Richtigkeit, Vollständigkeit und Genauigkeit der veröffentlichten Daten übernommen.\n\n")
            
            file.write("## Noch Fragen?\n\n")
            file.write("Weitere Informationen sind in der Entwicklerdokumentation zu finden:\n\n")
            file.write("* [📒 Dokumentation](documentation)\n\n")
            file.write("* [📄 Changelog ](changelog)\n\n")
            file.write("Wenn Sie unsicher sind, wie Sie die Daten nutzen können oder weitere Informationen wünschen, melden Sie sich gerne bei uns:\n\n")
            file.write("* 📧 [E-Mail](mailto:"+str(self.email)+")\n")
            
        print(f"Markdown file created at: {markdown_file_path}")