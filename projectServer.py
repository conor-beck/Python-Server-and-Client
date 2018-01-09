import re
from socket import *
import pickle
import json
import os.path
import datetime
import sys
BUFFER_SIZE = 1999999990
class Group:
    def __init__(self, name, posts, iD):
        self.name = name
        self.posts = posts
        self.iD = iD
    def getGroupName(self):
        return self.name
    def getPosts(self):
        return self.posts
    def getId(self):
        return self.iD
    def setPosts(self, p):
        self.posts = p
class Post:
    def __init__(self, date, author, title, content):
        self.date = date
        self.author = author
        self.title = title
        self.content = content
    def getDate(self):
        return self.date
    def getAuthor(self):
        return self.author
    def getTitle(self):
        return self.title
    def getContent(self):
        return self.content
def agHandle():
    with open('groupData.pickle', 'rb') as handle:
        data = pickle.load(handle)
    data = pickle.dumps(data)
    return data
def rewriteHandle(c, s):
    c.close()
    c, addr = s.accept()
    theFile = c.recv(BUFFER_SIZE)
    da = pickle.loads(theFile)
    with open('groupData.pickle', 'wb') as handle:
        pickle.dump(da, handle, protocol=pickle.HIGHEST_PROTOCOL)
def rgHandle():
    with open('groupData.pickle', 'rb') as handle:
        data = pickle.load(handle)
    data = pickle.dumps(data)
    return data
serverPort = 8007
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)

while 1:
    
    connectionSocket, addr = serverSocket.accept()
    
    inpu = connectionSocket.recv(1024)
    if inpu == 'ag':
        d = agHandle()
        connectionSocket.send(d)
    elif inpu == 'rg':
        d = rgHandle()
        connectionSocket.send(d)
    else:
        rewriteHandle(connectionSocket, serverSocket)
    connectionSocket.close()
    
