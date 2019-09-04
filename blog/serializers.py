from .models import Article
from rest_framework import serializers

class ArticleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Article
        # fields = ('title', 'brief_content', 'content')
        fields = '__all__'



    # def create(self, validated_data):
    #     return Article.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.save()
    #     return instance

