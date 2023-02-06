import pathlib, ctypes
import Controllers.System as System
from subprocess import Popen
from pymongo import MongoClient
from pymongo import database

def startDB():
  if System.get_service('MongoDB')['status'] == 'stopped':
    System.runAsAdmin(['net','start','MongoDB'])

#Cannot Shut Down MongoDB at this time
def stopDB():
  if System.get_service('MongoDB')['status'] == 'running':
    System.runAsAdmin(['net','stop','MongoDB'])

#Starts Compass
def startCompass():
   Popen('mongodbcompass.exe')

def dbConnect(constr:str, dbname:str):

  # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
  client = MongoClient(constr)

  # Create the database
  return client[dbname]


def newDatabase():...
def readDatabase():...
def updateDatabase():...
def dropDatabase():...
def newCollection():...
def readCollection():...
def updateCollection():...
def dropCollection():...
def newDocument():...
def readDocument():...
def updateDocument():...
def dropDocument():...