from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from django.http import HttpResponse
import json
import requests
from project.const import BOT_TOKEN



def webhook(request):
    if request.method == 'POST':

        data = json.loads(request.body.decode('utf-8'))
        print(data)
        message = data['message']
        chat_id = message['chat']['id']
        test = message["text"]
        buttons = [
            ["Button 1", "Button 2"],
            ["Button 3", "Button 4"]
        ]
        send_message(chat_id, test, buttons)

    return HttpResponse()

def send_message(chat_id, text, buttons):
    data = {
        "chat_id": chat_id,
        "text": text,
        "reply_markup": {
            "keyboard": buttons,
            "one_time_keyboard": True,
            "resize_keyboard": True
        }
    }
    response = requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", data)
    print(response)
    return 


