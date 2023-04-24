from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
def insert_student(request):
    if request.method=='POST':
        si=request.POST['si']
        sn=request.POST['sn']
        ph=request.POST['ph']
        pe=request.POST['pe']
        re=request.POST['re']
        SO=Student.objects.get_or_create(sid=si,sname=sn,phone=ph,percentage=pe,remarks=re)[0]
        SO.save()

        SDO=Student.objects.all()
        d={'student':SDO}

        return render(request,'display_student.html',context=d)
    return render(request,'insert_student.html')





def insert_course(request):
    sid=Student.objects.all()
    d={'sid':sid}

    if request.method=='POST':
        ci=request.POST['ci']
        si=request.POST['si']
        co=request.POST['co']
        clg=request.POST['clg']
        SO=Student.objects.get_or_create(sid=si)[0]
        SO.save()

        CO=Course.objects.get_or_create(cid=ci,sid=SO,course=co,college=clg)[0]
        CO.save()

        CDO=Course.objects.all()
        d={ 'CDO' : CDO }
        return render(request,'display_course.html',d)
        
    return render(request,'insert_course.html',d)


def update_student(request):
    SWO=Student.objects.all()
    d={'SO':SWO}
    if request.method=='POST':
        si=request.POST['si']
        sn=request.POST['sn']
        ph=request.POST['ph']
        pe=request.POST['pe']
        re=request.POST['re']
        SO=Student.objects.get(sid=si)

        SO1=Student.objects.filter(sid=SO).update(sname=sn,phone=ph,percentage=pe,remarks=re)
        SOW=Student.objects.all()
        d1={'student':SOW}
        return render(request,'display_student.html',d1)

    return render(request,'update_student.html',context=d)