from .views import index,add_cat,update_cat,edit_blog,delete_cat,view
from django.urls import path

urlpatterns = [
    path('', index,name="index"),
    path('add/', add_cat,name="add"),
    path('update/<cat_id>/', update_cat,name="update"),
    path('edit/<cat_id>/', edit_blog,name="edit"),
    path('view/<cat_id>/', view,name="view"),
    path('delete/<cat_id>/', delete_cat,name="delete"),
]