from django.urls import path

from Gradebook.views import index

urlpatterns = [

    path('', index, name='home'),


]
