from downloadMongoDB import downloadMongoDB
from downloadNodeJS import downloadNodeJS
from downloadVSCode import downloadVSCode

def downloadDevTools():
    downloadMongoDB()
    downloadNodeJS()
    downloadVSCode()

downloadDevTools()