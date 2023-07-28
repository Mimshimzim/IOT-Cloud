from mfrc522 import MFRC522
from machine import Pin

lock = Pin(28, Pin.OUT)
buzzer = Pin(27, Pin.OUT)
RLed = Pin(18, Pin.OUT)
GLed = Pin(19, Pin.OUT)
led = Pin(15, Pin.OUT)

lock.value(1)
buzzer.value(0)
RLed.value(0)
GLed.value(0)


def uid_to_string(uid):
    mystring = ""
    for i in uid:
        mystring = "%02X" % i + mystring
    return mystring


def read_rfid():
    rc522 = MFRC522(spi_id=0, sck=6, miso=4, mosi=7, cs=5, rst=22)

    (stat, tag_type) = rc522.request(rc522.REQALL)
    (status, raw_uid) = rc522.SelectTagSN()

    #stat == rc522.OK:
    rfid_data = uid_to_string(raw_uid)
    return(rfid_data)



