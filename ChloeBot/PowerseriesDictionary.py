from itertools import chain, combinations
import sqlite3
def stats_used_in_gui(exactvalues, targetlistval, cursor1, tablename):
    PowerPee = find_dict_power_series(exactvalues)
    exactstring = ''
    countstuff = 0
    for y in exactvalues:
        if countstuff == 0:
            exactstring = exactstring + y + "=" +exactvalues[y]
        else:
            exactstring = exactstring + "," + y + "=" +exactvalues[y]
        countstuff = countstuff + 1
    targetvalues = []
    for x in targetlistval:
        currentdict = {}
        currentdict['Target'] = x
        targetvalues.append(currentdict)
    statsassignedlist = assign_statistics_to_list(PowerPee, targetvalues, cursor1, tablename)
    parsered = identify_possible_dependancies(statsassignedlist)
    printthis = find_optimal_combination(parsered)
    #print(printthis)
    #print(exactstring)
    returndict = calculate_probabilities(printthis, exactstring, targetlistval, cursor1, tablename)
    #print(returndict)
    return returndict
def string2calculate(string):
    numdem = string.split('/')
    num = float(numdem[0])
    dem = float(numdem[1])
    num = round(num, 6)
    dem = round(dem, 6)
    checkforzero = int(dem)
    if checkforzero == 0:#don't divide by zero
        dem = 1.000000
    fraction = num/dem
    fraction = round(fraction, 6)
    return fraction
def identifysinglets(list):
    returndictionary ={}
    for mem in list:
        conditionstoadd = ''
        if len(mem) == 2:
            for m in mem:
                if m != '__Statistics__':
                    conditiontoadd = m +"="+ mem[m]
            returndictionary[conditiontoadd] = mem['__Statistics__']
    return returndictionary
def identify_possible_dependancies(dictionarylist):#takes a list of dictionaries as an argument
    singlets = identifysinglets(dictionarylist)
    datatoparse =[]
    for x in dictionarylist:#Identify data that needs to be classified
        if len(x) > 2:
            datatoparse.append(x)
    dictionarycon = dict()
    dataID = 0
    for y in datatoparse:#iterate over dictionaries in list
        #print('placehold')
        #print(y)
        #dictionarycon = dict()
        statementlist = []

        for singlemember in y:#iterate over single dictionary
            dependancecheck = 1.0
            if '__Statistics__' not in singlemember:#evtract data to check
                fetchstatement = singlemember +'='+ y[singlemember]
                statementlist.append(fetchstatement)
        strint = ''
        maxcount = len(statementlist)
        count = 1
        for sx in statementlist:
            if count < maxcount:
                strint = strint + sx + ','
                count = count + 1
            else:
                strint = strint + sx
        dictionarycon[strint] = y['__Statistics__']
    #print(dictionarycon)
    independancestats = dict()
    for q in dictionarycon:
        #current = dict()
        #print(q)
        c = dictionarycon[q]
        for i in c:
            #print(i)
            independancestats[i] = 1.000000
        break

    for x in dictionarycon:
        #arrayconditions = []
        arrayconditions = x.split(',')
        #print(arrayconditions)
        for t in arrayconditions:
            #print(t)
            #print(singlets[t])
            currentstring = singlets[t]
            #print(currentstring)
            for c in currentstring:
                returnstrval = currentstring[c]
                returnfloatval = string2calculate(returnstrval)
                #print(independancestats)
                currentfloat = independancestats[c]
                writevalue = returnfloatval * currentfloat
                independancestats[c] = writevalue

        editsubdictionary = dictionarycon[x]#classify gains
        #print("****************************************************************")
        #print(editsubdictionary)
        #print("****************************************************************")
        neweditsubdictionary = editsubdictionary
        addtoeditdictionary = dict()
        for ent in editsubdictionary:
            stringval = editsubdictionary[ent]
            floatval = string2calculate(stringval)
            sudocorrelation = independancestats[ent]
            correlation = floatval - sudocorrelation
            newentryname = ent + "Correlation"
            addtoeditdictionary[newentryname] = correlation
        #print(addtoeditdictionary)
        for ent in addtoeditdictionary:
            editsubdictionary[ent] = addtoeditdictionary[ent]
    return dictionarycon
def order_dictionary_correlations(dictionary):
    correlationstart = dict()
    numberof = len(dictionary)
    for x in dictionary:
        extractthis = dictionary[x]
        for mem in extractthis:
            if 'Correlation' in mem:
                correlationstart[mem]
        break
def calculate_probabilities(highgainmember, allvalues, targetvalues, cursor, table):
    #initialize targets
    targetlist = []
    #########################
    listgainattributes = highgainmember.split(',')
    listallattributes = allvalues.split(',')
    missingmembers = []
    for mem in listallattributes:
        if mem not in listgainattributes:
            missingmembers.append(mem)
    gainlength = len(listgainattributes)
    combos = combinations(listallattributes, gainlength)
    #print(combos)
    listarrays = []
    for x in combos:
        currentlist = []
        for y in x:
            currentlist.append(y)
        listarrays.append(currentlist)
    dictionarymemberlist = []
    #print(listarrays)
    returnstatistics = {}
    liststatdic = []
    for list in listarrays:
        #print(list)
        notinlist = []
        for q in listallattributes:
            if q not in list:
                notinlist.append(q)
        selectstatement = "SELECT COUNT(*) FROM "+table+" WHERE "
        countinlist = 0
        lenlist = len(list)
        lenmaxindex = lenlist - 1
        for m in list:
            splitdata = m.split('=')
            if countinlist == 0:
                selectstatement = selectstatement + splitdata[0] + " = '" + splitdata[1] + "'"
            else:
                selectstatement = selectstatement + " and " + splitdata[0] + " = '" + splitdata[1] + "'"
            countinlist = countinlist + 1
        countmissing = 0
        for h in notinlist:
            spliter = h.split('=')
            selectstatement = selectstatement + " and " + spliter[0] + " != '" + spliter[1] + "'"
        totalcases = cursor.execute(selectstatement)
        newstatement = selectstatement + " and Target = '[REPLACE]'"
        dictionarytargets = {}
        for val in totalcases:
            for num in val:
                #print(num)
                dictionarytargets['Total'] = num
                #print(targetlist)
        for targi in targetvalues:
            target = newstatement.replace('[REPLACE]', targi)
            targicases = cursor.execute(target)
            for this in targicases:
                for extract in this:
                    dictionarytargets[targi] = extract
        #print(dictionarytargets)
        liststatdic.append(dictionarytargets)
        #print('printvals')
    intitialisereturndic ={}
    for d in liststatdic:
        for q in d:
            intitialisereturndic[q] = 0
        break
    for y in liststatdic:
        for b in y:
            intitialisereturndic[b] = intitialisereturndic[b] + y[b]
    #print(intitialisereturndic)
    return intitialisereturndic


    #return combos
#def find_maximum




def powertrucker(dictionary, targetvalues, cursor, tablename):
    usedtargetvalues = []
    dictionaryadditive = {}
    for value in targetvalues:
        currenttarget = {}
        trigger = ''
        for val in value:
            trigger = value[val]
            #print('triger ='+trigger)
        #print('tigger')
        currenttarget['Target'] = trigger
        currentstats = generatestatistics(dictionary, cursor, tablename, currenttarget)
        dicid = 'Target='+trigger
        dictionaryadditive[dicid] = currentstats
        del currenttarget
    returndiction = {}
    for condition in dictionary:
        returndiction[condition] = dictionary[condition]
    for c in dictionaryadditive:
        returndiction['__Statistics__'] = dictionaryadditive
    return returndiction
def assign_statistics_to_list(dictionarylist, targetvalues, cursor, tablename):
    dictionaryarray = []
    for di in dictionarylist:
        addtolist = powertrucker(di, targetvalues, cursor, tablename)
        dictionaryarray.append(addtolist)
    return dictionaryarray





'''
dictionarycondition = {}
dictionarycondition['Outlook'] = 'Sunny'
dictionarycondition['Tempurature'] = 'Mild'
dictionarycondition['Humidity'] = 'High'
dictionarycondition['Windy'] = 'yes'
'''
def generatestatistics(conditions, cursor, table, target):
    grabcasenumbertarget = "SELECT COUNT(*) FROM "+table+" WHERE "
    grabcasenumber = "SELECT COUNT(*) FROM " + table + " WHERE "
    originalconditions = conditions
    #print(conditions)
    #print(target)
    allconditions = conditions
    for x in target:
        allconditions[x] = target[x]
    count = 0
    for condition in allconditions:
        if count == 0:
            addstatement = "" +condition+ " = '" +allconditions[condition]+ "'"
        else:
            addstatement = " and "+condition+" = '" +allconditions[condition]+ "'"
        count = count + 1
        grabcasenumbertarget = grabcasenumbertarget + addstatement

    #print(grabcasenumbertarget)
    cc = cursor.execute(grabcasenumbertarget)
    casenumbertarget = 0
    for sd in cc:
        for x in sd:
            casenumbertarget = int(x)
    #print(casenumbertarget)
    count = 0
    del originalconditions['Target']
    for condition in originalconditions:
        if count == 0:
            addstatement = "" + condition + " = '" + originalconditions[condition] + "'"
        else:
            addstatement = " and " + condition + " = '" + originalconditions[condition] + "'"
        count = count + 1
        grabcasenumber = grabcasenumber + addstatement

    #print(grabcasenumber)
    oc = cursor.execute(grabcasenumber)
    casenumber = 0
    for mem in oc:
        for y in mem:
            casenumber = int(y)
    returnstring = str(casenumbertarget) + "/" + str(casenumber)
    return returnstring

def find_dict_power_series(dictionary):
    def power_set(input):
        # returns a list of all subsets of the list a
        if (len(input) == 0):
            return [[]]
        else:
            main_subset = []
            for small_subset in power_set(input[1:]):
                main_subset += [small_subset]
                main_subset += [[input[0]] + small_subset]
            return main_subset
    def list_to_dictionary(array, Allen):
        dictionaryreturn ={}
        for mem in array:
            dictionaryreturn[mem] = Allen[mem]
        return dictionaryreturn
    dictionarylist = []
    list = []
    arraycons = []
    for x in dictionary:
        dict = {}
        arraycons.append(x)
        dict[x] = dictionary[x]
        list.append(dict)
        del dict
    #print(list)
    #print(arraycons)
    powerB = power_set(arraycons)
    #print(powerB)
    returndict = []
    for member in powerB:
        ret = list_to_dictionary(member, dictionary)
        if len(ret) != 0:
            returndict.append(ret)
    return returndict
def find_optimal_combination(powerlist):
    #print(' ')
    currentmax = {}
    currentmax['length'] = 0
    currentmax['cases'] = 0
    currentmax['combination'] = 0
    for member in powerlist:
        listmemberbreak = member.split(',')
        memlen = len(listmemberbreak)
        currentcasenumber = currentmax['cases']
        q = powerlist[member]
        for sub in q:
            if 'Target' in sub and 'Correlation' not in sub:
                splitthis = q[sub]
                spdat = splitthis.split('/')
                currentcasenumber = spdat[1]
                currentcasenumber = int(currentcasenumber)
            break
        if memlen > currentmax['length'] and currentcasenumber > 0:
            currentmax['length'] = memlen
            currentmax['cases'] = currentcasenumber
            currentmax['combination'] = member
    returnvalue = currentmax['combination']
    return returnvalue

#PowerPee = find_dict_power_series(dictionarycondition)
#print(PowerPee)
'''
perhaps = {'Outlook': 'Sunny'}
perhapsyes = {'Target': 'Yes'}
perhapsno = {'Target': 'No'}
#re = generatestatistics(perhaps, 'ggg', perhapsyes)
conn = sqlite3.connect('C:\\Users\\12564\\Desktop\\GolfData.db')
cursor1 = conn.cursor()
cursor2 = conn.cursor()

#re = generatestatistics(perhaps, cursor1, 'GolfData', perhapsyes)
#print(re)
#print(perhaps)
#probabilitylist = []
#targetvalues = []
#targetvalues.append(perhapsyes)
#targetvalues.append(perhapsno)
#hi = powertrucker(PowerPee[0], targetvalues, cursor1, 'GolfData')
targetlistval = []
targetlistval.append('No')
targetlistval.append('Yes')
#statsassignedlist = assign_statistics_to_list(PowerPee, targetvalues, cursor1, 'GolfData')
#print('statsassignmen')
#print(statsassignedlist)
#shrink = identifysinglets(statsassignedlist)
#parsered = identify_possible_dependancies(statsassignedlist)
#print(parsered)
#teststr = '6/9'
#lisr = calculate_probabilities('Outlook=Sunny,Tempurature=Mild,Humidity=High', 'Outlook=Sunny,Tempurature=Mild,Humidity=High,Windy=yes', targetlistval, cursor1, 'GolfData')
#print(PowerPee)
#print(hi)
#print(parsered)
#printthis = find_optimal_combination(parsered)
#newprobs = calculate_probabilities(printthis, 'Outlook=Sunny,Tempurature=Mild,Humidity=High,Windy=yes', targetlistval, cursor1, 'GolfData')
#print(printthis)
#print(newprobs)
extactvals = {}
extactvals['Outlook'] = 'Sunny'
extactvals['Tempurature'] = 'Mild'
extactvals['Humidity'] = 'High'
extactvals['Windy'] = 'yes'
perky = stats_used_in_gui(extactvals, targetlistval, cursor1, 'GolfData')
print(perky)
conn.close()
'''