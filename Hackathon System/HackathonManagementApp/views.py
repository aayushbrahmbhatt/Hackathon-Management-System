from django.shortcuts import render
from HackathonManagementApp.models import User,Hackathon,Participant
from django.contrib import messages
from django.http import HttpResponse
from HackathonManagementApp.forms import UserForms,HackathonForms,ParticipantForms
from django.db import connection

def HomePage(request):
    return render(request,'index.html')

def showRunQuery(request):
    return render(request,'showRunQuery.html')

def showHackathon_Detail(request):    
    userdata=User.objects.all()
    Hackathondata = Hackathon.objects.all()
    Participantdata = Participant.objects.all()
    detail = {
                'userdata': userdata,
                'hackathondata' : Hackathondata,
                'participantdata' : Participantdata
            }
    return render(request, 'Hackathon_Detail.html', detail)
    # return render(request,'Hackathon_Detail.html')
def showUser(request):
    showall=User.objects.all()
    detail = {
                'data': showall
            }
    return render(request, 'Hackathon_Detail.html', detail)
 
def InsertUser(request):
    if request.method=="POST":
        if request.POST.get('user_id') and request.POST.get('email_id') and request.POST.get('name') and request.POST.get('password') and request.POST.get('dob') and request.POST.get('age') and request.POST.get('mobile') :
            saverecord = User()
            saverecord.user_id=request.POST.get('user_id')
            saverecord.email_id=request.POST.get('email_id')
            saverecord.name=request.POST.get('name')
            saverecord.password=request.POST.get('password')
            saverecord.dob=request.POST.get('dob')
            saverecord.age=request.POST.get('age')
            saverecord.mobile=request.POST.get('mobile')

            allval=User.objects.all()
            for i in allval:
                if i.user_id==saverecord.user_id:
                    messages.warning(request,'User already exists!')
                    return render(request,'InsertUser.html')
            saverecord.save()
            messages.success(request,'User '+saverecord.name+' is saved successfully..!')
            return render(request,'InsertUser.html')
    else:
        messages.warning(request,'Enter all the data!')
        return render(request, 'InsertUser.html')
        
 
def sortUser(request):
    if request.method=="POST":
        if request.POST.get('Sort'):
            type=request.POST.get('Sort')
            sorted=User.objects.all().order_by(type)
            Hackathondata = Hackathon.objects.all()
            Participantdata = Participant.objects.all()
            context = {
                'userdata': sorted,
                'hackathondata' : Hackathondata,
                'participantdata' : Participantdata
            }
            return render(request,'Hackathon_Detail.html',context)
        else:
            return render(request,'Hackathon_Detail.html')
def editUser(request,id):
    editEventObj=User.objects.get(user_id=str(id))
    return render(request,'editUser.html',{"User":editEventObj})



def updateUser(request,id):
    UpdateEvent=User.objects.get(user_id=str(id))
    form=UserForms(request.POST,instance=UpdateEvent)
    if form.is_valid():
        form.save()
        messages.success(request,'Record updates succesfully!!')
        return render(request,'editUser.html',{"User":UpdateEvent})

def delUser(request,id):
    delUserObj=User.objects.get(user_id=str(id))
    context={
        "User":delUserObj
    }
    return render(request,'delUser.html',context)



def deletedUser(request,id):
    delUserObj=User.objects.get(user_id=str(id))
    delUserObj.delete()
    showall=User.objects.all()
    messages.success(request,'Record deleted succesfully!!')
    return render(request,'delUser.html',{"User": delUserObj})


def RunQuery(request):

    raw_query = request.POST.get('query')

    cursor = connection.cursor()
    cursor.execute(raw_query)
    alldata=cursor.fetchall()

    colnames = [desc[0] for desc in cursor.description]


    return render(request,'RunQuery.html',{'data':alldata,'colnames':colnames, 'lencol':range(len(colnames))})
