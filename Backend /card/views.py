from .models import CardDetail
from .serializers import CardSerializers, CardDetailSerializers
from rest_framework.generics import ListAPIView, CreateAPIView,RetrieveUpdateAPIView,RetrieveAPIView

from django.shortcuts import get_object_or_404

# Create your views here.

class CardList(ListAPIView):
    queryset = CardDetail.objects.all()
    serializer_class = CardSerializers


class CardCreate(CreateAPIView):
    queryset = CardDetail.objects.all()
    serializer_class = CardSerializers


class CardUpdate(RetrieveUpdateAPIView):
    serializer_class = CardSerializers
    lookup_field = 'slug'

    def get_object(self):
        slug = self.kwargs['slug']
        return get_object_or_404(CardDetail, slug=slug)

    def put(self,request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class CardDetails(RetrieveAPIView):
    serializer_class = CardDetailSerializers
    lookup_field  = 'slug'

    def get_object(self):
        slug = self.kwargs['slug']
        return get_object_or_404(CardDetail, slug=slug)