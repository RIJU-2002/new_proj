from django.urls import path
from . import views

urlpatterns = [
	path('', views.ApiOverview, name='home'),
    path('create/',views.add_items,name='add-item'),
    path('view/',views.view_items,name='view'),
    path('update/<int:pk>',views.update_items,name='update'),
    path('item/<int:pk>/delete',views.delete_items,name='delete')
]
