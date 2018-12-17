from django.urls import path
from basic_app import views

# SET THE NAMESPACE!
app_name = 'bs'

urlpatterns=[
    path(r'relative/',views.relative,name='relative'),
    path(r'other/',views.other,name='other'),
]
