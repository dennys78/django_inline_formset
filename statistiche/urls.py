from django.urls import path

from .views import (
    GiornalieroList, GiornalieroCreate, GiornalieroUpdate,
    delete_image, delete_dettaglio
)

app_name = 'statistiche'

urlpatterns = [
    path('', GiornalieroList.as_view(), name='list_giornaliero'),
    path('statistiche/create/', GiornalieroCreate.as_view(), name='create_giornaliero'),
    path('statistiche/update/<int:pk>/', GiornalieroUpdate.as_view(), name='update_giornaliero'),
    path('delete-image/<int:pk>/', delete_image, name='delete_image'),
    path('delete-dettaglio/<int:pk>/', delete_dettaglio, name='delete_dettaglio'),
]