#!/usr/bin/env python3

import zmq
import time
import sys

import filters as f
import utils as u


port = "5556"
if len(sys.argv) > 1:
    port =  sys.argv[1]
    int(port)

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:%s" % port)

while True:
    #  Wait for next request from client
    message = socket.recv_json()
    print("Received request: ", message)
    time.sleep (1)
    reply = u.process_message(message['message'])
    
    print("Sending back the reply: ", reply)
    socket.send_json({'message': reply})

