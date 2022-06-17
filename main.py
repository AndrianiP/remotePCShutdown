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
    incomingNum = request.form.get('From')
    print(incomingNum)
    message_body = request.form.get('Body')
    print(message_body)
    messageAnalysis(incomingNum, message_body)

def messageAnalysis(incomingNum, message):
    if (incomingNum == myNum):
        print(message, "\n")
        if(message == 'shutdown'):
            shutdown()
        elif(message == 'restart'):
            restart()
        elif(message == 'sleep'):
            sleep()
        elif(message == 'launchLeague'):
            launchLeague()
        elif(message == 'launchApex'):
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
    os.system('D: & cd D:\Documents\Coding\remotePCShutdown\ && python -m http.server 5000')
    print('App is running')
    app.run(host='0.0.0.0', port=5000,debug=True)

