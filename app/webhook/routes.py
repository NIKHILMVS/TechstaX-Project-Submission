from flask import Blueprint, json, request

webhook = Blueprint('Webhook', __name__, url_prefix='/webhook')

from flask import Flask
from flask import json
from flask import request
from flask import redirect
from flask import url_for
from flask import session
from app.extensions import client
import time

app=Flask(__name__)

db=client.db
collection=db.github_actions

SECRET_KEY="HI"

@webhook.route('/')
def home():
    return 'hi this is home page'
    
@webhook.route('/github',methods=['POST'])
def message():
    if request.headers['Content-Type']=='application/json':
        print("*"*50)
        str_obj=json.dumps(request.json)
        json_obj=json.loads(str_obj)
        x="pull_request"
        try:
            dct={"request_id":json_obj["sender"]["id"],"Author":json_obj[x]["user"]["login"],"action":json_obj["action"],"from_branch":json_obj[x]["head"]["ref"],"to_branch":json_obj[x]["head"]["repo"]["default_branch"],"timestamp":json_obj[x]["base"]["repo"]["pushed_at"]}
            
            collection.insert_one(dct)
        except:
            pass
        
        return "SUCCESSFUL"


while(True):
    @webhook.route('/receiver')
    def receiver():
        cursor = collection.find().sort([('timestamp', -1)]).limit(1)[0]
        author=cursor["Author"]
        from_branch=cursor["from_branch"]
        to_branch=cursor["to_branch"]
        timestamp=cursor["timestamp"]

        return f"{author} submitted a pull request from {from_branch} to {to_branch} on {timestamp}"
        
    time.sleep(15)


