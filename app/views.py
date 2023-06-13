from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from django.http import HttpResponse
import json
import requests
from project.const import BOT_TOKEN



def home(request):
    return render(request, 'app/page_1.html')

class HelloWorldView(APIView):
    def get(self, request):
        data = {"message": "Hello, world!"}
        return Response(data)
    



def webhook(request):
    if request.method == 'POST':

        data = json.loads(request.body.decode('utf-8'))
        message = data['message']
        chat_id = message['chat']['id']
        send_message(chat_id, 'Hello, World!')
        
    return HttpResponse()

def send_message(chat_id, text):
    
    url = f"https://api.telegram.org/{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("Message sent successfully!")
    else:
        print("Failed to send the message.")
