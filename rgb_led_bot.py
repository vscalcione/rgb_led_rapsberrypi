import sys
import time
import random
import datetime
import telepot
import RPi.GPIO as GPIO
import os

# LED
def on(pin):
    GPIO.output(pin, GPIO.HIGH)
    return "Led state: ON"

def off(pin):
    GPIO.output(pin, GPIO.LOW)
    return "Led state: OFF"

def welcome():
    return "Hi, Im a bot"

# to use Raspeberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# set up GPIO output channel

GPIO.setup(11, GPIO.OUT)

def handle(message):
    chat_id = message['chat']['id']
    command = message['text']
    print ('Input command is %s' % command)

    if command == "/start":
        bot.sendMessage(chat_id, welcome())
    if command == '/on':
        bot.sendMessage(chat_id, on(11))
    elif command == '/off':
        bot.sendMessage(chat_id, off(11))

bot_token = os.environ.get('BOT_TOKEN')
bot = telepot.Bot(bot_token)
bot.message_loop(handle)
print ('I\'m listening')

while True:
    time.sleep(10)
