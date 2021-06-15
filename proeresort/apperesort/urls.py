
from . import views
from django.urls import path

urlpatterns = [
    path('',views.homee,name='homee'),
path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logins',views.logins,name='logins'),
    path('userlogin',views.userhome,name='userhome'),
    path('reg',views.reg,name='reg'),
    path('out',views.out,name='out'),


    path('base', views.base, name='base'),
    path('index', views.index, name='index'),
    path('success', views.success, name='success'),

    path('viewbookings', views.viewbookings, name='viewbookings'),
    path('adminhome',views.adminhome,name='adminhome'),
    path('addresort', views.addresort, name='addresort'),
    path('userview', views.userview, name='userview'),
    path('addre',views.addre,name='addre'),
    path('adminaddresort', views.adminaddresort, name='adminaddresort'),
    path('adminaddre',views.adminaddre,name='adminaddre'),
    path('profile', views.managerprofile, name='profile'),
    path('managerregister',views.managerregister, name='managerregister'),
    path('managerreg',views.managerreg,name='managerreg'),
    path('managerhome',views.managerhome,name='managerhome'),
    path('about',views.about,name='about'),
    path('editresort',views.editresort,name='editresort'),
    path('editfile',views.editfile,name='editfile'),
    path('update', views.update, name='update'),

    path('ser', views.ser, name='search'),
    path('aser', views.aser, name='aser'),

    path('imagegallery',views.imagegallery,name='imagegallery'),
    path('contact',views.contact,name='contact'),
    path('resortabout',views.resortabout,name='resortabout'),
    path('det',views.det,name='det'),
    path('viewresort', views.viewresort, name='viewresort'),
    path('viewmanager', views.viewmanager, name='viewmanager'),
    path('homee', views.homee, name='homee'),
    path('adminprofile', views.adminprofile, name='adminprofile'),
    path('readmore',views.readmore,name='readmore'),
    path('userprofile',views.userprofile,name='userprofile'),
    path('managerprofile',views.managerprofile,name='mangerprofile'),
    path('viewresorts', views.viewresorts, name='viewresorts'),
    path('resortmanagerview', views.resortmanagerview, name='resortmanagerview'),

    path('feedback',views.feedback,name='feedback'),
    path('resortfeedback',views.resortfeedback,name='resortfeedback'),
    path('feedbacks',views.feedbacks,name='feedbacks'),
    path('adminfeedbacks', views.adminfeedbacks, name='adminfeedbacks'),
    path('managerfeedbacks', views.managerfeedbacks, name='managerfeedbacks'),
    path('adminfeedback', views.adminfeedback, name='adminfeedback'),
    path('managerfeedback', views.managerfeedback, name='managerfeedback'),
    path('userfeedbackview', views.userfeedbackview, name='userfeedbackview'),
    path('feedbackview',views.feedbackview,name='feedbackview'),

    path('managerprofileupdate',views.managerprofileupdate,name='managerprofileupdate'),
    path('managerupdateprofile',views.managerupdateprofile,name='managerupdateprofile'),
    path('editmanagerresort',views.editmanagerresort,name='editmanagerresort'),
    path('managerupdate', views.managerupdate, name='managerupdate'),
    path('editmanagerfile',views.editmanagerfile,name='editmanagerfile'),
    path('userhome',views.userhome,name='userhome'),
    path('demo',views.demo,name='demo'),
    path('delete',views.delete, name='delete'),

    path('booknow', views.booknow, name='booknow'),
    path('book', views.book, name='book'),
    path('mybooking', views.mybooking, name='mybooking'),
    path('adminbookview',views.adminbookview,name='adminbookview'),
    path('managerbookview', views.managerbookview, name='managerbookview'),

    path('payments',views.payments, name='payments'),
    path('payment',views.payment, name='payment'),
    path('pay',views.pay, name='pay'),

    path('state',views.state,name='state'),
    path('states',views.states,name='states'),
    path('stateview', views.stateview, name='stateview'),

    path('termsconditions',views.termsconditions,name='termsconditions'),
    path('addimage', views.addimage, name='addimage'),
    path('addimg', views.addimg, name='addimg'),
    path('viewimage', views.viewimage, name='viewimage'),
    path('forgot', views.forgot, name='forgot'),
    path('forgotpassword', views.forgotpassword, name='forgotpassword'),
    path('add', views.add, name='add'),
    path('det1', views.det1, name='det1'),
    path('save', views.save, name='save'),


]
