from django.shortcuts import render
import datetime



def main(request):
    context = {'message':'Django很棒','time':datetime.datetime.now()}
    return render(request,'main/main.html',context,)