
from django.shortcuts import render,redirect
from .models import Upload
import pandas as panda
import logging
import json

logger = logging.getLogger(__name__)
  
def upload(request):
    if request.method == 'POST':
        file=request.FILES['file']
        
        data= panda.read_csv(file,header=[2])
        upload=Upload(file=file,rows=len(data),data=data.to_json())
        
        upload.save()
        return redirect('upload')
    else :
        list = Upload.objects.all()
        return render(request,'upload.html',{'list': list})
               
def display(request, id):
   
    item = Upload.objects.get(id=id)

    
    data = {
        'item': item,
       
    }
    return render(request,'display.html',data)
   
def add(request):
      context = {
          
      }
      return redirect(request,'display.html',context)
  