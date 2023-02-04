from downloadMongoDB import downloadMongoDB
from downloadNodeJS import downloadNodeJS
from downloadVSCode import downloadVSCode
from downloadMongoDBCompass import downloadMongoCompass
from downloadMongoDBShell import downloadMongoSH

def downloadDevTools():
    downloadMongoDB()
    downloadNodeJS()
    downloadVSCode()
    downloadMongoCompass()
    downloadMongoSH()

downloadDevTools()