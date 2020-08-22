import sys
import time
import random
import datetime
import telepot
import RPi.GPIO as GPIO

# LED
def on(pin):
    GPIO.output(pin, GPIO.HIGH)
    return

def off(pin):
    GPIO.output(pin, GPIO.LOW)
    return

# to use Raspeberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# set up GPIO output channel

GPIO.setup(11, GPIO.OUT)

def handle(message):
    chat_id = message['chat']['id']
    command = message['text']
    print ('Input command is %s' % command)

    if command == '/on':
        bot.sendMessage(chat_id, on(11))
    elif command == '/off':
        bot.sendMessage(chat_id, off(11))

bot_token = '1235090250:AAFwq-3709QPv1qVAX_K_UGFFYRcYnm0oVg'
bot = telepot.Bot(bot_token)
bot.message_loop(handle)
print ('I\'m listening')

while True:
    time.sleep(10)
