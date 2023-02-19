import re
import math
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

class User:

    def __init__(self, idade, sexo, tensao, colesterol, batimento, temDoenca):
        self.idade = idade
        self.sexo = sexo
        self.tensao = tensao
        self.colesterol = colesterol
        self.batimento = batimento
        self.temDoenca = temDoenca

    def createUser(input):
        params = re.split(",", input)
        #print(params)
        r = User(int(params[0]), params[1], int(params[2]), int(params[3]), int(params[4]), int(params[5][0]))
        return r

    def getIdade(self):
        return self.idade

    def getSex(self):
        return self.sexo
    
    def hasDoenca(self):
        return self.temDoenca

#Creating List

def calculaDoentes(dataBase):
    r = 0
    for x in dataBase:
        if (x.hasDoenca() == 1):
            r+=1
    return r

def doencaPorSexo(dataBase):
    doentesM = doentesF = 0
    for paciente in dataBase:
        a = paciente.hasDoenca()
        b = paciente.getSex()
        if (paciente.hasDoenca() == 1):

            if (b == 'M'):
                doentesM+=1
            elif (b == 'F'):
                doentesF+=1
    return float(doentesM/(doentesM+doentesF))

def tabelaSexo(malePercentage, totalSick):
    print("Doentes M - " + str(int(malePercentage * totalSick)))
    print("Doentes F - " + str(int(totalSick - (malePercentage * totalSick))))


def maxIdade(dataBase):
    r = 0
    for x in dataBase:
        if x.idade > r:
            r = x.idade
    return r

def tabelaIdade(inputList):
    print(" Idade  | Quantidade\n")
    n = 0
    while(n < len(inputList)):
        print(" " + str(30+n*5) + "-" + str(34+n*5) + "  |  " + str(inputList[n]))
        n+=1


def doencaPorIdade(dataBase):
    mi = maxIdade(dataBase)
    i = 0
    r = []
    while(i*5+30 <= mi):
        r.insert(i, 0)
        i+=1

    for paciente in dataBase:
        if(paciente.hasDoenca() == 1):
            index = math.floor((paciente.getIdade()-30)/5)
            r[index]+=1
    return r

def maxColesterol(dataBase):
    r = 0
    for x in dataBase:
        if x.colesterol > r:
            r = x.colesterol
    return r

def minColesterol(dataBase):
    r = 999999
    for x in dataBase:
        if x.colesterol < r:
            r = x.colesterol
    return r

def doencaPorColesterol(dataBase):
    max = maxColesterol(dataBase)
    min = minColesterol(dataBase)
    i = 0
    r = []
    while(i*10+min <= max):
        r.insert(i, 0)
        i+=1

    for paciente in dataBase:
        if(paciente.hasDoenca() == 1):
            index = math.floor((paciente.colesterol-min)/10)
            r[index]+=1
    return r

def tabelaColesterol(inputList):
    print(" Colesterol | Quantidade\n")
    n = 0
    while (n < len(inputList)):
        if(inputList[n] > 0):
            print(" " + str(10*n) + "-" + str(10*n+9) + " | " + str(inputList[n]))
        n+=1

myheart = open("C:/Users/longu/OneDrive/Documents/GitHub/PL2023/TPC1/myheart.csv", "r")
line_list = myheart.readlines()
n = 1
dataBase = []
while(n < line_list.__len__()):
    #print(line_list[n])
    new_User = User.createUser(line_list[n])
    dataBase.append(new_User)
    n+=1
myheart.close()


#List created
#Calculating queries
doentinhos = calculaDoentes(dataBase)

inputNo = 9

while(int(inputNo) >= 0):
    print("\n\n\n0 - Doenca por sexo")
    print("1 - Doenca por idade")
    print("2 - Doenca por colesterol")
    inputNo = int(input("Insira opcao:"))
    print("\n\n")
    if(inputNo == 0):
        tabelaSexo(doencaPorSexo(dataBase), doentinhos)
    elif(inputNo == 1):
        tabelaIdade(doencaPorIdade(dataBase))
    elif(inputNo == 2):
        tabelaColesterol(doencaPorColesterol(dataBase))

    