import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

TRIG = 7
ECHO = 12
Buzzer = 32

GPIO.setup(TRIG, GPIO.OUT)
GPIO.output(TRIG, 0)
GPIO.setup (ECHO, GPIO.IN)
GPIO.setup (Buzzer, GPIO.OUT)

GPIO.output(Buzzer, True)
buzzer = GPIO.PWM(Buzzer, 1)
buzzer.start(1)

def DutyCycle(distance):
    if distance < 25 and distance > 20:
        return 20
    if distance < 20 and distance > 16:
        return 40
    if distance < 16 and distance > 12:
        return 60
    if distance < 12 and distance > 8:
        return 80
    if distance < 8 and distance > 5:
        return 90
    if distance < 5:
        return 100
    if distance > 25:
        return 1
    else:
        return 1
def dist():
    print("Checking distance...")
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    start = time.time()
    stop = time.time()
    while GPIO.input(ECHO) == 0:
        start = time.time()
    while GPIO.input(ECHO) == 1:
        stop = time.time()
    realTime = stop - start
    distance = realTime * 17150
    distance = round(distance, 2)
    print ("Checked")
    print ("Distance: ", distance, "cm")
    return distance
try:
    while True:
        GPIO.output(TRIG, False)
        time.sleep(1)
        distance = dist()
        sound = DutyCycle(distance)
        buzzer.ChangeDutyCycle(sound)
        time.sleep(1)
except KeyboardInterrupt:
    print ("Program stopped")
    GPIO.cleanup()
    buzzer.stop
