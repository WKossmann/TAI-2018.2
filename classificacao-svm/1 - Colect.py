import RPi.GPIO as GPIO
import time
import csv
import sys

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
  writer = csv.writer(open("Dados/Dados2.csv", 'w'))
  while(1):
      for i in range(100):  
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
        
        print(red,",", green, ",", blue)
        
        data = [float(red),float(green),float(blue),int(cor)]
        print(data)
        writer.writerow(data)

      cor = input()
      if cor == "x":
        break

def endprogram():
    GPIO.cleanup()

if __name__=='__main__':
    
    setup()

    try:
        loop()

    except KeyboardInterrupt:
        endprogram()
