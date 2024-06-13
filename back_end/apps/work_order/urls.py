from django.urls import path
from .views import MttoCreateView, MttoListView, MttoDetailView

urlpatterns = [
    path('add_mtto/', MttoCreateView.as_view(), name='add_mtto'), 
    path('mtto/list/<int:vehicle_id>/', MttoListView.as_view(), name='mtto_list'), 
    path('mtto/list/<int:vehicle_id>/mtto_detail/<int:id>/', MttoDetailView.as_view(), name='mtto_detail'),
]