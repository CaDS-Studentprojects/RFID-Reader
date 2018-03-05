#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import sys
sys.path.insert(0,"/home/pi/MFRC522")
import MFRC522
from time import sleep
import json
import time
import signal
from File_Manager import File_Manager
import grpc
import rfid_pb2
import rfid_pb2_grpc

present_user_dict = {}
uid_dict = {}
continue_reading = True

def main():
    # Need to explicitly declare as global because of assignment!
    global uid_dict

    # Remove "channel already in use" warning
    GPIO.setwarnings(False)

    # Hook the SIGINT
    signal.signal(signal.SIGINT, end_read)

    # Connect to grpc server
    channel = grpc.insecure_channel('localhost:50051')
    stub = rfid_pb2_grpc.RFID_SERVICEStub(channel)

    uid_dict = import_UID_dict()

    print "Welcome to the RFID Reader"
    print "Press Ctrl-C to stop."

    MIFAREReader = MFRC522.MFRC522()

    # Default key for authentication
    key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]

    while continue_reading:
            # Scan for cards
            (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

            # If a card is found
            if status == MIFAREReader.MI_OK:
                print "----------------------------------"
                print "Card detected"

                # Get the UID of the card
                (status,uid) = MIFAREReader.MFRC522_Anticoll()

                # If we have the UID, continue
                if status == MIFAREReader.MI_OK:
                    combined_UID = str(uid[0]) + str(uid[1]) + str(uid[2]) + str(uid[3])
                    print "UID: " + combined_UID

                    # Select the scanned tag
                    MIFAREReader.MFRC522_SelectTag(uid)

                    # Authenticate
                    status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, 8, key, uid)

                    # Check if authenticated
                    if status == MIFAREReader.MI_OK:
                        print "Data: " + str(MIFAREReader.MFRC522_Read(8))
                        present_user_dict = check_Login_Status(stub, combined_UID)
                        MIFAREReader.MFRC522_StopCrypto1()
                    else:
                        print "Authentication error"

                    sleep(2)


def check_Login_Status(stub, uid):
    if not present_user_dict:
        print "System starting...."

    username = uid_dict[uid];

    if uid not in present_user_dict:
        present_user_dict[uid] = username
        print "User " + username + " with ID: " + uid + " logged in!"

        # RPC with logged in user info
        stub.RFID_Change(rfid_pb2.RFID_MSG(id=1234, name_login=username, user_list=str(present_user_dict)))
    else:
        del present_user_dict[uid]
        print "User " + username + " with ID: " + uid + " logged out!"

        # RPC with logged out user info
        stub.RFID_Change(rfid_pb2.RFID_MSG(id=1234, name_logout=username, user_list=str(present_user_dict)))

        if not present_user_dict:
            print "System shutting down...."

    print present_user_dict

    return present_user_dict

# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading
    print "Ctrl+C captured, ending read."
    continue_reading = False
    #fileManager.export_JSON(uid_dict, "UIDs.json")
    GPIO.cleanup()

def import_UID_dict():
    fileManager = File_Manager()
    uid_dict = fileManager.import_JSON("UIDs.json")

    # Initialize with empty dict if no file exists
    if uid_dict == "":
        uid_dict = {}
    else:
        # deserialize to object
        uid_dict = json.loads(uid_dict)

    print "Imported dictionary: "
    print uid_dict

    return uid_dict


if __name__ == '__main__':
    main()