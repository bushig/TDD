from django.shortcuts import render
from django.http.response import HttpResponse

def home_page(request):
    return HttpResponse('<html><head><title>To-Do lists</title></head><h1>To-Do app</h1>qweqewqewwe</html>')
