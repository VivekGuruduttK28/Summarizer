import time
from django.http import HttpResponse
from django.shortcuts import redirect, render

from flask import Flask, render_template,request
from django.contrib import messages
from new import settings

from new.settings import MEDIA_ROOT,MEDIA_URL
from .text import  sum1
from .ds1 import sum2
from .models import details,image
import imghdr
import time
import qrcode
import urllib.parse
import random
from new import settings
from django.core.mail import EmailMessage
from .imagetot import text


def index(request,uname):
     
     try:
        try:
             
             ip_address = request.META.get('REMOTE_ADDR', None)
             print(ip_address)
             user=details.objects.get(username= uname)
             if not user.subscription:
                  return redirect('/subscribe/{}'.format(uname))
             print(user.ip)
             if ip_address!=user.ip:
                  
                  return redirect('/')
             
             body=request.POST["data"]
             result=sum1(body)
             return render(request,'file.html',{'result':result,'input':body,'uname':uname})
        except:
               user=details.objects.get(username= uname)
               return render(request,'file.html',{'uname':uname})
     except:
          return redirect('/')


    

def summarize2(request,uname):
     try:
        try:
             ip_address = request.META.get('REMOTE_ADDR', None)
             
             user=details.objects.get(username= uname)
             if ip_address!=user.ip:
                  return redirect('/')
             body=request.POST["data"]
             result=sum2(body)
             return render(request,'file1.html',{'result':result,'input':body,'uname':uname})
        except:
               user=details.objects.get(username= uname)
               return render(request,'file1.html',{'uname':uname})
     except:
          return redirect('/')



def landing(request,uname):
      return render (request,"landing.html",{'uname':uname})
def login(request):
     return render(request,'login.html')

def signup(request):
     username1=request.POST['username']
     email1=request.POST["email"]
     password1=request.POST["pswd"]
     try:
          k=details.objects.get(username=username1)
          print('error')
          return redirect('/')

     except:
          lol=details(username=username1,password=password1,email=email1,subscription=False,ip=0)
          lol.save()
          messages.success(request, 'Account created successfully!')
          return redirect('/')
          

def signin(request):
     email1=request.POST['lmao']
     password1=request.POST['lmaol']
     user=details.objects.get(email=email1)
     if user.password==password1:
          uname=user.username
          ip_address = request.META.get('REMOTE_ADDR', None)
          user.ip=ip_address
          user.save()
          return redirect('/land/{}'.format(uname))
          
     else:
          return redirect('/')
     
def payment(request,uname):
     
     user=details.objects.get(username= uname)
     if  user.subscription:
           img_name='success.png'
           return render(request,"payment.html",{"img1":img_name})
     qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
            )
     gpay_uri = 'upi://pay?pa=vishalsmurali@okhdfcbank&pn=Vishal S Murali&am=50.00&cu=INR&aid=uGICAgICfiuT0ag'
     
     qr.add_data(gpay_uri)
     qr.make(fit=True)
            

    
    # Create an image from the QR code
     qr_img = qr.make_image(fill_color="black", back_color="white")
     img_name = 'qr' +uname + '.png'
     qr_img.save(settings.MEDIA_ROOT+ '/' + img_name)
     
     
     email_sender='vtech232003@gmail.com'
     email_password='yjgnaqafqtoylopf'
     email_receiver='vishalsmurali@gmail.com'
     em=EmailMessage()
     em['From']='vtech232003@gmail.com'
     em['To']=''
     em['subject']='True'
     em.set_content('/makeittrue/{}'.format(uname))
     context=ssl.create_default_context()
     with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
          smtp.login(email_sender,email_password)
          smtp.sendmail(email_sender,email_receiver,em.as_string())
     return render(request,'payment.html',{'img1':img_name,'MEDIA_ROOT':MEDIA_ROOT})

def pay(request,uname):
     ip_address = request.META.get('REMOTE_ADDR', None)
             
     user=details.objects.get(username= uname)
     if ip_address!=user.ip:
          return redirect('/')
     return render(request,'subscribe.html',{'uname':uname})

import os
from email.message import EmailMessage
import ssl
import smtplib


def makeittrue(request,uname):
     dele=uname
     media_path = os.path.join(settings.MEDIA_ROOT)  # Replace 'images' with your media subdirectory
    
     image_path = os.path.join(media_path, 'qr'+dele+'.png')
    
    # Remove the image file from the media directory
     if os.path.exists(image_path):
         os.remove(image_path)
     else:
          print('No image')
     
     user=details.objects.get(username=uname)
     user.subscription=True
     user.save()
     return HttpResponse('success')

def stt(request,uname):
     try:
          ip_address = request.META.get('REMOTE_ADDR', None)
               
          user=details.objects.get(username= uname)
          if ip_address!=user.ip:
               return redirect('/')
          
     except:
          return redirect('/')
     if not user.subscription:
                  return redirect('/subscribe/{}'.format(uname))
     return render (request,"stt.html",{'uname':uname})

def tot(request,uname):
     try:     
          ip_address = request.META.get('REMOTE_ADDR', None)
               
          user=details.objects.get(username= uname)
          if ip_address!=user.ip:
               return redirect('/')
     except:
          return redirect('/')
     try:
          image2=request.FILES['image']
          x=random.randint(1,1000)
          print(x)
          image4=image2.name
          image3=image(name=x,image1=image2)
          image3.save()
          res=text(image4)
          
          
          try:
                    image3 = image.objects.get(name=x)
                    image3.image1.delete()  # Delete the image file
                    image3.delete()  # Delete the image model instance
          except image.DoesNotExist:
                    print("Image instance not found for deletion.")
          if not user.subscription:
                  return redirect('/subscribe/{}'.format(uname))
          return render(request,'tot.html',{'res':res,'uname':uname})
     except:
          if not user.subscription:
                  return redirect('/subscribe/{}'.format(uname))
          return render(request,'tot.html',{'uname':uname})
     
from .audio import text_audio,delete_file

def audio(request,uname):
     try:
          ip_address = request.META.get('REMOTE_ADDR', None)
               
          user=details.objects.get(username= uname)
          if ip_address!=user.ip:
               return redirect('/')
     except:
          return redirect('/')
     try:
          if not user.subscription:
                  return redirect('/subscribe/{}'.format(uname))
          text=request.POST['text1']
          audio1,x=text_audio(text)
          print('l')
          
          return render(request,'audio.html',{'audio':audio1,'uname':uname})
     except:
          if not user.subscription:
                  return redirect('/subscribe/{}'.format(uname))
          print('hell')
          return render(request,'audio.html',{'uname':uname})
     

from django.shortcuts import render

def error_404(request, exception):
    return render(request, '404/error.html', status=404)
