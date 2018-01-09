import sys
import re
from socket import *
import pickle
import json
import os.path
import datetime
serverName = sys.argv[1]
serverPort = int(sys.argv[2])
BUFFER_SIZE = 1999999990

# name = 'user.pickle'
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
    
    

def ag(inpu, socket, d):
    j = 0
    sMarker = '(s)'
    nMarker = '( )'
    if len(inpu) > 1:
        
        size = inpu[1]
        size = int(size)
        sendThis = 'ag'
        
        socket.send(sendThis)
        re = socket.recv(BUFFER_SIZE)
        servGroups = pickle.loads(re)
        while j < len(servGroups):
            #k = 0
            tempGroups = []
            pos = len(servGroups) - j
            toGo = pos - size
            if toGo < 0:
                thisMuch = size + toGo
                l = 0
                while l < thisMuch:
                    gName = servGroups[j].getGroupName()
                    tempGroups.append(gName)
                    num = str(j + 1)
                    display = num + '. ' + nMarker + ' ' + gName
                    n = 0
                    while n < len(d[0]):
                        if d[0][n] == gName:
                            num = str(j + 1)
                            display = num + '. ' + sMarker + ' ' + gName
                        
                            
                        n = n + 1
                    print(display)
                        
                    j = j + 1
                    l = l + 1
                p = 1
                while p == 1:
                    co = raw_input('input:')
                    co = co.split()
                    if co[0] == 's':
                        if len(co) > 2:
                            k = 1
                            while k < len(co):
                                target = int(co[k]) - 1
                                targetName = tempGroups[target]
                                d[0].append(targetName)
                                k = k + 1
                        else:
                            target = int(co[1]) - 1
                            targetName = tempGroups[target]
                            d[0].append(targetName)
                    elif co[0] == 'u':
                        if len(co) > 2:
                            k = 1
                            while k < len(co):
                                target = int(co[k]) - 1
                                targetName = tempGroups[target]
                                d[0].remove(targetName)
                                k = k + 1
                        else:
                            target = int(co[1])
                            targetName = tempGroups[target]
                            d[0].remove(targetName)
                    elif co[0] == 'n':
                        p = 0
                    elif co[0] == 'q':
                        p = 0
                    else:
                        print('Unsupported input')
            
            else:
                l = 0
                while l < size:
                    gName = servGroups[j].getGroupName()
                    tempGroups.append(gName)
                    num = str(j + 1)
                    display = num + '. ' + nMarker + ' ' + gName
                            
                    n = 0
                    while n < len(d[0]):
                        if d[0][n] == gName:
                            num = str(j + 1)
                            display = num + '. ' + sMarker + ' ' + gName
                        n = n + 1
                            
                    print(display)
                        
                    j = j + 1
                    l = l + 1
                p = 1
                while p == 1:
                    co = raw_input('input:')
                    co = co.split()
                    if co[0] == 's':
                        if len(co) > 2:
                            k = 1
                            while k < len(co):
                                target = int(co[k]) - 1
                                targetName = tempGroups[target]
                                d[0].append(targetName)
                                k = k + 1
                        else:
                            target = int(co[1]) - 1
                            targetName = tempGroups[target]
                            d[0].append(targetName)
                    elif co[0] == 'u':
                        if len(co) > 2:
                            k = 1
                            while k < len(co):
                                target = int(co[k]) - 1
                                targetName = tempGroups[target]
                                d[0].remove(targetName)
                                k = k + 1
                        else:
                            target = int(co[1])
                            targetName = tempGroups[target]
                            d[0].remove(targetName)
                    elif co[0] == 'n':
                        p = 0
                    elif co[0] == 'q':
                        if j != len(servGroups):
                            j = 1000
                        p = 0
                    else:
                        print('Unsupported input')
                        
        
    else:
        sendThis = 'ag'
        socket.send(sendThis)
        re = socket.recv(BUFFER_SIZE)
        servGroups = pickle.loads(re)
        p = 0
        tempGroups = []
        while p < len(servGroups):
            gName = servGroups[p].getGroupName()
            num = p + 1
            st = str(num)
            display = st + '. ' + nMarker + ' ' + gName
            a = 0
            while a < len(d[0]):
                
                if d[0][a] == gName:
                    num = p + 1
                    st = str(num)
                    display = st + '. ' + sMarker + ' ' + gName
                a = a + 1
            
            
            print(display)
            tempGroups.append(gName)
            p = p + 1
        p = 1
        while p == 1:
            co = raw_input('input:')
            co = co.split()
            if co[0] == 's':
                if len(co) > 2:
                    k = 1
                    while k < len(co):
                        target = int(co[k]) - 1
                        targetName = tempGroups[target]
                        d[0].append(targetName)
                        k = k + 1
                else:
                    target = int(co[1]) - 1
                    targetName = tempGroups[target]
                    d[0].append(targetName)
            elif co[0] == 'u':
                if len(co) > 2:
                    k = 1
                    while k < len(co):
                        target = int(co[k]) - 1
                        targetName = tempGroups[target]
                        d[0].remove(targetName)
                        k = k + 1
                else:
                    target = int(co[1]) - 1
                    targetName = tempGroups[target]
                    
                    d[0].remove(targetName)
            elif co[0] == 'n':
                p = 0
            elif co[0] == 'q':
                p = 0
            else:
                print('Unsupported input')
    
    return d
            
def login(inpu):
    userId = inpu
    fileN = inpu + '.pickle'
    # (os.path.isfile(file) == True):
    with open(fileN, 'rb') as handle:
        data = pickle.load(handle)
    return data    
def sg(inpu, s, d):
    j = 0
    if len(inpu) > 1:
        size = inpu[1]
        size = int(size)
        servGroups = d[0]
        while j < len(servGroups):
            #k = 0
            tempGroups = []
            pos = len(servGroups) - j
            toGo = pos - size
            if toGo < 0:
                thisMuch = size + toGo
                l = 0
                while l < thisMuch:
                    gName = servGroups[j].getGroupName()
                    tempGroups.append(gName)
                   # n = 0
                    num = j + 1
                    num = str(j)
                    display = num + '. ' + gName
                    print(display)
                    j = j + 1
                    l = l + 1
                p = 1
                while p == 1:
                    co = raw_input('input:')
                    co = co.split()
                    
                    if co[0] == 'u':
                        if len(co) > 2:
                            k = 1
                            while k < len(co):
                                target = int(co[k]) - 1
                                targetName = tempGroups[target]
                                d[0].remove(targetName)
                                k = k + 1
                        else:
                            target = int(co[1]) - 1
                            targetName = tempGroups[target]
                            d[0].remove(targetName)
                    elif co[0] == 'n':
                        p = 0
                    elif co[0] == 'q':
                        p = 0
                    else:
                        print('Unsupported input')
            
            else:
                l = 0
                while l < size:
                    gName = servGroups[j]
                    tempGroups.append(gName)
                    n = 0
                    num = j + 1
                    num = str(num)
                    display = num + '. ' + gName
                    print(display)
                    j = j + 1
                    l = l + 1
                p = 1
                while p == 1:
                    co = raw_input('input:')
                    co = co.split()
                    if co[0] == 'u':
                        if len(co) > 2:
                            k = 1
                            while k < len(co):
                                target = int(co[k]) - 1
                                targetName = tempGroups[target]
                                d[0].remove(targetName)
                                k = k + 1
                        else:
                            target = int(co[1]) - 1
                            targetName = tempGroups[target]
                            d[0].remove(targetName)
                    elif co[0] == 'n':
                        p = 0
                    elif co[0] == 'q':
                        if j != len(servGroups):
                            j = 1000
                        p = 0
                    else:
                        print('Unsupported input')
                        
        
    else:
        
        servGroups = d[0]
        p = 0
        tempGroups = []
        while p < len(servGroups):
            gName = servGroups[p]
            num = p + 1
            num = str(num)
            display = num + '. ' + gName
            print(display)
            tempGroups.append(gName)
            p = p + 1
        p = 1
        while p == 1:
            co = raw_input('input:')
            co = co.split()
            
            if co[0] == 'u':
                if len(co) > 2:
                    k = 1
                    while k < len(co):
                        target = int(co[k]) - 1
                        targetName = tempGroups[target]
                        d[0].remove(targetName)
                        k = k + 1
                else:
                    target = int(co[1]) - 1
                    targetName = tempGroups[target]
                    d[0].remove(targetName)
            elif co[0] == 'n':
                p = 0
            elif co[0] == 'q':
                p = 0
            else:
                print('Unsupported input')
    return d
def update(dat, socke):
    socke.close()
    socke = socket(AF_INET, SOCK_STREAM)
    socke.connect((serverName,serverPort))
    toSend = 'u'
    socke.send(toSend)
    socke.close()
    socke = socket(AF_INET, SOCK_STREAM)
    socke.connect((serverName,serverPort))
    toSend = pickle.dumps(dat)
    socke.send(toSend)
    
def rg(inpu, socket, d):
        sendThis = 'rg'
        socket.send(sendThis)
        re = socket.recv(BUFFER_SIZE)
        servGroups = pickle.loads(re)
        gName = inpu[1]
        j = 0
        pos = -1
        while j < len(servGroups):
            tempName = servGroups[j]
            tempName = tempName.getGroupName()
            if gName == tempName:
                pos = j
            j = j + 1
        posts = servGroups[pos].getPosts()
        j = 0
        while j < len(posts):
            form = str(j + 1) + '. '
            form = form + str(posts[j].getDate())
            form = form + ' ' + posts[j].getTitle()
            print(form)
            j = j + 1
        j = 0
        while j == 0:
            do = raw_input('Input:')
            if do == 'q':
                j = 1
            elif do == 'p':
                title = raw_input('Post Title:')
                author = d[1]
                da = datetime.datetime.now()
                c = ''
                q = 0
                while q == 0:
                    toAdd = raw_input('Input post content: ')
                    if toAdd == '\\n.\\n':
                        q = 1
                    else:
                        c = c + ' ' + toAdd
                p = Post(da, author, title, c)
                posts.append(p)
                servGroups[pos].setPosts(posts)
                update(servGroups, socket)
                posts = servGroups[pos].getPosts()
                u = 0
                while u < len(posts):
                    form = str(u + 1) + '. '
                    form = form + str(posts[u].getDate())
                    form = form + ' ' + posts[u].getTitle()
                    print(form)
                    u = u + 1
                
            elif do == 'r':
                print('Not supported')
            elif do == 'n':
                print('Not supported')
            else:
                whereToRead = int(do)
                choice = whereToRead - 1
                print('Group: ' + gName)
                print('Subject: ' + posts[choice].getTitle())
                print('Author: ' + posts[choice].getAuthor())
                print('Date: ' + str(posts[choice].getDate()))
                print(posts[choice].getContent())
                k = 0
                while k == 0:
                    doNext = raw_input('Input:')
                    if doNext == 'q':
                        k = 1
                    else:
                        print('Input not supported')
                k = 0
                while k < len(posts):
                    form = str(k + 1) + '. '
                    form = form + str(posts[k].getDate())
                    form = form + ' ' + posts[k].getTitle()
                    print(form)
                    k = k + 1
                
        
def main():
    #clientSocket = socket(AF_INET, SOCK_STREAM)
    #clientSocket.connect((serverName,serverPort))
    i = 1
    while i == 1:
        response = raw_input("Please login or ask for help: ")
        r = response.split()
        if response == 'help':
            print "login: takes userID as argument and displays posts + subscribed groups\n"
            print "ag: takes the name of all existing groups, 'N' groups at a time\n"
            print " 	s: subscribe to groups"
            print " 	u: unsubscribe to groups"
            print " 	n: list next 'N' discussion groups"
            print " 	q: exit from ag command\n"
            print "sg: lists 'N' subscribed groups\n"
            print "rg: displays status, time stamp, subject line of all posts in 'gname' 'N' at a time\n"
            print "		[id]: number between 1 & N denoting post within list of N posts to display\n"
            print "			n: display 'N' more lines\n"
            print "			q: quit displaying the post content\n"
            print "		r: marks post as read\n"
            print "		n: list the next 'N' posts\n"
            print "		p: post to group\n"
            print "		q: quit the rg command\n"
            print "logout: logs out current user and terminates the program\n"
        else:
            data = login(response)
            i = 2
    i = 1
    while i == 1:
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((serverName,serverPort))
        #fileName = data[1] + '.pickle'
        fileName = data[1]
        fileName = fileName + '.pickle'
        #print(fileName)
        #a = raw_input('wait')
        with open(fileName, 'wb') as handle:
            pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)
        with open(fileName, 'rb') as handle:
            data = pickle.load(handle)
        response = raw_input("Please enter a command: ")
        r = response.split()
        
        if r[0] == 'help':
            print "login: takes userID as argument and displays posts + subscribed groups\n"
            print "ag: takes the name of all existing groups, 'N' groups at a time\n"
            print " 	s: subscribe to groups"
            print " 	u: unsubscribe to groups"
            print " 	n: list next 'N' discussion groups"
            print " 	q: exit from ag command\n"
            print "sg: lists 'N' subscribed groups\n"
            print "rg: displays status, time stamp, subject line of all posts in 'gname' 'N' at a time\n"
            print "		[id]: number between 1 & N denoting post within list of N posts to display\n"
            print "			n: display 'N' more lines\n"
            print "			q: quit displaying the post content\n"
            print "		r: marks post as read\n"
            print "		n: list the next 'N' posts\n"
            print "		p: post to group\n"
            print "		q: quit the rg command\n"
            print "logout: logs out current user and terminates the program\n"
        elif r[0] == 'ag':
            data = ag(r, clientSocket, data)
            clientSocket.close()
        elif r[0] == 'sg':
            data = sg(r, clientSocket, data)
        elif r[0] == 'rg':
            rg(r, clientSocket, data)
            clientSocket.close()
        elif r[0] == 'logout':
            
            clientSocket.close()
            sys.exit()
            i = 2
        else:
            print('Unsupported input, input help for available commands')
    print('loggingout')
main()


