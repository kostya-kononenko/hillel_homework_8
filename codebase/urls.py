from codebase.views import crud_list, form

from django.urls import path


app_name = "codebase"
urlpatterns = [
    path('', crud_list, name='index'),
    path('<int:age>/', crud_list, name='crud-filter'),
    path('form/', form, name='form'),

]
