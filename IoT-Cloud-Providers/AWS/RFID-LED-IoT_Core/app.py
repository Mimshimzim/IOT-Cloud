from umqtt.simple import MQTTClient
from machine import Pin, Timer
from math import sin
from read_rfid import read_rfid
from wlan_connect import wifi_connect
import network
import ssl
import ubinascii
import machine
import time
import ntptime
import led

###################
# MQTT Configuration #
###################
MQTT_CLIENT_ID = ""
MQTT_CLIENT_KEY = ""
MQTT_CLIENT_CERT = ""
MQTT_BROKER = ""
MQTT_TOPIC = ""

##################
# WIFI Configuration #
##################
WIFI_SSID = ''
WIFI_PASSWORD = ''

wifi_connect(WIFI_SSID,WIFI_PASSWORD)

def read_der_file(file):
    with open(file, 'rb') as input:
        data = input.read()
    input.close()
    return data

def mqtt_callback(topic, msg):
    """ Callback function for received messages"""
    rfid_tag = msg.decode()
    print("received data:")
    print(rfid_tag)
    if rfid_tag  == "A96036F3":
        led.turn_on()
    elif rfid_tag == "1DE8F2B1":
        led.turn_off()


key = read_der_file(MQTT_CLIENT_KEY)
cert = read_der_file(MQTT_CLIENT_CERT)
ssl_params = {'key': key,'cert': cert, 'server_side': False}

ntptime.settime()
mqtt = MQTTClient( MQTT_CLIENT_ID, MQTT_BROKER, keepalive = 60, ssl = True, ssl_params = ssl_params )
mqtt.set_callback(mqtt_callback)
mqtt.connect()
while True:
    print("Please the RFID card:")
    data=read_rfid()
    mqtt.publish(MQTT_TOPIC,data)
    mqtt.subscribe(MQTT_TOPIC)

