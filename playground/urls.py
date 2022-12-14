from django.urls import path
from . import views

#  A URLConf module
urlpatterns = [
    path('hello/', views.say_hello),
    path('numbers/', views.numbers)

]

# now we need to import url into main url
# in storefront urls.py