from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Ownerreg,Customer,Roomdetails,Roombook,Category,Sub_category,Feedbackown,Feedbackcust,Massege,Mail,Country,State,City

def index(request):
    return render(request,"myrmapp/index.html")
def registration(request):
  country = Country.objects.values("country_name").distinct()
  state = State.objects.values("St_name").distinct()
  city = City.objects.values("city_name").distinct()
  context = {'f': country,'g': state,'h': city}
  return render(request,"myrmapp/registration.html",context)
def registrationcode(request):
    s = Ownerreg(username=request.POST['txtuser'],email=request.POST['email'],password=request.POST['password'],mobile=request.POST['mobile'],gender=request.POST['gender'],address=request.POST['address'],country=request.POST['country'],state=request.POST['state'],city=request.POST['city'],reg_date=request.POST['regdate'])
    s.save()
    r="Registration submitted successfully"
    return render(request,"myrmapp/registration.html",{"res":r})
def registrationcustomer(request):
  country = Country.objects.values("country_name").distinct()
  state = State.objects.values("St_name").distinct()
  city = City.objects.values("city_name").distinct()
  context = {'f': country,'g': state,'h': city}
  return render(request,"myrmapp/registrationcustomer.html",context)
def registrationcustomercode(request):
    s = Customer(username=request.POST['txtuser'],email=request.POST['email'],password=request.POST['password'],mobile=request.POST['mobile'],gender=request.POST['gender'],address=request.POST['address'],country=request.POST['country'],state=request.POST['state'],city=request.POST['city'],reg_date=request.POST['regdate'])
    s.save()
    r="Customer Registration submitted successfully"
    return render(request,"myrmapp/registrationcustomer.html",{"res":r})


def login(request) :
    return render(request,"myrmapp/login.html")
def loginall(request):
    ouname  = Ownerreg.objects.filter(email=request.POST['txtuser'])
    opass1  = Ownerreg.objects.filter(password=request.POST['txtpass'])
    cuname  = Customer.objects.filter(email=request.POST['txtuser'])
    cpass1  = Customer.objects.filter(password=request.POST['txtpass'])
    if ouname.count()>0 and opass1.count()>0:
        request.session['sid'] = request.POST['txtuser']
        return HttpResponseRedirect("/myrmapp/ownerdash")
    elif cuname.count()>0 and cpass1.count()>0:
        request.session['sid'] = request.POST['txtuser']
        return HttpResponseRedirect("/myrmapp/custodash")
    else :
        r="invalid userid and password"
        return render(request,"myrmapp/login.html",{"res":r})	

def ownerdash(request):
    if request.session.has_key('sid'): 
        s=request.session['sid']
        return render(request,'myrmapp/ownerdashboard.html',{"uname" : s})  
    else :
        return HttpResponseRedirect("/login") 
def ownerlogout(request):
    if request.session.has_key('sid'): 
        del request.session['sid'] 
        return HttpResponseRedirect("/myrmapp")	
def custodash(request):
    if request.session.has_key('sid'): 
        s=request.session['sid']
        r=request.session['rid']
        data=Roomdetails.objects.filter(id=r)
        return render(request,'myrmapp/custodashdashboard.html',{"uname" : s,"flist":data})  
    else:
        return HttpResponseRedirect("/login")

def custologout(request):
    if request.session.has_key('sid'): 
        del request.session['sid'] 
        return HttpResponseRedirect("/myrmapp")   

def addcat(request):
  return render(request,'myrmapp/addcat.html')
def addcatcode(request):
  s = Category(category_name=request.POST['addcat'])
  s.save()
  r="Add Category successfully"
  return render(request,'myrmapp/addcat.html',{"result":r})

def addsubcat(request):
  cat = Category.objects.values("category_name").distinct()
  context = {'f': cat}
  return render(request,'myrmapp/addsubcat.html',context)
def addsubcatcode(request):
  cid= Category.objects.get(category_name=request.POST['category_name']) 
  s = Sub_category(categoryid=cid,subcategory_name=request.POST['addsubcat'])
  s.save()
  r="Add SubCategory successfully"
  return render(request,'myrmapp/addsubcat.html',{"result":r})
def addroom(request):
  email = Ownerreg.objects.values("email").distinct()
  cat = Category.objects.values("category_name").distinct()
  subcat=Sub_category.objects.values("subcategory_name").distinct()
  city=City.objects.values("city_name").distinct()
  context = {'e':email,'f': cat,'c':subcat,'ct':city}
  return render(request,'myrmapp/addroom.html',context) 
def addroomcode(request):
  #oid= Ownerreg.objects.get(email=request.POST['email']) 
  #cid= Category.objects.get(category_name=request.POST['category_name']) 
  #scid= Sub_category.objects.get(subcategory_name=request.POST['subcategory_name']) 
  s = Roomdetails(ownemail=request.POST['ownemail'],roomtitle=request.POST['roomtitle'],roomdetails=request.POST['roomdetails'],category=request.POST['cat_name'],subcategory=request.POST['subcat_name'],roomimg=request.POST['roomimg'],landmark=request.POST['landmark'],adddate=request.POST['adddate'],price=request.POST['price'],city=request.POST['city'],status=request.POST['status'])
  s.save()
  r="Room Add successfully"
  return render(request,'myrmapp/addroom.html',{"result":r})   

def viewcat(request):
  if request.session.has_key('sid'):
   s=request.session['sid'] 
   flist = Category.objects.all()
   context = {'f': flist}
   return render(request,'myrmapp/viewcat.html',context)    
def viewsubcat(request):
  if request.session.has_key('sid'):
   s=request.session['sid'] 
   cat=Category.objects.all()
   flist = Sub_category.objects.all()
   context = {'c':cat,'f': flist}
   return render(request,'myrmapp/viewsubcat.html',context)    
def viewroom(request):
  if request.session.has_key('sid'):
   s=request.session['sid'] 
   flist = Roomdetails.objects.all()
   context = {'f': flist}
   return render(request,'myrmapp/viewroom.html',context)    
def viewcustomer(request) :
   if request.session.has_key('sid'):
     s=request.session['sid'] 
     flist = Customer.objects.all()
     context = {'f': flist}
   return render(request,'myrmapp/viewcustomer.html',context)
def viewowner(request) :
   if request.session.has_key('sid'):
     s=request.session['sid'] 
     flist = Ownerreg.objects.all()
     context = {'f': flist}
   return render(request,'myrmapp/viewowner.html',context)
def viewbookedroom(request) :
  if request.session.has_key('sid'):
   s=request.session['sid'] 
   flist = Roombook.objects.all()
   context = {'f': flist}
   return render(request,'myrmapp/viewbookedroom.html',context)
def viewbookedroomc(request) :
  if request.session.has_key('sid'):
   s=request.session['sid'] 
   flist = Roombook.objects.filter(customerid=s)
   context = {'f': flist}
   return render(request,'myrmapp/viewbookedroomc.html',context)
def ownprofile(request):                                    #......................problem
  if request.session.has_key('sid'):
   s=request.session['sid'] 
   #uname  = Customer.objects.filter(username=request.POST['sid'])
   flist = Ownerreg.objects.filter(email=s)
   context = {'f': flist,'id' :s}
   return render(request,'myrmapp/ownprofile.html',context)  
def cusprofile(request):                                    #......................problem
  if request.session.has_key('sid'):
   s=request.session['sid'] 
   #uname  = Customer.objects.filter(username=request.POST['sid'])
   flist = Customer.objects.filter(email=s)
   context = {'f': flist,'id' :s}
   return render(request,'myrmapp/cusprofile.html',context)  
def viewmassege(request):
  if request.session.has_key('sid'):
    s=request.session['sid']
    flist=Massege.objects.all()
    context={'f':flist}
    return render(request,'myrmapp/viewmassege.html',context)

def delcat(request,f_id):
  flist = Category.objects.get(pk=f_id)
  return render(request, 'myrmapp/delcat.html', {'f': flist})
def deletecatcode(request):
  q = Category.objects.get(pk=request.POST['txtid'],category_name=request.POST['txtuser'])
  q.delete()
  return HttpResponseRedirect("/myrmapp/viewcat") 
def delsubcat(request,f_id):
  flist = Sub_category.objects.get(pk=f_id)
  return render(request, 'myrmapp/delsubcat.html', {'f': flist})
def deletesubcatcode(request):
  q = Sub_category.objects.get(pk=request.POST['txtid'],subcategory_name=request.POST['txtuser'])
  q.delete()
  return HttpResponseRedirect("/myrmapp/viewsubcat") 
def delroom(request,f_id):
  q = Roomdetails.objects.get(pk=f_id)
  q.delete()
  return HttpResponseRedirect("/myrmapp/viewroom") 
def deletecus(request,f_id):
  flist = Customer.objects.get(pk=f_id)
  return render(request, 'myrmapp/deletecus.html', {'f': flist})
def deletecusdata(request):
  q = Customer.objects.get(pk=request.POST['txtid'],username=request.POST['txtuser'],email=request.POST['email'])
  q.delete()
  return HttpResponseRedirect("/myrmapp/viewcustomer") 
def delrmbook(request,f_id):
  q = Roombook.objects.get(pk=f_id)
  q.delete()
  return HttpResponseRedirect("/myrmapp/viewbookedroom")
def deletemsg(request,f_id):
  q=Massege.objects.get(pk=f_id)
  q.delete()
  return HttpResponseRedirect("/myrmapp/viewmassege")
def editroom(request,f_id):
  flist = Roomdetails.objects.get(pk=f_id)
  return render(request, 'myrmapp/editroom.html', {'f': flist})
def editroomcode(request):
  q = Roomdetails.objects.get(pk=request.POST['id'])
  q.ownemail=request.POST['ownemail']
  q.roomtitle=request.POST['roomtitle']
  q.roomdetails=request.POST['roomdetails']
  q.category=request.POST['category']
  q.subcategory=request.POST['subcategory']
  q.roomimg=request.POST['roomimg']
  q.landmark=request.POST['landmark']
  q.adddate=request.POST['adddate']
  q.price=request.POST['price']
  q.city=request.POST['city']
  q.status=request.POST['status']
  q.save()
  r="update Room successfully"
  return render(request,'myrmapp/editroom.html',{"result":r}) 
def editcus(request,f_id):
  flist = Customer.objects.get(pk=f_id)
  return render(request, 'myrmapp/editcus.html', {'f': flist})
def custupdcode(request):
  q = Customer.objects.get(pk=request.POST['txtid'])
  q.username=request.POST['txtuser']
  q.email=request.POST['email']
  q.password=request.POST['password']
  q.mobile=request.POST['mobile']
  q.address=request.POST['address']
  q.country=request.POST['country']
  q.state=request.POST['state']
  q.city=request.POST['city']
  q.reg_date=request.POST['regdate']
  q.save()
  r="update Record successfully"
  return render(request,'myrmapp/editcus.html',{"result":r})

def searchcusdata(request):
 flist = Customer.objects.filter(username=request.POST["txtuser"])
 context = {'f': flist} 
 return  render(request,'myrmapp/searchcusdata.html',context)
def searchroomloc(request):
  city = Roomdetails.objects.values("city").distinct()
  land =Roomdetails.objects.values("landmark").distinct()
  category =Roomdetails.objects.values("category").distinct()
  subcat=Sub_category.objects.values("subcategory_name").distinct()
  context = {'f': city,'l':land,'cat':category,'sc':subcat}
  return render(request,'myrmapp/searchroomloc.html',context)
def searchroomlocdata(request):
 flist = Roomdetails.objects.filter(city=request.POST["city"]).filter(landmark=request.POST["landmark"]).filter(category=request.POST["category"])
 context = {'f': flist} 
 return  render(request,'myrmapp/searchroomdata.html',context)
def serchroom(request):
 flist = Roomdetails.objects.filter(landmark=request.POST["landmark"]) or Roomdetails.objects.filter(city=request.POST["landmark"])
 context = {'f': flist} 
 return  render(request,'myrmapp/searchroomdata.html',context)
def serchcity(request):
  flist=Roomdetails.objects.filter(city=request.POST["city"])
  context={'f':flist}
  return render(request,'myrmapp/serchcity.html',context)
def booking(request,f_id):
  request.session['rid']=f_id
  return HttpResponseRedirect("/myrmapp/login")
def bookconf(request,f_id):
  flist = Roomdetails.objects.get(pk=f_id)
  if request.session.has_key('sid'): 
   s=request.session['sid']
   r=request.session['rid']
   data=Roomdetails.objects.filter(id=r)

   return render(request,'myrmapp/bookconf.html',{"uname" : s,"flist":data})
def bookingdone(request):
 s = Roombook(roomid=request.POST['txtloc'],customerid=request.POST['uname'],mobile=request.POST['mobile'],bookdate=request.POST['date'])
 s.save()
 m=request.POST['mobile']
 res="Room booking successfully"
 msg="http://api.mVaayoo.com/mvaayooapi/MessageCompose?user=poonamchandramca@gmail.com:8962269272&senderID=TEST SMS&receipientno="+m+"&msgtxt=Booking done&state=4"
 context={"result":res,"massage":msg}
 return HttpResponseRedirect(msg,{"result":res})
 #return render(request,"myrmapp/bookconf.html",context)
def payment(request):
  return HttpResponseRedirect("https://www.sandbox.paypal.com/webapps/hermes?token=3NU22970P6946022P&useraction=commit&mfid=1528087064458_2ec58187882d5")

def massage(request):
  s=Massege(name=request.POST['name'],phone=request.POST['phone'],email=request.POST['email'],description=request.POST['describe'])
  s.save()
  res="Massege hasbeen sent successfully!"
  return render(request, 'myrmapp/index.html',{'resultmsg':res})

def sendmail(request):
  s=Mail(email=request.POST['email'])
  s.save()
  res="Mail hasbeen sent successfully!"
  return render(request,'myrmapp/index.html',{'result':res}) 

def forgotpass(request,f_id):
  flist = Ownerreg.objects.get(pk=f_id)
  return render(request, 'myrmapp/forgotpass.html', {'f': flist})
def forgotpasscode(request):
  q = Ownerreg.objects.get(pk=request.POST['id'])
  q.email=request.POST['email']
  q.password=request.POST['password']
  q.save()
  res="Password hasbeen Change successfully!"
  return render(request,'myrmapp/forgotpass.html',{'result':res}) 
def cforgotpass(request,f_id):
  flist = Customer.objects.get(pk=f_id)
  return render(request, 'myrmapp/cforgotpass.html', {'f': flist})
def cforgotpasscode(request):
  q = Customer.objects.get(pk=request.POST['id'])
  q.email=request.POST['email']
  q.password=request.POST['password']
  q.save()
  res="Password hasbeen Change successfully!"
  return render(request,'myrmapp/cforgotpass.html',{'result':res}) 