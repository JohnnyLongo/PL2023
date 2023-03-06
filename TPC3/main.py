#Construa agora um ou vários programas Python para processar o texto 'processos.txt' (procurar o ficheiro no Bb) com o intuito de calcular frequências de alguns elementos 
#(a ideia é utilizar arrays associativos, dicionários em Python, para o efeito) conforme solicitado a seguir:

#a) Calcula a frequência de processos por ano (primeiro elemento da data);
#b) Calcula a frequência de nomes próprios (o primeiro em cada nome) e apelidos (o ultimo em cada nome) por séculos e apresenta os 5 mais usados;
#c) Calcula a frequência dos vários tipos de relação: irmão, sobrinho, etc.;
#d) Converta os 20 primeiros registos num novo ficheiro de output mas em formato Json.

import re
import math
import datetime
import json

class Process:
    def __init__(self, processID, date, name1, name2, name3, rest):
        self.processID = processID
        self.date = date
        self.name1 = name1
        self.name2 = name2
        self.name3 = name3
        self.rest = rest
    
    def createProcess(input):
        params = re.split("::", input)
        if(len(params) != 7):
            return None
        date = re.split("-", params[1])
        dt = datetime.datetime(int(date[0]), int(date[1]), int(date[2]))
        r = Process(int(params[0]), dt, params[2], params[3], params[4], params[5])
        return r
    
    def toJSON(self):
        r = self
        r.date = r.date.strftime("%x")
        return json.dumps(r, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
    
processes = open("C:/Users/longu/OneDrive/Documents/GitHub/PL2023/TPC3/processos.txt", "r")
line_list = processes.readlines()
n = 1
dataBase = {}
while(n < line_list.__len__()):
    #print(line_list[n])
    new_process = Process.createProcess(line_list[n])
    if(new_process != None):        #invalid line check
        dataBase[n] = new_process
    n+=1
processes.close()
#print(dataBase)


# funcoes


def ex1(dataBase):
    values = {}
    for key in dataBase:
        value = dataBase.get(key)
        y = value.date.year
        if not y in values.keys():
            values[y] = 0
        values.update({y: values.get(y) + 1})
    years = list(values.keys())
    years.sort()
    for year in years:
        print(year, " | ",  values.get(year))

def ex2(dataBase):
    year = 1600
    
    while year < 2000:    
        print(year, "s : \n")
        nomes = {}
        apelidos = {}

        for key in dataBase:
            if(dataBase.get(key).date.year >= year and dataBase.get(key).date.year < year+100):
                value = dataBase.get(key).name1
                names = re.split(" ", value)
                if not names[0] in nomes.keys():
                    nomes[names[0]] = 0
                nomes.update({names[0]: nomes.get(names[0]) + 1})
                apelido = names[len(names) - 1]
                if not apelido in apelidos.keys():
                   apelidos[apelido] = 0
                apelidos.update({apelido: apelidos.get(apelido) + 1})
    
        modasNP = list(nomes.values())
        modasNP.sort()
        i = 1
        print("Nomes Proprios:")
        while i < 6 and i <= len(modasNP):
            n = str(list(nomes.keys())[list(nomes.values()).index(modasNP[len(modasNP)-i])])    #roubado ao StackOverflow
            print(i, " - ", n, modasNP[len(modasNP)-i])
            i+=1
            modasAP = list(apelidos.values())
            modasAP.sort()
        i = 1
        print("\nApelidos:")
        l = list(apelidos.keys())
        a = list(apelidos.values())
        while i < 6 and i <= len(modasAP):
            n = str(l[a.index(modasAP[len(modasAP)-i])])    #também roubado ao StackOverflow
            print(i, " - ", n, modasAP[len(modasAP)-i])
            i+=1
        year += 100
    
def ex3(dataBase):
    relaNO = {}
    for key in dataBase:
        value = dataBase.get(key)
        rest =re.split(",", value.rest)
        i = 1
        while i < len(rest):
            elem = rest[i]
            elem = re.split("\.", elem, 1)
            if len(elem) > 1 and re.search("Proc.", elem[1]) != None:
                if not elem[0] in relaNO.keys():
                    relaNO[elem[0]] = 0
                relaNO.update({elem[0]: relaNO.get(elem[0]) + 1})
            i+=1
    
    for key in relaNO:
        print(key, " | ", relaNO.get(key))

def ex4(dataBase): 
    i = 1
    f = open("C:/Users/longu/OneDrive/Documents/GitHub/PL2023/TPC3/output.json", "w")
    while i <= 20:
        i+=1
        print(dataBase.get(i))
        json.dump(dataBase.get(i).toJSON(), f)
    f.close()



#menu

opt = 99

while (int (opt) >= 0):
    opt = input("\nEscreve o no. da alinea que queres executar\n")
    if(int (opt) == 1):
        ex1(dataBase)
    elif(int (opt) == 2):
        ex2(dataBase)
    elif(int (opt) == 3):
        ex3(dataBase)
    elif(int (opt) == 4):
        ex4(dataBase)


