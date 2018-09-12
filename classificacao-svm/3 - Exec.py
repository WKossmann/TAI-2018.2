import pandas as pd
import RPi.GPIO as GPIO
import time
import csv
import sys
from sklearn.svm import SVC
from sklearn.externals import joblib
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

FILE_TO_DOWNLOAD =  "Dados2.csv"
DATA_PATH = "Dados/"

# Importando dados do arquivo
dataset = pd.read_csv(DATA_PATH+FILE_TO_DOWNLOAD)

X = dataset.iloc[:,:3].values
Y = dataset.iloc[:,3].values

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.25, random_state = 0)

sc = StandardScaler()
X_train = sc.fit_transform(X_train)

classif = joblib.load('Dados/treinamento2.pkl')

s2 = 23
s3 = 24
signal = 25
NUM_CYCLES = 10

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(signal,GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(s2,GPIO.OUT)
    GPIO.setup(s3,GPIO.OUT)
    

def loop():
    temp = 1
    cor = input()
    while(1):
        # Coletando o valor de vermelho do sensor
        GPIO.output(s2,GPIO.LOW)
        GPIO.output(s3,GPIO.LOW)
        time.sleep(0.01)
        start = time.time()
        for impulse_count in range(NUM_CYCLES):
          GPIO.wait_for_edge(signal, GPIO.FALLING)
        duration = time.time() - start      #seconds to run for loop
        red  = NUM_CYCLES / duration   #in Hz

        #Coletando o valor de azul do sensor
        GPIO.output(s2,GPIO.LOW)
        GPIO.output(s3,GPIO.HIGH)
        time.sleep(0.01)
        start = time.time()
        for impulse_count in range(NUM_CYCLES):
            GPIO.wait_for_edge(signal, GPIO.FALLING)
        duration = time.time() - start
        blue = NUM_CYCLES / duration

        #Coletando o valor de verde do sensor
        GPIO.output(s2,GPIO.HIGH)
        GPIO.output(s3,GPIO.HIGH)
        time.sleep(0.01)
        start = time.time()
        for impulse_count in range(NUM_CYCLES):
            GPIO.wait_for_edge(signal, GPIO.FALLING)
        duration = time.time() - start
        green = NUM_CYCLES / duration

        #print(red,",", green, ",", blue)

        Test = [[int(red),int(green),int(blue)]]
        Test = sc.transform(Test)

        Result = classif.predict(Test)
        Resposta = ['Vermelho','Verde','Azul','Amarelo']
        print(Resposta[Result[0]])

        #cor = input()
        #if cor == "x":
        #    break

def endprogram():
    GPIO.cleanup()

if __name__=='__main__':
    
    setup()

    try:
        loop()

    except KeyboardInterrupt:
        endprogram()
