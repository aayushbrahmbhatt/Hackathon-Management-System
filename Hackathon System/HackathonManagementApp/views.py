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

# def showGame(request):
#     showall=Game.objects.all()
#     context = {
#         'data': showall
#     }
#     return render(request,'showGame.html',context)

# def sortGame(request):
#     if request.method=="POST":
#         if request.POST.get('Sort'):
#             type=request.POST.get('Sort')
#             sorted=Game.objects.all().order_by(type)
#             context = {
#                 'data': sorted
#             }
#             return render(request,'sortGame.html',context)
#     else:
#         return render(request,'sortGame.html')

# def insertGame(request):
#     if request.method=="POST":
#         if request.POST.get('game_id') and request.POST.get('game_name') and request.POST.get('game_type') and request.POST.get('age_rest') and request.POST.get('height_rest') and request.POST.get('rate') and request.POST.get('duration'):
#             saverecord=Game()
#             saverecord.game_id=request.POST.get('game_id') 
#             saverecord.game_name=request.POST.get('game_name')
#             saverecord.game_type=request.POST.get('game_type')
#             saverecord.age_rest=request.POST.get('age_rest')
#             saverecord.height_rest=request.POST.get('height_rest')
#             saverecord.rate=request.POST.get('rate')
#             saverecord.duration=request.POST.get('duration')

#             allval=Game.objects.all()
            
#             for i in allval:
#                 if int(i.game_id)==int(request.POST.get('game_id')):
#                     messages.warning(request,'Game already exists....!');
#                     return render(request,'insertGame.html')

#             saverecord.save()
#             messages.success(request,'Customer '+saverecord.customer_name+' is saved succesfully!!')
#             return render(request,'insertCustomer.html')
#             saverecord.save()
#             messages.success(request,'Game '+saverecord.game_name+' is saved succesfully!!')
#             return render(request,'insertGame.html')
#     else:
#             return render(request,'insertGame.html')

# def editGame(request,id):
#     editGameObj=Game.objects.get(game_id=id)
#     context={
#         "Game":editGameObj
#     }
#     return render(request,'editGame.html',context)

# def updateGame(request,id):
#     updateGame=Game.objects.get(game_id=id)
#     form=GameForms(request.POST,instance=updateGame)
#     if form.is_valid():
#         form.save()
#         messages.success(request,'Record updates succesfully!!')
#         return render(request,'editGame.html',{"Game":updateGame})

# def delGame(request,id):
#     delGameObj=Game.objects.get(game_id=id)
#     context={
#         "Game":delGameObj
#     }
#     return render(request,'delGame.html',context)

# def deletedGame(request,id):
#     delGameObj=Game.objects.get(game_id=id)
#     delGameObj.delete()
#     showall=Game.objects.all()
#     messages.success(request,'Record deleted succesfully!!')
#     return render(request,'delGame.html',{"Game": delGameObj})


# def showCustomer(request):
#     showall=Customer.objects.all()
#     context = {
#         'data': showall
#     }
#     return render(request,'showCustomer.html',context)

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
        
        # else:
        #   return render(request, 'InsertUser.html')

    




# def insertCustomer(request):
#     if request.method=="POST":
#         if request.POST.get('customer_id') and request.POST.get('customer_name') and request.POST.get('debitcard_id') and request.POST.get('age') and request.POST.get('height') and request.POST.get('house_no') and request.POST.get('street_no') and request.POST.get('pin_code'):
#             saverecord=Customer()
#             saverecord.customer_id=request.POST.get('customer_id') 
#             saverecord.customer_name=request.POST.get('customer_name')
#             saverecord.debitcard_id=request.POST.get('debitcard_id')
#             saverecord.age=request.POST.get('age')
#             saverecord.height=request.POST.get('height')
#             saverecord.house_no=request.POST.get('house_no')
#             saverecord.street_no=request.POST.get('street_no')
#             saverecord.pin_code=request.POST.get('pin_code')

#             allval=Customer.objects.all()
            
#             for i in allval:
#                 if int(i.customer_id)==int(request.POST.get('customer_id')):
#                     messages.warning(request,'Customer already exists....!');
#                     return render(request,'insertCustomer.html')

#             saverecord.save()
#             messages.success(request,'Customer '+saverecord.customer_name+' is saved succesfully!!')
#             return render(request,'insertCustomer.html')
#     else:
#             return render(request,'insertCustomer.html')

# def InsertUser(request):
#     if request.method=="POST":
#         if request.POST.get('user_id') and request.POST.get('email_id') and request.POST.get('name') and request.POST.get('password') and request.POST.get('dob') and request.POST.get('age') and request.POST.get('mobile'):
#             saverecord=User()
#             saverecord.user_id=request.POST.get('user_id') 
#             saverecord.user_name=request.POST.get('email_id')
#             saverecord.password=request.POST.get('name')
#             saverecord.age=request.POST.get('password')
#             saverecord.height=request.POST.get('dob')
#             saverecord.house_no=request.POST.get('age')
#             saverecord.street_no=request.POST.get('mobile')

#             allval=User.objects.all()
            
#             for i in allval:
#                 if int(i.user_id)==int(request.POST.get('user_id')):
#                     messages.warning(request,'User already exists....!');
#                     return render(request,'insertUser.html')

#             saverecord.save()
#             messages.success(request,'User '+saverecord.user_name+' is saved succesfully!!')
#             return render(request,'insertUser.html')
#     else:
#             return render(request,'insertUser.html')

# def sortCustomer(request):
#     if request.method=="POST":
#         if request.POST.get('Sort'):
#             type=request.POST.get('Sort')
#             sorted=Customer.objects.all().order_by(type)
#             context = {
#                 'data': sorted
#             }
#             return render(request,'sortCustomer.html',context)
#     else:
#         return render(request,'sortCustomer.html')

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

# def editCustomer(request,id):
#     editCustomerObj=Customer.objects.get(customer_id=id)
#     context={
#         "Customer":editCustomerObj
#     }
#     return render(request,'editCustomer.html',context)

# def editUser(request,id):
#     editUserObj=User.objects.get(user_id=str(id))
#     context={
#         "User":editUserObj
#     }
#     return render(request,'editUser.html',context)

def editUser(request,id):
    editEventObj=User.objects.get(user_id=str(id))
    return render(request,'editUser.html',{"User":editEventObj})

# def updateCustomer(request,id):
#     updateCustomer=Customer.objects.get(customer_id=id)
#     form=CustomerForms(request.POST,instance=updateCustomer)
#     if form.is_valid():
#         form.save()
#         messages.success(request,'Record updates succesfully!!')
#         return render(request,'editCustomer.html',{"Customer":updateCustomer})

# def updateUser(request,id):
#     updateUser=User.objects.get(user_id=str(id))
#     form=UserForms(request.POST,instance=updateUser)
#     if form.is_valid():
#         form.save()
#         messages.success(request,'Record updates succesfully!!')
#         return render(request,'editUser.html',{"User":updateUser})


def updateUser(request,id):
    UpdateEvent=User.objects.get(user_id=str(id))
    form=UserForms(request.POST,instance=UpdateEvent)
    if form.is_valid():
        form.save()
        messages.success(request,'Record updates succesfully!!')
        return render(request,'editUser.html',{"User":UpdateEvent})
# def delCustomer(request,id):
#     delCusObj=Customer.objects.get(customer_id=id)
#     context={
#         "Customer":delCusObj
#     }
#     return render(request,'delCustomer.html',context)

def delUser(request,id):
    delUserObj=User.objects.get(user_id=str(id))
    context={
        "User":delUserObj
    }
    return render(request,'delUser.html',context)



# def deletedCustomer(request,id):
#     delCusObj=Customer.objects.get(customer_id=id)
#     delCusObj.delete()
#     showall=Customer.objects.all()
#     messages.success(request,'Record deleted succesfully!!')
#     return render(request,'delCustomer.html',{"Customer": delCusObj})

def deletedUser(request,id):
    delUserObj=User.objects.get(user_id=str(id))
    delUserObj.delete()
    showall=User.objects.all()
    messages.success(request,'Record deleted succesfully!!')
    return render(request,'delUser.html',{"User": delUserObj})

# def runQueryGame(request):
#     raw_query = "select * from gamezone.game where game_type='Racing' and age_rest>=18;"

#     cursor = connection.cursor()
#     cursor.execute(raw_query)
#     alldata=cursor.fetchall()

#     return render(request,'runQueryGame.html',{'data':alldata})



# def runQueryCustomer(request):
#     raw_query = "select customer_id, customer_name, customer.debitcard_id, balance from gamezone.customer join gamezone.debitcard on customer.debitcard_id=debitcard.debitcard_id;"

#     cursor = connection.cursor()
#     cursor.execute(raw_query)
#     alldata=cursor.fetchall()

#     return render(request,'runQueryCustomer.html',{'data':alldata})

def RunQuery(request):

    raw_query = request.POST.get('query')

    cursor = connection.cursor()
    cursor.execute(raw_query)
    alldata=cursor.fetchall()

    colnames = [desc[0] for desc in cursor.description]


    return render(request,'RunQuery.html',{'data':alldata,'colnames':colnames, 'lencol':range(len(colnames))})