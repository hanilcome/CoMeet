from django.urls import path
from . import views

app_name = 'commit'

urlpatterns = [
     path('', views.home, name='home'),
     path('detail/', views.detail, name='detail'),
     path('detail/<int:id>', views.detail_commit, name='detail_commit'),
     path('detail/comment/<int:id>', views.detail_write_comment, name='detail_writer_comment'),
     path('detail/comment/delete/<int:id>', views.detail_delete_comment, name='detail_delete-comment'),
     path('write/', views.write_view, name='write_view'),
     path('edit/<int:id>', views.edit_view, name='edit_view'),
     path('write/delete/<int:id>', views.delete_view, name='delete_view'),
]
