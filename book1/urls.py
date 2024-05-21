from django.urls import path
from . import views

urlpatterns =[
    path('' , views.web ,name='web'),
    path('login.htm',views.login , name='login'),
    path('sem21.htm',views.sem21, name='sem21'),
    path('sem22.htm',views.sem22, name='sem22'),
    path('sem31.htm',views.sem31 , name='sem31'),
    path('sem32.htm',views.sem32 , name='sem32'),
    path('sem41.htm',views.sem41 , name='sem41'),
    path('sem42.htm',views.sem42 , name='sem42'),
    path('semi21.htm',views.semi21 , name='semi21'),
    path('semi22.htm',views.semi22 , name='semi22'),
    path('semi31.htm',views.semi31 , name='semi31'),
    path('semi32.htm',views.semi32 , name='semi32'),
    path('semi41.htm',views.semi41 , name='semi41'),
    path('semi42.htm',views.semi42 , name='semi42'),
    path('seme21.htm',views.seme21 , name='seme21'),
    path('seme22.htm',views.seme22 , name='seme22'),
    path('seme31.htm',views.seme31 , name='seme31'),
    path('seme32.htm',views.seme32 , name='seme32'),
    path('seme41.htm',views.seme41 , name='seme41'),
    path('seme42.htm',views.seme42 , name='seme42'),
    path('logout.htm',views.logout , name='logout'),
    path('about.htm',views.about,name='about'),
    path('first.htm',views.first ,name='first'),
    
    

]