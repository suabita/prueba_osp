from django.urls import path
from prueba.views import PruebaListView, PruebaCreateView, PruebaDetailView, PruebaUpdateView

app_name = 'prueba'

urlpatterns = [
    path('principal', PruebaListView.as_view(), name='principal'),
    path('create', PruebaCreateView.as_view(), name='create'),
    path('detail/<pk>', PruebaDetailView.as_view(), name='detail'),
    path('update/<pk>', PruebaUpdateView.as_view(), name='update'),
]
