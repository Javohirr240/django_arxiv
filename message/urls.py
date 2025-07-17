from django.urls import path
from .views import IndexView, ContactPageView, Xabarlar
urlpatterns = [
  path('', ContactPageView.as_view(), name='index'),
  path('xabarlar/', Xabarlar.as_view(), name='list'),
]