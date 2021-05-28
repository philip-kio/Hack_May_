from django.urls import path
from .views import CardUpdate,CardCreate, CardList, CardDetails

urlpatterns=[
path('', CardList.as_view(),name='all_cards'),
path('card-create/', CardCreate.as_view(), name='create'),
path('card-update/<str:slug>/',CardUpdate.as_view(), name='update'),
path('TakeMyCard/<str:slug>/', CardDetails.as_view(), name='myCard' ),


]