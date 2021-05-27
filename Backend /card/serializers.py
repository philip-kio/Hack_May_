from rest_framework import serializers
from .models import CardDetail



class CardSerializers(serializers.ModelSerializer):
    
    class Meta:
        model= CardDetail
        fields = '__all__'
        lookup_field = 'slug'
        extra_kwargs ={
            'url': {'lookup_field':'slug'}
        }


class CardDetailSerializers(serializers.ModelSerializer):
    
    class Meta:
        model= CardDetail
        fields = (  
            "first_name",
            "last_name",
            "slug",
            "employment_title",
            "company",
            "email",
            "brief_description",
            "linkedIn"
        )
        lookup_field = 'slug'
        extra_kwargs ={
            'url': {'lookup_field':'slug'}
        }
