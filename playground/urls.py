from django.urls import path
from . import views

#  A URLConf module
urlpatterns = [
    path('hello/', views.say_hello)
]

# now we need to import url into main url
# in storefront urls.py