# remotePCShutdown
 Text to Shutdown 

Using Twilio service and Ngrok you are able to execute certain powershell/cmd commands that are predetermined which can allow you to shutdown your pc remotely, put it to sleep, or restart it.

Combine this with task scheduler and you can have it start running at boot.

How to use:

-Download Flask library

-Get Twilio phone number setup

-Replace ACC_SID with your twilio Account SID

-Replace the AUTH with your authorization token

-Replace API_Key with your API key or leave it blank

-Replace *myNum* with your phone number

-Replace *twilNum* with your registered twilio phone number

-For the launchLeague method and launchApex method, (you can change the name if you want and then) change the file directory to whichever your file directory is. The command first goes to the D: drive then goes into the game directory then executes the application if possible.

-Change line 59's directory to wherever you downloaded these files.
