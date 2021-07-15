import os
from itertools import chain, combinations
import json
import sys
import xlrd
import json
import time
#import openpyxl
import xml.etree.ElementTree as ET
import xmltodict
import math
import sqlite3
from tkinter import filedialog
import tkinter as tk
import PowerseriesDictionary
class createfiledialog:
    def __init__(self):
        self.returnstring = ''
        self.rootstartmenu = tk.Tk()
        self.directory = filedialog.askdirectory()
        self.printtext = self.directory + '\\'
        self.printtext = self.printtext.replace('/', '\\')
        self.rootstartmenu.title(self.directory)
        self.framestartmenu = tk.Frame(self.rootstartmenu)
        tk.Label(self.framestartmenu, text=self.printtext).grid(row=0, column=0)
        self.file = tk.Entry(self.framestartmenu)
        self.file.grid(row=0, column=1)
        tk.Button(self.framestartmenu, text="Create database", command=self.create).grid(row=0, column=3)
        tk.Label(self.framestartmenu, text='.db').grid(row=0, column=2)
        self.framestartmenu.pack(pady=10, padx=10)
        tk.mainloop()
    def create(self):
        self.returnstring = self.directory + self.file.get()
        self.rootstartmenu.destroy()
class NewTrainingSet:
    def __init__(self):
        newfile = createfiledialog()
        filedirectory = newfile.returnstring
        self.masterroot = tk.Tk()
        self.masterframe = tk.Frame(self.masterroot)
class Function_File_Wrapper:
    def __init__(self, Object, filetypewithtext, titletext):
        self.tkObject = Object
        self.filetypewithtext = filetypewithtext
        self.titletext = titletext
    def WrapRunner():
        browseFiles(self.tkObject, self.filetypewithtext, self.titletext)
def browseFiles(ConfigerObject, filetypewithtext, titletext):
    filetype = ''
    filetext = ''
    
    for x in filetypewithtext:
        filetype = x
        filetext = filetypewithtext[x]
        break
    passingfiletype = "*."+filetype+"*"
    filename = filedialog.askopenfilename(initialdir="/", title=titletext, filetypes=(("Text files",
                                                      "*.json*"),
                                                     ("all files",
                                                      "*.db*")))
    # Change label contents
    ConfigerObject.configure(text="File Selected: " + filename)
class store:
    def __init__(self, value):
        self.value = value
currentdirectory = str(sys.argv[0])
def calculate_targets(dictionary, cursor, database):
    print('Grimaze')
removesubstr = currentdirectory.replace('\\KhloeBotDevelopment.py', '')
print(removesubstr)
removesubstrexe = removesubstr.replace('\\KhloeBotDevelopment.exe', '')
listdirectory = os.listdir(removesubstrexe)
currentdirectoryObj = store(removesubstrexe)
validdatabases = []
validtrees = []
possibledatasources = []
for member in listdirectory:
    if '.db' in member:
        jfile = member.replace('.db', '.json')
        #search json
        if jfile in listdirectory:
            validdatabases.append(member)
            validtrees.append(jfile)
    #find datasources
    elif '.xlsx' in member:
        possibledatasources.append(member)
datasourcesObj = store(possibledatasources)
validtreesObj = store(validtrees)
validdbObj = store(validdatabases)
#Bay#Bay#############################Bay###################Bay

################################################################
class updatedataprojectdirectory():
    def __init__(self):
        currentdirectory = str(sys.argv[0])
        removesubstr = currentdirectory.replace('\\KhloeBotDevelopment.py', '')
        print(removesubstr)
        removesubstrexe = removesubstr.replace('\\KhloeBotDevelopment.exe', '')
        listdirectory = os.listdir(removesubstrexe)
        currentdirectoryObj = store(removesubstrexe)
        validdatabases = []
        validtrees = []
        possibledatasources = []
        for member in listdirectory:
            if '.db' in member:
                jfile = member.replace('.db', '.json')
                # search json
                if jfile in listdirectory:
                    validdatabases.append(member)
                    validtrees.append(jfile)
            # find datasources
            elif '.xlsx' in member:
                possibledatasources.append(member)
        self.validdatabases = validdatabases
        self.validtrees = validtrees
        self.possibledatasources = possibledatasources
class ChloeBotStartmenu:
    def __init__(self):
        self.rootstartmenu = tk.Tk()
        dictions = {}
        dictions['json'] = 'json'
        self.text1 = tk.StringVar()
        self.text1.set('old')
        self.rootstartmenu.title("ChloeBot")
        self.framestartmenu = tk.Frame(self.rootstartmenu)
        Choices = {'Build decision tree.', 'Use Existing decision tree.'}
        self.framestartmenu.pack(pady = 10, padx = 40)
        tk.Label(self.framestartmenu, text="Select Option").grid(row = 0, column = 1)
        #editlabel = tk.Label(self.framestartmenu, text="changeval").grid(row = 4, column = 1)
        #Command2Browse = Function_File_Wrapper(editlabel, dictions, "Select")
        tk.Button(self.framestartmenu, text="Build decision tree", command=BuilddesisiontreeGui).grid(row = 1, column = 1)
        tk.Button(self.framestartmenu, text="Use existing decision tree", command=SelectexistingtreeGui).grid(row = 2, column = 1)
        #tk.Button(self.framestartmenu, textvariable=self.text1, command=self.opendata).grid(row = 3, column = 1)
        self.rootstartmenu.mainloop()
    def opendata(self):
        filename = filedialog.askopenfilename(initialdir="/", title="Select JSON tree", filetypes=(("Text files", "*.json*"), ("all files", "*.db*")))
        self.text1.set(filename)
        # Change label contents
        #self.editlabel.configure(text="File Selected: " + filename)
class SelectexistingtreeGui:
    def __init__(self):
        currentdirdata = updatedataprojectdirectory()
        self.root = tk.Tk()
        self.root.title("Select existing tree")
        print(currentdirdata.validtrees)
        self.treeselectmenu = tk.Frame(self.root)
        self.Choices = currentdirdata.validtrees
        self.treeselectmenu.pack(pady = 10, padx = 40)
        tk.Label(self.treeselectmenu, text="Select tree").grid(row = 0, column = 1)
        self.tkvar = tk.StringVar(self.root)
        try:
            self.popupMenu = tk.OptionMenu(self.treeselectmenu, self.tkvar, *self.Choices)
            self.popupMenu.grid(row = 1, column =1)
            tk.Button(self.treeselectmenu, text="Classify single datapoint", command=self.treedb).grid(row=2, column=1)
            tk.Button(self.treeselectmenu, text="Classify bulk data").grid(row=3, column=1)
        except:
            tk.Label(self.treeselectmenu, text="No valid data").grid(row = 1, column =1)

        self.root.mainloop()
    def treedb(self):
        jsonfile = self.tkvar.get()
        dbfile = jsonfile.replace('.json', '.db')
        print(dbfile)
        tablename = jsonfile.replace('.json', '')
        data = fetchtreeconditions(dbfile)
        database = currentdirectoryObj.value + '\\' + dbfile
        enternewdata = enterdata(data, database, tablename)
        print(data)
class findbulkdata:
    def __init__(self):
        self.root = tk.Tk()
def fetchtreeconditions(databasefile):
    databasetoopen = currentdirectoryObj.value + '\\' + databasefile
    basetablename = databasefile.replace('.db', '')

    grabbasename = "SELECT Node FROM "+basetablename+"Node"
    nodedictionary = {}
    print(databasetoopen)
    conn = sqlite3.connect(databasetoopen)
    cursor = conn.cursor()
    #grab nodes
    nodesql = cursor.execute(grabbasename)
    nodelist = []
    for entree in nodesql:
        print(entree)
        node = extractsingle(entree)
        print(node)
        nodelist.append(node)
    #grab nodemembers
    print(nodelist)
    for node in nodelist:
        selectmemberstatement = "SELECT NodeMember FROM "+basetablename+"NodeMemberData WHERE Node = '"+node+"'"
        membercursor = conn.cursor()
        sqlmembers = membercursor.execute(selectmemberstatement)
        members = []
        for mem in sqlmembers:
            member = extractsingle(mem)
            members.append(member)
        membercursor.close()
        nodedictionary[node] = members
    return nodedictionary
class enterdata:
    def __init__(self, dictionary, database, maintable):
        self.dictionary = dictionary
        self.database = database
        self.tablename = maintable
        self.dictionarylength = len(dictionary)
        self.root = tk.Tk()
        self.griddimentions = []
        #intitializing tkvariabales
        self.var1 = tk.StringVar(self.root)
        self.choice1 = []
        self.var2 = tk.StringVar(self.root)
        self.choice2 = []
        self.var3 = tk.StringVar(self.root)
        self.choice3 = []
        self.var4 = tk.StringVar(self.root)
        self.choice4 = []
        self.var5 = tk.StringVar(self.root)
        self.choice5 = []
        self.var6 = tk.StringVar(self.root)
        self.choice6 = []
        self.var7 = tk.StringVar(self.root)
        self.choice7 = []
        self.var8 = tk.StringVar(self.root)
        self.choice8 = []
        self.var9 = tk.StringVar(self.root)
        self.choice9 = []
        self.var10 = tk.StringVar(self.root)
        self.choice10 = []
        self.var11 = tk.StringVar(self.root)
        self.choice11 = []
        self.var12 = tk.StringVar(self.root)
        self.choice12 = []
        self.var13 = tk.StringVar(self.root)
        self.choice13 = []
        self.var14 = tk.StringVar(self.root)
        self.choice14 = []
        self.var15 = tk.StringVar(self.root)
        self.choice15 = []
        self.var16 = tk.StringVar(self.root)
        self.choice16 = []
        self.var17 = tk.StringVar(self.root)
        self.choice17 = []
        self.var18 = tk.StringVar(self.root)
        self.choice18 = []
        self.var19 = tk.StringVar(self.root)
        self.choice19 = []
        self.var20 = tk.StringVar(self.root)
        self.choice20 = []
        self.root.title("enter data to classify")
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady = 5, padx = 5)
        self.buildbuttons()
    def buildbuttons(self):
        count = 0
        self
        for node in self.dictionary:
            count = count + 1
            self.findvariable(count, node)
        submitdatabuttonrow = count + 1
        tk.Button(self.frame, text='Classify', command=self.builddictionary).grid(row=submitdatabuttonrow, column=0)
        self.count = count
    def findvariable(self, number, nobe):
        tk.Label(self.frame, text=nobe).grid(row = number, column = 0)
        if number == 1:
            self.label1 = nobe
            self.choice1 = self.dictionary[nobe]
            tk.OptionMenu(self.frame, self.var1, *self.choice1).grid(row = number, column = 1)
        elif number == 2:
            self.label2 = nobe
            self.choice2 = self.dictionary[nobe]
            tk.OptionMenu(self.frame, self.var2, *self.choice2).grid(row=number, column=1)
        elif number == 3:
            self.label3 = nobe
            self.choice3 = self.dictionary[nobe]
            tk.OptionMenu(self.frame, self.var3, *self.choice3).grid(row=number, column=1)
        elif number == 4:
            self.label4 = nobe
            self.choice4 = self.dictionary[nobe]
            tk.OptionMenu(self.frame, self.var4, *self.choice4).grid(row=number, column=1)
        elif number == 5:
            self.label5 = nobe
            self.choice5 = self.dictionary[nobe]
            tk.OptionMenu(self.frame, self.var5, *self.choice5).grid(row=number, column=1)
        elif number == 6:
            self.label6 = nobe
            self.choice6 = self.dictionary[nobe]
            tk.OptionMenu(self.frame, self.var6, *self.choice6).grid(row=number, column=1)
        elif number == 7:
            self.label7 = nobe
            self.choice7 = self.dictionary[nobe]
            tk.OptionMenu(self.frame, self.var7, *self.choice7).grid(row=number, column=1)
        elif number == 8:
            self.label8 = nobe
            self.choice8 = self.dictionary[nobe]
            tk.OptionMenu(self.frame, self.var8, *self.choice8).grid(row=number, column=1)
        elif number == 9:
            self.label9 = nobe
            self.choice9 = self.dictionary[nobe]
            tk.OptionMenu(self.frame, self.var9, *self.choice9).grid(row=number, column=1)
        elif number == 10:
            self.label10 = nobe
            self.choice10 = self.dictionary[nobe]
            tk.OptionMenu(self.frame, self.var10, *self.choice10).grid(row=number, column=1)
        elif number == 11:
            self.label11 = nobe
            self.choice11 = self.dictionary[nobe]
            tk.OptionMenu(self.frame, self.var11, *self.choice11).grid(row=number, column=1)
        elif number == 12:
            self.label12 = nobe
            self.choice12 = self.dictionary[nobe]
            tk.OptionMenu(self.frame, self.var12, *self.choice12).grid(row=number, column=1)
        elif number == 13:
            self.label13 = nobe
            self.choice13 = self.dictionary[nobe]
            tk.OptionMenu(self.frame, self.var13, *self.choice13).grid(row=number, column=1)
        elif number == 14:
            self.label14 = nobe
            self.choice14 = self.dictionary[nobe]
            tk.OptionMenu(self.frame, self.var14, *self.choice14).grid(row=number, column=1)
        elif number == 15:
            self.label15 = nobe
            self.choice15 = self.dictionary[nobe]
            tk.OptionMenu(self.frame, self.var15, *self.choice15).grid(row=number, column=1)
        elif number == 16:
            self.label16 = nobe
            self.choice16 = self.dictionary[nobe]
            tk.OptionMenu(self.frame, self.var16, *self.choice16).grid(row=number, column=1)
        elif number == 17:
            self.label17 = nobe
            self.choice17 = self.dictionary[nobe]
            tk.OptionMenu(self.frame, self.var17, *self.choice17).grid(row=number, column=1)
        elif number == 18:
            self.label18 = nobe
            self.choice18 = self.dictionary[nobe]
            tk.OptionMenu(self.frame, self.var18, *self.choice18).grid(row=number, column=1)
        elif number == 19:
            self.label19 = nobe
            self.choice19 = self.dictionary[nobe]
            tk.OptionMenu(self.frame, self.var19, *self.choice19).grid(row=number, column=1)
        elif number == 20:
            self.label20 = nobe
            self.choice20 = self.dictionary[nobe]
            tk.OptionMenu(self.frame, self.var20, *self.choice20).grid(row=number, column=1)
    def builddictionary(self):
        coutcount = self.count
        conditiondictionary = {}
        cout = 1
        while cout <= coutcount:
            if cout == 1:
                conditiondictionary[self.label1] = self.var1.get()
            elif cout == 2:
                conditiondictionary[self.label2] = self.var2.get()
            elif cout == 3:
                conditiondictionary[self.label3] = self.var3.get()
            elif cout == 4:
                conditiondictionary[self.label4] = self.var4.get()
            elif cout == 5:
                conditiondictionary[self.label5] = self.var5.get()
            elif cout == 6:
                conditiondictionary[self.label6] = self.var6.get()
            elif cout == 7:
                conditiondictionary[self.label7] = self.var7.get()
            elif cout == 8:
                conditiondictionary[self.label8] = self.var8.get()
            elif cout == 9:
                conditiondictionary[self.label9] = self.var9.get()
            elif cout == 10:
                conditiondictionary[self.label10] = self.var10.get()
            elif cout == 11:
                conditiondictionary[self.label11] = self.var11.get()
            elif cout == 12:
                conditiondictionary[self.label12] = self.var12.get()
            elif cout == 13:
                conditiondictionary[self.label13] = self.var13.ge()
            elif cout == 14:
                conditiondictionary[self.label14] = self.var14.get()
            elif cout == 15:
                conditiondictionary[self.label15] = self.var15.get()
            elif cout == 16:
                conditiondictionary[self.label16] = self.var16.get()
            elif cout == 17:
                conditiondictionary[self.label17] = self.var17.get()
            elif cout == 18:
                conditiondictionary[self.label18] = self.var18.get()
            elif cout == 19:
                conditiondictionary[self.label19] = self.var19.get()
            elif cout == 20:
                conditiondictionary[self.label20] = self.var20.get()
            cout = cout + 1
        self.outputdictionary = conditiondictionary
        self.dapoutit()
    def dapoutit(self):
        dapout(self.database, self.tablename, self.outputdictionary)
        print(self.outputdictionary)
    def submitdata(self):
        self.builddictionary(self)
        self.dapoutit(self)
class dapout:
    def __init__(self, database, tablename, dictionary):
        output = Deicider(database, tablename, dictionary)
        print('******************************')
        print(dictionary)
        print('******************************')
        cout = 1
        #outputstr = output['leaf']
        #result = getresult(output)
        self.root = tk.Tk()
        self.root.title('Assignment')
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10, padx=10)
        for x in dictionary:
            Nodename = str(x)
            assignment = dictionary[x]
            textassignment = Nodename + ' = ' + str(assignment)
            tk.Label(self.frame, text=textassignment).grid(row=cout, column=0)
            cout = cout + 1
        result = 'Outcome = '+output
        tk.Label(self.frame, text=result).grid(row = cout, column=0)
        self.root.mainloop()
class fetchingdat:
    def __init__(self, data, count, loadingstr8):
        self.root = tk.Tk()
        datastring = data.get()
        self.root.title(datastring)
        self.loadingstr = tk.StringVar()
        self.loading = tk.Frame(self.root)
        self.loading.pack(pady = 5, padx = 10)
        tk.Label(self.loading, text=loadingstr8).grid(row = 0, column = 0)
        self.loadingstr.set('hi')
        #time.sleep(4)
        #self.loadingends()
        self.root.mainloop()
        time.sleep(4)
        self.loadingends()
    def editlabel(self):
        self.loadingstr.set('new set')
    def loadingends(self):
        self.root.destroy()
class classifynewdata:
    def __init__(self):
        self.root = tk.Tk()
class BuilddesisiontreeGui:
    def __init__(self):
        root = tk.Tk()
        Choices = datasourcesObj.value
        root.title("Build decision tree")
        buildtreeGUI = tk.Frame(root)
        buildtreeGUI.pack(pady = 10, padx = 40)
        tk.Label(buildtreeGUI, text="Select Data").grid(row = 0, column = 1)
        self.tkvar = tk.StringVar(root)
        popupMenu = tk.OptionMenu(buildtreeGUI, self.tkvar, *Choices).grid(row = 1, column = 1)
        tk.Button(buildtreeGUI, text="Use selected tree", command=self.buildtreefromdata).grid(row = 2, column =1)
    def buildtreefromdata(self):
        dir = currentdirectoryObj.value
        execldatfile = self.tkvar.get()
        execldat = dir +'\\'+ execldatfile
        dabase = execldat.replace('.xlsx', '.db')
        maintable = execldatfile.replace('.xlsx', '')
        builddata = convertXL2DBF(execldat, dabase, maintable)
        builddata.ProcessNodes(maintable)
        builddata.BuildDesisionTree(maintable)
        #update = updatedata()updatedataprojectdirectory
        print('Build')
def convertxml2json(xfile):
    with open(xfile) as xml_file:
        data_dict = xmltodict.parse(xml_file.read())
    xml_file.close()
    #print(data_dict)
    json_data = json.dumps(data_dict)
    #print(json_data)
    jfile = xfile.replace('.xml', '.json')
    with open(jfile, "w") as jeff:
        jeff.write(json_data)
    return jfile
def conditionentropy(NodeConditions, tablename, database):
    conlen = len(NodeConditions)
    statement = ""
    if conlen == 0:
        statement = "SELECT Target FROM "+tablename
    else:
        statement = "SELECT Target FROM "+tablename+ " WHERE "
        countnodes = 0
        for node in NodeConditions:
            countnodes = countnodes + 1
            if countnodes < conlen:
                statement = statement + node + " = '" + NodeConditions[node] + "' AND "
            else:
                statement = statement + node + " = '" + NodeConditions[node] + "'"
    #statement has been generated
    conn = sqlite3.connect(database)
    cursor1 = conn.cursor()
    print(statement)
    currentdata = cursor1.execute(statement)
    bester = {}
    bester['Yes'] = 0
    bester['No'] = 0
    for x in currentdata:
        y = extractsingle(x)
        if y == 'Yes':
            bester['Yes'] = bester['Yes'] + 1
        elif y == 'No':
            bester['No'] = bester['No'] + 1
    yescount = bester['Yes']
    nocount = bester['No']
    entropy = entropyID3(yescount, nocount)
    conn.close()
    return entropy
def processLoopNode(NodeConditions, tablename, database, xmldataObj, Usednodelist):
    inheritednodes = Usednodelist
    for this in NodeConditions:
        if this not in Usednodelist:
            del NodeConditions[this]
    currententropy = conditionentropy(NodeConditions, tablename, database)
    #findalready assigned nodes
    assignednodes = []
    for node in NodeConditions:
        assignednodes.append(node)
    #get all nodes
    conn = sqlite3.connect(database)
    curse = conn.cursor()
    statement = "SELECT Node FROM "+tablename+"Node"
    allnodes = curse.execute(statement)
    listallnodes = []
    for nod in allnodes:
        cain = extractsingle(nod)
        listallnodes.append(cain)
    #all nodes fetched
    #find nodes to parse through
    nodestoparse = []
    for node in listallnodes:
        if node not in assignednodes:
            nodestoparse.append(node)
    #find gain for valid nodes
    gaindictionary = {}
    for n in nodestoparse:
        nodeentrop = conditionalnodeentropy(NodeConditions, n, tablename, database)
        gain = currententropy - nodeentrop
        gaindictionary[n] = gain
    #identify optimalnode
    optimalnode = findmaxgain(gaindictionary)
    inheritednodes.append(optimalnode)
    #getmembers of optimal node
    Selectoptimum = "SELECT NodeMember FROM "+tablename+"NodeMemberData WHERE Node = '"+optimalnode+"'"
    members = curse.execute(Selectoptimum)
    memepar = []
    for m in members:
        gail = extractsingle(m)
        memepar.append(gail)
    #add element to tree
    cc = ET.SubElement(xmldataObj, optimalnode)
    #next step processnodemembers
    for x in memepar:
        newdata = NodeConditions
        newdata[optimalnode] = x
        processLoopNodeMember(newdata, tablename, database, cc, x, inheritednodes)
        del newdata
def processLoopNodeMember(NodeConditions, tablename, database, xmldataObj, cmember, usednodes):
    #find outcome of Memberdatainsert
    memObj = ET.SubElement(xmldataObj, cmember)
    currentstatistics = condictiongeneratestatistics(NodeConditions, tablename, database)
    current = ''
    f = ''
    for x in NodeConditions:
        if NodeConditions[x] == cmember:
            current = x
    if currentstatistics['Yes'] > 0 and currentstatistics['No'] == 0:
        leafnote = ET.SubElement(memObj, 'leaf')
        leafnote.text = 'Yes'
        del NodeConditions[current]
    elif currentstatistics['Yes'] == 0 and currentstatistics['No'] > 0:
        leafnote = ET.SubElement(memObj, 'leaf')
        leafnote.text = 'No'
        del NodeConditions[current]
    elif currentstatistics['Yes'] == 0 and currentstatistics['No'] == 0:
        leafnote = ET.SubElement(memObj, 'Bae')
        for h in NodeConditions:
            note = ET.SubElement(leafnote, h)
            note.text = NodeConditions[h]
        del NodeConditions[current]
    else:
        processLoopNode(NodeConditions, tablename, database, memObj, usednodes)
        
        
def condictiongeneratestatistics(dictionary, tablename, database):
    dictlen = len(dictionary)
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    selectstatement = "SELECT Target FROM " +tablename + " WHERE " 
    count = 1
    for x in dictionary:
        if count != dictlen:
            selectstatement = selectstatement + x + " = '" + dictionary[x] + "' AND "
            count = count + 1
        else:
            selectstatement = selectstatement + x + " = '" + dictionary[x] + "'"
    print(selectstatement)
    data = cursor.execute(selectstatement)
    yescount = 0
    nocount = 0
    for y in data:
        extract = extractsingle(y)
        if extract == 'Yes':
            yescount = yescount + 1
        elif extract == 'No':
            nocount = nocount + 1
    returndictionary = {}
    conn.close()
    returndictionary['Yes'] = yescount
    returndictionary['No'] = nocount
    returndictionary['statement'] = selectstatement
    conn.close()
    return returndictionary
def conditionalnodeentropy(givenconditions, nodeofinterest, tablename, database):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    conlen = len(givenconditions)
    selectstatement = "SELECT " + nodeofinterest + ", Target FROM " +tablename + " WHERE " 
    count = 1
    if conlen == 0:
        selectstatement = "SELECT " + nodeofinterest + ", Target FROM " +tablename
    else:
        for x in givenconditions:
            if count != conlen:
                selectstatement = selectstatement + x + " = '" + givenconditions[x] + "' AND "
                count = count + 1
            else:
                selectstatement = selectstatement + x + " = '" + givenconditions[x] + "'"
    print(selectstatement)
    data = cursor.execute(selectstatement)
    memberdictionary ={}
    
    assignedmemberarray = []
    
    for k in data:
        indexer = 0
        currentmem = ''
        for y in k:
            #currentmem = ''
            if indexer == 0:
                if y not in assignedmemberarray:
                    assignedmemberarray.append(y)
                    initializedic = {}
                    initializedic['Yes'] = 0
                    initializedic['No'] = 0
                    memberdictionary[y] = initializedic
                indexer = indexer + 1
                currentmem = y
            else:
                fetch = memberdictionary[currentmem]
                fetch[y] = fetch[y] + 1
    currenttotal = 0
    numerator = 0
    for m in memberdictionary:
        current = memberdictionary[m]
        yescount = current['Yes']
        nocount = current['No']
        memtot = yescount + nocount
        currenttotal = currenttotal + memtot
        ents = entropyID3(yescount, nocount)
        numerator = numerator + memtot * ents
    
    totalentrop = numerator/currenttotal
    conn.close()
    return totalentrop
#def growtree(treedictionary, databasefile, tablename, nodescovered):
#    #for
def findmaxgain(dictionary):
    maxgain = 0.0
    maxgainnode = ''
    for node in dictionary:
        if dictionary[node] > maxgain:
            maxgain = dictionary[node]
            maxgainnode = node
    return maxgainnode
    
def extractsingle(this):
    for x in this:
        return x
def yesprobability(Yes, No):
    Total = float(Yes) + float(No)
    YesProbability = float(Yes/Total)
    NoProbability = float(No/Total)
    return YesProbability
def entropyID3(Yes, No):
    Total = float(Yes) + float(No)
    YesProbability = float(Yes/Total)
    NoProbability = float(No/Total)
    probabilitylist = [YesProbability, NoProbability]
    #print(probabilitylist)
    returnvalue = 0
    for value in probabilitylist:
        if value > 0.0:
            newvalue = (-1.0) * value * math.log2(value)
        else:
            newvalue = value
        returnvalue = returnvalue + newvalue
    return returnvalue
def calculateNodeEntropy(database, tablename, node, total, totalentropy):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    c2 = conn.cursor()
    countcases = 0
    statement = "SELECT * FROM "+tablename
    statementque = []
    del statement
    statement = "SELECT "+node+" FROM "+tablename
    nodemembers = []
    memberdictionary = {}
    print(statement)
    #print(c.execute(statement))
    firstquery = c.execute(statement)
    for y in firstquery:
        print (y)
        h = extractsingle(y)
        print (h)
        if h not in nodemembers:
            nodemembers.append(h)
            #memberdictionary[h] = {}
            temstatement = "SELECT Target FROM "+tablename+" WHERE "+node+ " = '" + h + "'"
            yescount = 0
            nocount = 0
            #start new connection
            trythis = c2.execute(temstatement)
            for s in trythis:
                #membercount = membercount + 1
                rawstring = extractsingle(s)
                if rawstring == 'Yes':
                    yescount = yescount + 1
                else:
                    nocount = nocount + 1
            mem = {}
            mem['Yes'] = yescount
            mem['No'] = nocount
            memberdictionary[h] = mem
            membercount = yescount + nocount
            memprob = float(membercount/total)
            memberentropy = entropyID3(yescount, nocount)
            #Add member data
            Memberdatainsert = "INSERT INTO "+tablename+"NodeMemberData VALUES ('"+node+"','"+str(h)+"',"+str(memprob)+","+str(memberentropy)+","+str(yescount)+","+str(nocount)+")"
            print(Memberdatainsert)
            statementque.append(Memberdatainsert)
            #c.execute(Memberdatainsert)
            continue
        else:
            print (h)
            continue
    for direction in statementque:
        c.execute(direction)
    currentnodeentropy = 0.0
    for m in nodemembers:
        currentstatement = "select NodeMemberProbability, NodeMemberEntropy from "+tablename+"NodeMemberData where Node = '"+node+"' and NodeMember = '"+m+"'"
        kl = c.execute(currentstatement)
        currentarray = []
        for la in kl:
            currentarray = []
            #currentarray.append(la)
            print(la)
            for a in la:
                currentarray.append(a)
                print(a)
            currentnodeentropy = currentnodeentropy + currentarray[0]*currentarray[1]
    #Enter entropy intodatabase
    nodegain = totalentropy - currentnodeentropy
    statement = "INSERT INTO "+tablename+"Node VALUES('"+node+"',"+str(currentnodeentropy)+","+str(nodegain)+")"
    c.execute(statement)
    conn.commit()
def findXLDataType (integernum):
    returnvalue = 'empty'
    if integernum == 0:
        returnvalue = 'empty'
    elif integernum == 1:
        returnvalue = 'text'
    elif integernum == 2:
        returnvalue = 'num'
    elif integernum == 3:
        returnvalue = 'text'
    elif integernum == 4:
        returnvalue = 'boolean'
    elif integernum == 5:
        returnvalue = 'error'
    elif integernum == 6:
        returnvalue = 'blank'
    return returnvalue
def findoptimalnode (priorconditions, tablename, database):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    conlen = len(givenconditions)
    assignednodes = []
    for nodename in priorconditions:
        assignednodes.append(nodename)
    statement = "SELECT Node FROM "+tablename+"Node"
    nodesrun = []
    outque = cursor.execute(statement)
    for x in outque:
        y = extractsingle(x)
        if y not in assignednodes:
            nodesrun.append(y)
            
    noderundictionary = {}
    for namednode in nodesrun:
        nodeentropy = conditionalnodeentropy(givenconditions, namednode, tablename, database)
        noderundictionary[namednode] = nodeentropy
    returnvalue = noderundictionary
    return returnvalue        
        
    #print(selectstatement)
#def generateNodeData (dbfile):
class convertXL2DBF:
    def __init__ (self, xlfile, dbfile, tablename):
        dictionarydatatypes = {}
        data = xlrd.open_workbook(xlfile)
        currentsheet = data.sheet_by_index(0)
        datanames = currentsheet.row_values(0)
        datapointlist = currentsheet.col_values(0)
        maxindexcolumn = len(datapointlist) - 1
    
        filewriter = r"[REPLACE]"
        filewriter = filewriter.replace('[REPLACE]', dbfile)
        #create db file
        conn = sqlite3.connect(dbfile)
        c = conn.cursor()
        #generate command string to create table
        runstring = 'CREATE TABLE ' + tablename + '('
        counter = 0
        datalength = len(datanames) - 1
        nodelistlength = datalength - 1
        NodesDictionary = {}
        #handling datatypes
        while(counter <= datalength):
            print(counter)
            if (counter < datalength):
                currentnode = currentsheet.cell_value(counter, 0)
                currentnodevalues = currentsheet.col_values(counter)
                currentnodename = datanames[counter]
                currentnodevalues.pop(0)
                members = []
                for x in currentnodevalues:
                    if x not in members:
                        members.append(x)
                
                NodesDictionary[currentnodename] = members
                type = currentsheet.cell(counter, 1).ctype
                typeassignment = findXLDataType(type)
                runstring = runstring + datanames[counter] + ' ' + typeassignment + ', '
            elif (counter == datalength):
                type = currentsheet.cell(counter, 1).ctype
                typeassignment = findXLDataType(type)
                runstring = runstring + datanames[counter] + ' ' + typeassignment + ')'
            counter = counter + 1
        print(runstring)
        c.execute(runstring)
        tablenodesdictionary = {}
        tablenodesdictionary[tablename] = NodesDictionary
        self.tablenodedictionary = tablenodesdictionary
        #enterdatapoints
        datastartind = 1
        while (datastartind <= maxindexcolumn):
            currentrunstring = "INSERT INTO " + tablename + " VALUES ("
            counter = 0
            while (counter <= datalength):
                print(counter)
                currentdata = currentsheet.cell_value(datastartind, counter)
                if (counter == datalength):
                    currentrunstring = currentrunstring + "'" + str(currentdata) + "')"
                else:
                    currentrunstring = currentrunstring + "'" + str(currentdata) + "',"
                counter = counter + 1
            datastartind = datastartind + 1
            print (currentrunstring)
            c.execute(currentrunstring)
                
                
        #sheet.col_values(0)
        writestatement = 'SELECT Target FROM ' + tablename
        #countdatapoints = 0
        yescount = 0
        nocount = 0
        for x in c.execute(writestatement):
            currentvalue = extractsingle(x)
            if currentvalue == 'Yes':
                yescount = yescount + 1
            else:
                nocount = nocount + 1
               
            #countdatapoints = countdatapoints + 1
            print (x)
        tabledata = {}
        rawdict = {}
        countdatapoints = yescount + nocount
        rawdict['Yes'] = yescount
        rawdict['No'] = nocount
        rawdict['Total'] = countdatapoints
        rawdict['Entropy'] = entropyID3(yescount, nocount)
        rawdict['YesProbability'] = float(yescount)/float(nocount)
        rawdict['NoProbability'] = float(nocount)/float(yescount)
        tabledata[tablename] = rawdict
        self.tabledata = tabledata
        conn.commit()
        conn.close()
        self.tablenames = []
        appendthis = self.tablenames.append(tablename)
        datanames.remove('Target')
        diction = {}
        diction[tablename] = datanames
        self.datapoints = countdatapoints
        self.dbfile = dbfile
        self.tablenames = appendthis
        self.nodelistdictionary = diction
    def ProcessNodes(self, tablename):
        nodes = self.nodelistdictionary[tablename]
        conn = sqlite3.connect(self.dbfile)
        c = conn.cursor()
        #GenerateNodeMemberData
        NodeMemberData = "CREATE TABLE " + tablename + "NodeMemberData (Node text, NodeMember text, NodeMemberProbability real, NodeMemberEntropy real, yescount real, nocount real)"
        c.execute(NodeMemberData)
        for node in nodes:
            for member in node:
                statement = "SELECT * FROM " +tablename+ " WHERE Target = 'Yes' AND "+str(node)+ " = '" + str(member) + "'"
                countyes = 0
                for x in c.execute(statement):
                    countyes = countyes + 1
                statement = "SELECT * FROM " +tablename+ " WHERE Target = 'Yes' AND "+str(node)+ " = '" + str(member) + "'"
                countno = 0
                for y in c.execute(statement):
                    countno = countno + 1
        NodeEntropy = "CREATE TABLE " +tablename + "Node (Node text, NodeEntropy real, Gain real)"
        c.execute(NodeEntropy)
        for node in nodes:
            Select = "SELECT Target FROM " + tablename + " where "
        for node in nodes:
            print(node)
            firststatement = "SELECT "+str(node)+" FROM "+tablename
            state = c.execute(firststatement)
            for x in state:
                for y in x:
                    print(str(y))
        fetch = self.nodelistdictionary
        tabledata = self.tabledata[tablename]
        tableentropy = tabledata['Entropy']
        currenttable = fetch[tablename]
        for c in currenttable:
            calculateNodeEntropy(self.dbfile, tablename, c, self.datapoints, tableentropy)
    def BuildDesisionTree(self, tablename):
        NodeConditons = {}
        UsedNodes = []
        #ET.set('version', '1.0')
        data = ET.Element('Tree')
        database = self.dbfile
        #givedatabase = ET.SubElement(data, 'Database')
        #givedatabase.text = self.dbfile
        processLoopNode(NodeConditons, tablename, self.dbfile, data, UsedNodes)
        b_xml = ET.tostring(data)
        thisthing = str(b_xml)
        tree_xml = thisthing[2:-1]
        #print(str(b_xml))
        formating = "<?xml version='1.0' encoding='UTF-8' standalone='yes'?>\n"
        tree_xml = formating + tree_xml
        newfile = self.dbfile
        newfile = newfile.replace('.db', '.xml')
        with open(newfile, "w") as f:
            f.write(tree_xml)
            f.close()
        self.json = convertxml2json(newfile)
def Deicider(database, tablename, data):
    jfile = database.replace('.db', '.json')
    jadedump = {}
    print(jfile)
    with open(jfile) as json_file:
        jadump = json.load(json_file)
        jadedump = jadump
    conec = sqlite3.connect(database)
    curry = conec.cursor()
    print(jadedump)
    #get nodes
    selectnodes = "SELECT Node FROM " +tablename+ "Node"
    nodes = curry.execute(selectnodes)
    listnodes = []
    jade = jadedump['Tree']
    tree = jade
    for single in nodes:
        dataextract = extractsingle(single)
        listnodes.append(dataextract)
    #conec.close()
    print('nodes')
    print(listnodes)
    #interact with desision tree
    fetch = ""
    print('fetching'+str(fetch))
    print(tree)
    print(data)
    for g in tree:
        fetch = g
    while fetch in listnodes:
        tree = tree[fetch]
        fetchmember = data[fetch]
        tree = tree[fetchmember]
        print(tree)
        for n in tree:
            print(n)
            fetch = n
            print(fetch)
    outcome = tree[fetch]
    print(fetch)
    #get targetvalues
    first = "SELECT Target FROM " + tablename
    firsttargetget = curry.execute(first)
    targetvaluelist = []
    for u in firsttargetget:
        firsty = extractsingle(u)
        targetvaluelist.append(firsty)
        break
    nthselectstatement = "SELECT Target FROM " + tablename + " WHERE"
    nthcountstatement = "SELECT COUNT(*) FROM " + tablename + " WHERE"
    ncount = 0
    zeroexitcondition = 1
    if fetch == 'Bae':
        first = "SELECT Target FROM " + tablename
        firsttargetget = curry.execute(first)
        targetvaluelist = []
        for u in firsttargetget:
            firsty = extractsingle(u)
            targetvaluelist.append(firsty)
            break
        nthselectstatement = "SELECT Target FROM " + tablename + " WHERE"
        nthcountstatement = "SELECT COUNT(*) FROM " + tablename + " WHERE"
        ncount = 0
        zeroexitcondition = 1
        while zeroexitcondition != 0:
            currenttarget = targetvaluelist[ncount]
            if ncount == 0:
                nthselectstatement = nthselectstatement + " Target != '" + currenttarget + "'"
                nthcountstatement = nthcountstatement + " Target != '" + currenttarget + "'"
            else:
                nthselectstatement = nthselectstatement + " and Target != '" + currenttarget + "'"
                nthcountstatement = nthcountstatement + " and Target != '" + currenttarget + "'"
            print(nthselectstatement)
            ncount = ncount + 1
            currentselect = curry.execute(nthselectstatement)
            print(nthselectstatement)
            for y in currentselect:
                nthy = extractsingle(y)
                print(y)
                print(nthy)
                targetvaluelist.append(nthy)
                break
            currentcount = curry.execute(nthcountstatement)
            for c in currentcount:
                cathy = extractsingle(c)
                zeroexitcondition = cathy
                break
        grabthis = PowerseriesDictionary.stats_used_in_gui(data, targetvaluelist, curry, tablename)
        print(grabthis)
        total = grabthis['Total']
        total = float(total)
        probabilitydiction = {}
        for grab in grabthis:
            if grab != 'Total':
                grabbed = grabthis[grab]
                grabbed = float(grabbed)
                newvalue = grabbed/total
                probabilitydiction[grab] = newvalue
        #findmaximum
        currentmaxprob = 0.0
        tiestatus = ''
        currentmaxtarget = ''
        tielist = []
        for g in probabilitydiction:
            curval = probabilitydiction[g]
            if curval > currentmaxprob:
                currentmaxprob = curval
                currentmaxtarget = g
                tielist.append(g)
                tiestatus = ''
            elif curval == currentmaxprob:
                tiestatus = 'yes'
                tielist.append(g)
        probpercet = currentmaxprob * 100
        strpercent = str(probpercet)
        if tiestatus != 'yes':
            outcome = currentmaxtarget + ' (' + strpercent + ' percent certainty)'
        else:
            outcome = 'Uncertain, '
            arraylen = len(tielist)
            couty = 0
            maxi = arraylen - 1
            while couty <= maxi:
                curt = tielist[couty]
                if couty == 0:
                    outcome = outcome + curt
                elif couty == 1 and arraylen == 2:
                    outcome = outcome + ' and ' + curt
                elif couty > 0 and couty < maxi:
                    outcome = outcome + ', ' + curt
                elif couty == maxi:
                    outcome = outcome + ', and ' + curt
                couty = couty + 1
            outcome = outcome + ' are equally probable.'
    print(outcome)
    return outcome
def getresult(dictionarystr):
    result = ''
    dictionary = json.loads(dictionarystr)
    you = dictionary['leaf']
    print(you)
    for n in dictionary:
        if n == 'leaf':
            result = dictionary['leaf']
        else:
            result = 'ask'
    return result

ChloeBotStartmenu()
#{'race': 'birdman', 'class': 'rogue', 'alignment': 'CG', 'background': 'artisan', 'gender': 'male'}