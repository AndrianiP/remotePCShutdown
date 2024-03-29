from flask import Flask, request
from twilio import twiml
from twilio.rest import Client
import time
import os


ACC_SID = os.environ['TWILIO_ACC_SID']
AUTH = os.environ['TWILIO_AUTH_TOKEN']
SID = os.environ['TWILIO_SID']
API_KEY = os.environ['TWILIO_API_KEY']

myNum = os.environ['MY_NUM']
twilNum = os.environ['TWIL_NUM']

client = Client(ACC_SID, AUTH)
app = Flask(__name__)

@app.route('/sms', methods=['GET', 'POST'])
def message():
    time.sleep(5)
    incomingNum = request.values.get('From')
    #print(incomingNum)
    message_body = request.values.get('Body')
    #print(message_body)
    messageAnalysis(incomingNum, message_body)
    return "message_body"

def messageAnalysis(incomingNum, message):
    if (incomingNum == myNum):
        #print(message, "\n")
        if(message == 'Shutdown'):
            shutdown()
        elif(message == 'Restart'):
            restart()
        elif(message == 'Sleep'):
            sleep()
        elif(message == 'LaunchLeague'):
            launchLeague()
        elif(message == 'LaunchApex'):
            launchApex()

    
def shutdown():
    os.system('shutdown /s /t 1')
def restart():
    os.system('shutdown /r /t 1')
def sleep():
    os.system('rundll32.exe powrprof.dll, SetSuspendState Sleep')
def launchLeague():
    print('\nLaunching League of Legends')
    os.system('D: & cd D:\Riot Games\Riot Client\ && RiotClientServices.exe')
    print('\nLaunched League of Legends')
def launchApex():
    print('\nLaunching Apex')
    os.system('D: d: & cd D:\Program Files (x86)\Origin Games\Apex\ && r5apex.exe')
    print('\nLaunched Apex')

if __name__ == '__main__':
    print('App is running\n')
    app.run(host='0.0.0.0', port=5000,debug=True)