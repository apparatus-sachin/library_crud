from django.urls import path
from . import views

urlpatterns=[
path("",views.library_add,name='library_add'),
path("library_list",views.library_list,name='library_list'),
path("libray_edit/<int:id>",views.library_edit,name='library_edit'),
path("library_update/<int:id>",views.library_update,name='library_update'),
path("library_trash/<int:id>",views.library_trash,name='library_trash')

]