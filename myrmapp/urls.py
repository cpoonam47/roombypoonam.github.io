from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/',views.login, name='login'),
    path('loginall/',views.loginall,name='loginall'),
    path('registration/', views.registration, name='registration'),
    path('registrationcode/',views.registrationcode, name='registrationcode'),
    path('registrationcustomer/', views.registrationcustomer, name='registrationcustomer'),
    path('registrationcustomercode/',views.registrationcustomercode, name='registrationcustomercode'),
    path('ownerdash/',views.ownerdash,name='ownerdash'),
    path('ownerlogout/',views.ownerlogout,name='ownerlogout'),
    path('custodash/',views.custodash,name='custodash'),
    path('custologout/',views.custologout,name='custologout'),

    path('addcat/',views.addcat,name='addcat'),
    path('addcatcode/',views.addcatcode, name='addcatcode'),
    path('addsubcat/',views.addsubcat,name='addsubcat'),
    path('addsubcatcode/',views.addsubcatcode, name='addsubcatcode'),
    path('addroom/',views.addroom,name='addroom'),
    path('addroomcode/',views.addroomcode, name='addroomcode'),

    path('viewcat/',views.viewcat, name='viewcat'),
    path('viewsubcat/',views.viewsubcat, name='viewsubcat'),
    path('viewroom/',views.viewroom, name='viewroom'),
    path('viewcustomer/', views.viewcustomer, name='viewcustomer'),
    path('viewowner/', views.viewowner, name='viewowner'),
    path('viewbookedroom/', views.viewbookedroom, name='viewbookedroom'),
    path('ownprofile/', views.ownprofile, name='ownprofile'),
    path('cusprofile/', views.cusprofile, name='cusprofile'),
    path('viewmassege/', views.viewmassege, name='viewmassege'),
    path('viewbookedroomc/',views.viewbookedroomc, name='viewbookedroomc'),


    path('<int:f_id>/delcat/', views.delcat, name='delcat'),
    path('deletecatcode/', views.deletecatcode, name='deletecatcode'),
    path('<int:f_id>/delsubcat/', views.delsubcat, name='delsubcat'),
    path('deletesubcatcode/', views.deletesubcatcode, name='deletesubcatcode'),
    path('<int:f_id>/delroom/', views.delroom, name='delroom'),
    path('<int:f_id>/deletecus/', views.deletecus, name='deletecus'),
    path('deletecusdata/', views.deletecusdata, name='deletecusdata'),
    path('<int:f_id>/delrmbook/', views.delrmbook, name='delrmbook'),
    path('<int:f_id>/deletemsg/',views.deletemsg, name='deletemsg'),
    

    path('<int:f_id>/editroom/', views.editroom, name='editroom'),
    path('editroomcode/', views.editroomcode, name='editroomcode'),
    path('<int:f_id>/editcus/', views.editcus, name='editcus'),
    path('custupdcode/', views.custupdcode, name='custupdcode'),



    path('searchcusdata/', views.searchcusdata, name='searchcusdata'),
    path('searchroomloc/', views.searchroomloc, name='searchroomloc'),
    path('searchroomlocdata/',views.searchroomlocdata, name='searchroomlocdata'),
    path('serchroom/',views.serchroom, name='serchroom'),
    path('serchcity/',views.serchcity, name='serchcity'),

    path('<int:f_id>/booking/', views.booking, name='booking'),
    path('<int:f_id>/bookconf/', views.bookconf, name='bookconf'),
    path('bookingdone/', views.bookingdone, name='bookingdone'),
    path('payment/', views.payment, name='payment'),

    path('massage/',views.massage, name='massage'),
    path('sendmail/',views.sendmail, name='sendmail'),
    path('<int:f_id>/replysms/',views.sendmail, name='replysms'),

    path('<int:f_id>/forgotpass/',views.forgotpass, name='forgotpass'),
    path('forgotpasscode/',views.forgotpasscode, name='forgotpasscode'),
    path('<int:f_id>/cforgotpass/',views.cforgotpass, name='cforgotpass'),
    path('cforgotpasscode/',views.cforgotpasscode, name='cforgotpasscode'),
]
