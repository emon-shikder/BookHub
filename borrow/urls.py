from django.urls import path, include
from borrow.views import borrowView,returnView
urlpatterns = [
   path("Borrow/<int:id>/",borrowView,name='borrow'),
   path("Return/<int:id>/",returnView,name='return'),
]