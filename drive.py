import json
import requests
from tkinter.filedialog import askopenfile
headers = {"Authorization": "Bearer ya29.A0ARrdaM97g-mtUySZ8FKLIpd0LXKWfcJOLuEnYZk_k66_nVvb4h6GzAiTUptvQDKOvK7XVdH9LoQmgAl_cn3alb9mOmLROZwlzKA4GVQyeVXURXqkU47EywW2UEmeN9Thb_12EZA7qxTkpVZMNf7j1_Pd41sY"} #add your oath authorization key, of the mail you want to use for your note backup
para = {
    "name": "Pynote.txt",
}
files = {
    'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
    'file': askopenfile(mode ='r', filetypes =[('Text Files', '*.txt')])
}
r = requests.post(
    "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
    headers=headers,
    files=files
)
print(r.text)
