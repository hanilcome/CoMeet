from django.urls import path
from . import views

app_name = 'commit'

urlpatterns = [
    path('<int:id>', views.detail, name='detail_view'),
    path('edit/<int:id>', views.edit_view, name='edit_view'),
]
