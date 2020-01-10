#Programa : Raspberry push button e leds
#Autor : FILIPEFLOP
 
contador = 0
 
import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BOARD)
 
#Define os pinos como saida
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(31, GPIO.OUT)
GPIO.setup(29, GPIO.OUT) 

#desliga todos as saidas
GPIO.output(16,0)#pino 16
GPIO.output(18,0)#pino 18
GPIO.output(31,0)#pino 31
GPIO.output(29,0)#pino 33
contador = 1
i=1
while(1):
  if i > 0 :
    if contador == 1:
        GPIO.output(16, 1)
        print ("paleta direita")
        contador+=1
        time.sleep(1)
        GPIO.output(16, 0)
    #Caso contador = 2, aciona a saida
    if contador == 2:
        GPIO.output(18, 1)
        print ("paleta esquerda")
        contador+=1
        time.sleep(1)
        GPIO.output(18, 0)
 
    #Caso contador = 3, aciona a saida
    if contador == 3:
        GPIO.output(29, 1)
        print ("lampada direita")  
        contador+=1
        time.sleep(1)
        GPIO.output(29, 0)
        #Caso contador = 4, aciona a saida
    if contador == 4:
        GPIO.output(31, 1)
        print ("lampada esquerda ")
        contador+=1
        time.sleep(1)
        GPIO.output(31, 0)
    #Caso contador = 5, desliga todas as saidas
    #zera a variavel contador
    if contador == 5:
        print ("teste terminou \n desligando as saidas e zerando o contador")
        GPIO.output(16,0)
        GPIO.output(18,0)
        GPIO.output(31,0)
        GPIO.output(29,0)
        
        contador = 0   
    
            