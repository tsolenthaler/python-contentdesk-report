import contentdeskreport.check.checkUrl as checkUrl

class Checks:
    def __init__(self, products, projectPath, cdnurl):
        print("Checks")
        self.products = products
        self.projectPath = projectPath
        self.cdnurl = cdnurl
        self.ResultCheckUrl = checkUrl.checkUrl(self.products)