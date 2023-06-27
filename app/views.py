from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from django.http import HttpResponse
from .tg_def import message_get
from .tg_def import text_send






class WebhookView(APIView):
    def post(self, request):
        message = message_get(request)

        text_send(message)
        return HttpResponse()