from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('log_in/', views.log_in_view, name='log_in'),
    path('log_out/', views.log_out_view, name='log_out'),
    path('sign_up/', views.sign_up_view, name='sign_up'),
    path('my_page/<int:id>', views.my_page_view, name='my_page'),
]