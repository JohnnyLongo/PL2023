import re
import math

levantado = False
saldo = 0
while(True):
    input_command = input("")
    if(re.match("LEVANTAR", input_command)):
        levantado = True
    elif(re.match("POUSAR", input_command)):
        levantado = False

        moedas2e = math.floor(saldo/200)
        saldo -=moedas2e*200
        moedas1e = math.floor(saldo/100)
        saldo -=moedas1e*100
        moedas50c = math.floor(saldo/50)
        saldo -=moedas50c*50
        moedas20c = math.floor(saldo/20)
        saldo -=moedas20c*20
        moedas10c = math.floor(saldo/10)
        saldo -=moedas10c*10
        moedas5c = math.floor(saldo/5)
        saldo -=moedas5c*5
        moedas2c = math.floor(saldo/2)
        saldo -=moedas2c*2
        moedas1c = saldo
        saldo -= saldo

        string = "moedas - "
        if(moedas2e != 0):
            string = string + str(moedas2e) + "x2e " 
        if(moedas1e != 0):
            string = string + str(moedas1e) + "x1e "
        if(moedas50c != 0):
            string = string + str(moedas50c) + "x50c "
        if(moedas20c != 0):
            string = string + str(moedas20c) + "x20c "
        if(moedas10c != 0):
            string = string + str(moedas10c) + "x10c "
        if(moedas5c != 0):
            string = string + str(moedas5c) + "x5c "
        if(moedas2c != 0):
            string = string + str(moedas2c) + "x2c "
        if(moedas1c != 0):
            string = string + str(moedas1c) + "x1c"
        
        print(string)
        
        
        
    elif(re.match("T=[0-9]+", input_command) and levantado == True):
        number = re.split("=", input_command, 0)[1]
        if(not re.match("00", number)):
            if(len(number) != 9):
                print("numero invalido")
        elif(saldo < 150):
            print("saldo insuficiente")
        else:
            saldo-=150

        if(re.match("601|641", number)):
            print("chamada bloqueada")
        
        if(re.match("2", number)):
            if(saldo < 25):
                print("saldo insuficiente")
            else:
                saldo -= 25
        
        if(re.match("808", number)):
            if(saldo < 10):
                print("saldo insuficiente")
            else:
                saldo -= 10

        if(not re.match("800|2|00|601|641|808", number)):
            print("numero invalido")
        
        print("saldo - ", math.floor(saldo/100), "e", saldo%100, "c")

    elif(re.match("MOEDA [0-9, ]+", input_command) and levantado == True):
        coins = re.split(" ", input_command, 0)
        coins.pop(0)
        for coin in coins:

            if(re.match("1c|2c|5c", coin)):
                saldo += int (coin[0])
            elif(re.match("10c|20c|50c", coin)):
                saldo += int (coin[0]) * 10
            elif(re.match("1e|2e", coin)):
                saldo += int (coin[0]) * 100
            else:
                print(coin, " - moeda invalida")
    
        print("saldo - ", math.floor(saldo/100), "e", saldo%100, "c")
    
    elif(re.match("ABORTAR", input_command)):

        moedas2e = math.floor(saldo/200)
        saldo -=moedas2e*200
        moedas1e = math.floor(saldo/100)
        saldo -=moedas1e*100
        moedas50c = math.floor(saldo/50)
        saldo -=moedas50c*50
        moedas20c = math.floor(saldo/20)
        saldo -=moedas20c*20
        moedas10c = math.floor(saldo/10)
        saldo -=moedas10c*10
        moedas5c = math.floor(saldo/5)
        saldo -=moedas5c*5
        moedas2c = math.floor(saldo/2)
        saldo -=moedas2c*2
        moedas1c = saldo
        saldo -= saldo

        string = "moedas - "
        if(moedas2e != 0):
            string = string + str(moedas2e) + "x2e " 
        if(moedas1e != 0):
            string = string + str(moedas1e) + "x1e "
        if(moedas50c != 0):
            string = string + str(moedas50c) + "x50c "
        if(moedas20c != 0):
            string = string + str(moedas20c) + "x20c "
        if(moedas10c != 0):
            string = string + str(moedas10c) + "x10c "
        if(moedas5c != 0):
            string = string + str(moedas5c) + "x5c "
        if(moedas2c != 0):
            string = string + str(moedas2c) + "x2c "
        if(moedas1c != 0):
            string = string + str(moedas1c) + "x1c"
        
        print(string)
        break
        
        
