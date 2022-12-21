from django.urls import path
from . import views
urlpatterns = [
path('<str:start_name>/<int:start_id>',views.begin,name='begin'),
path('<int:begin_id>/<str:begin_name>',views.trackbegin,name='trackbegin'),
path('mycv',views.mycv,name='mycv'),
]