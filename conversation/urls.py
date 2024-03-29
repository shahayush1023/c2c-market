from django.urls import path
from . import views

app_name = 'conversation'

urlpatterns = [
    path('',views.inbox,name='inbox'),
    path('<int:pk>/',views.detail,name='detail'),
    path('new/<int:item_pk>/',views.new_conversation,name='conversation'),
    path('delete/<int:pk>/',views.delete,name='delete')
]


