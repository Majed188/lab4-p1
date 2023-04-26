from django.urls import path
from tax.views import default1,calculate,therate
urlpatterns= [
path("",default1,name="empty"),
path("taxrate",therate,name="rate"),
path("<str:num>",calculate,name="cal")



]
