# TPC2
####Crie um programa em Python que tenha o seguinte comportamento:

####Pretende-se um programa que some todas as sequências de dígitos que encontre num texto;
####Prepare o programa para ler o texto do canal de entrada: stdin;
####Sempre que encontrar a string “Off” em qualquer combinação de maiúsculas e minúsculas, esse comportamento é desligado;
####Sempre que encontrar a string “On” em qualquer combinação de maiúsculas e minúsculas, esse comportamento é novamente ligado;
####Sempre que encontrar o caráter “=”, o resultado da soma é colocado na saída.

isOn = True
analyse = ''
n = 0
total = 0
while(n >= len(analyse) or analyse[n] != "="):
    if(n >= len(analyse)):
        n = 0
        analyse = input("")
    if(analyse[n] == "o" or analyse[n] == "O"):
        if(n+1 < len(analyse) and (analyse[n+1] == "n" or analyse[n+1] == "N")):
            isOn = True
            n+=1
        elif(n+2 < len(analyse) and(analyse[n+1] in "Ff" and analyse[n+2] in "Ff")):
            isOn = False
            n+=2
    elif(analyse[n].isdigit() and isOn == True):
        total+=int(analyse[n])
    n+=1
print("total = " + str(total))
