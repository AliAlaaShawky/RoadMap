from django.urls import path
from . import views
urlpatterns = [
path('<str:course_name>/<int:start>',views.cv,name='cv'),
path('<int:start>/<str:course_name>',views.trackcv,name='trackcv'),

]