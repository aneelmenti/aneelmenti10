from . import views
from django.urls import path
app_name='mimapp'
urlpatterns = [
path('html', views.htmldisplay),
path('xml', views.xmldisplay),
path('excel', views.exceldisplay),

]