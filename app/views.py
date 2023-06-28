from django.shortcuts import render
from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from django.http import HttpResponse
from .tg_def import message_get
import json

class WebhookView(APIView):
    def post(self, request):
        message = message_get(request)
        if message["data"]["callback"] != "none":
            response = redirect('callback_get')
        elif message["content"]["photo_id"] != "none":
            response = redirect('photo_get')
        elif message["content"]["audio"] != "none":
            response = redirect('audio_get')
        elif message["content"]["document"] != "none":
            response = redirect('document_get')
        elif message["content"]["text"] != "none":
            text_get(message)
        return HttpResponse()

def text_get(request):
    print(request)
    return 

def callback_get(request):
    print(request)
    return 

def photo_get(request):
    print(request)
    return 

def audio_get(request):
    print(request)
    return 

def document_get(request):
    print(request)
    return 