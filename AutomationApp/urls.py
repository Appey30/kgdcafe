from django.urls import path
from . import views

app_name = "AutomationApp"
urlpatterns = [

#path('add',views.addproduct, name='addprod.html'), 
#path('/<str:prodd_id>', views.dproduct , name='deleteprod'),
path('<int:del_id>', views.delprod , name='delprod'),
path('edit/<int:edit_id>', views.editprod , name='editprod'),
]
