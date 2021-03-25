
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("pavan", views.pavan, name="pavan"),
    #path("<str:name>", views.greet, name="greet"),
    path("helloHTML", views.hello_from_htmlpage, name="hello_html"),
    path("<str:name>", views.greeting, name="greeting"),

]