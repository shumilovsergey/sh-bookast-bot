import json
import requests
from project.const import BOT_TOKEN

def message_get(request):
    data = json.loads(request.body.decode('utf-8'))
    chat_id = data["message"]["chat"]["id"]
    message_id = data["message"]["message_id"]
    ###
    try: 
        text = data["message"]["text"]
    except:
        text = "none"
    ###    
    try:
        photo_id = data["message"]["photo"][0]["file_id"]
    except:
        photo_id = "none"
    ###
    try: 
        audio_name = data["message"]["audio"]["file_name"]
        audio_type = data["message"]["audio"]["mime_type"]
        audio_id = data["message"]["audio"]["file_id"]
        audio = {
            "audio_name" : audio_name,
            "audio_type" : audio_type,
            "audio_id" : audio_id
        }
    except:
        audio = "none"
    ###
    try:
        document_name = data["message"]["document"]["file_name"]
        document_type = data["message"]["document"]["mime_type"]
        document_id = data["message"]["document"]["file_id"]
        document = {
            "document_name" : document_name,
            "document_type" : document_type,
            "document_id" : document_id
        }
    except:
        document = "none"
    ###
    message = {
        "data" : {
            "chat_id" : chat_id,
            "message_id" : message_id
        }, 
        "content" : {
            "text" : text,
            "photo_id" : photo_id,
            "audio" : audio,
            "document" : document
        }
    }
    return message

def text_send(message):
    chat_id = message["data"]["chat_id"]
    text = message["content"]["text"]
    data = { 
        "chat_id": chat_id,
        "text": text
    }
    response = requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", data)
    return response





