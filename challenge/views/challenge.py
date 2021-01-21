from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views import View

class Challenge(View):

    def get(self, request):
        return render(request, 'base.html')