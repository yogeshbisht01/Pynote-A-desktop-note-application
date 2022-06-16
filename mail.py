# Python code to illustrate Sending mail with attachments
# from your Gmail account
                                                    
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase            #libraries imported
from email import encoders
import pyttsx3 
import requests
import subprocess
import speech_recognition as sr
from tkinter.filedialog import askopenfile

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def remove(toaddr):
    return toaddr .replace(" ", "")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.8           
        r.energy_threshold = 5000           #for voice recognition adjustment
        r.dynamic_energy_threshold = True 
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
    except Exception as e:
        time.sleep(10)
        pyttsx3.speak("i can't hear you,please speak again...") 
        return "None"
    return query

# open the file to be sent
filename = "pynote.txt"
attachment = askopenfile(mode ='r', filetypes =[('Text Files', '*.txt')])

fromaddr = "desktopassistant555@gmail.com"
speak('whom do you want to share')
toaddr=takecommand()
toaddr=remove(toaddr)+"@gmail.com"


# instance of MIMEMultipart
msg = MIMEMultipart()

# storing the senders email address
msg['From'] = fromaddr

# storing the receivers email address      
msg['To'] = toaddr

# storing the subject
msg['Subject'] = "Note."

# string to store the body of the mail
body = "Hey! Here is a note for you :)"

# attach the body with the msg instance
msg.attach(MIMEText(body, 'plain'))

# instance of MIMEBase and named as p
p = MIMEBase('application', 'octet-stream')

# To change the payload into encoded form
p.set_payload((attachment).read())

# encode into base64
encoders.encode_base64(p)

p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

# attach the instance 'p' to instance 'msg'
msg.attach(p)

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login(fromaddr, "deskassis@555")

# Converts the Multipart msg into a string
text = msg.as_string()

# sending the mail
s.sendmail(fromaddr, toaddr, text)

# terminating the session
s.quit()


