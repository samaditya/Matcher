from django.shortcuts import render
from .models import *
# Create your views here.
from django.shortcuts import render,HttpResponse
from PyPDF2 import PdfReader


def index(request):
     
     # if request.method == "POST":
      
     return render(request, "index.html")

def handler(request):
     
     if request.method == "POST":
          key = request.POST.get('key')
          
          file = request.FILES.get('Myfile')
          a = MyModel(file = file)
          a.save()
          print(file)
          print(key)
          reader = PdfReader(file)
          number_of_pages = len(reader.pages)          
          page = reader.pages[0]
          text = page.extract_text()
         
          

          if text.find(key)!=-1:
               return render(request , "success.html")
          else:
               return render(request , "index.html")
     