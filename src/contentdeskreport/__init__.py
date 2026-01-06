from contentdeskreport.extract.extract import Extraction
from contentdeskreport.transform.transform import Transform
from contentdeskreport.check.checks import Checks
from contentdeskreport.load.load import Load

class ContentdeskReport:
    """
    ContentdeskReport class to extract data from a given target and generate a markdown file.
    """
    def __init__(self, host, clientid, secret, user, passwd, cdnurl, projectPath, organization, name, website, organization_website, email, region):
        print("INIT - ContentdeskReport")
        self.host = host
        self.clientid = clientid
        self.secret = secret
        self.user = user
        self.passwd = passwd
        self.cdnurl = cdnurl
        self.projectPath = projectPath
        self.extractProducts = Extraction(self.host, self.clientid, self.secret, self.user, self.passwd)
        self.saveProducts()
        self.debugExtractProducts()
        #self.checks = Checks(self.extractProducts.getProducts(), self.projectPath, self.cdnurl)
        self.transformProducts = Transform(self.extractProducts.getProducts(), self.projectPath, self.cdnurl)
        #self.debugTransformProducts()
        self.loadProducts = Load(self.transformProducts.getTransformProducts(), self.projectPath, organization, name, website, organization_website, email, region, self.transformProducts.getTransformProductsAkeneo())
        #self.debugLoadProducts()
    
    def getExtractProducts(self):
        """
        Returns the extracted products.
        """
        return self.extractProducts
    
    def getTransformProducts(self):
        return self.transformProducts
    
    def getLoadProducts(self):
        return self.loadProducts
    
    def saveProducts(self):
        Load.createJsonFile(self.extractProducts.getProducts(), "original", "products", self.projectPath)
    
    def debugExtractProducts(self):
        Load.debugToFile(self.extractProducts.getProducts(), "extractProducts", self.projectPath)
        print("Debug file extractProducts created")
        
    def debugLoadProducts(self):
        Load.debugToFile(self.checks, "loadProducts", self.projectPath)
        print("Debug file loadProducts created")