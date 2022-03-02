from .models import Article
from rest_framework import serializers


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'author', 'email', 'date']


# Default Serializer
"""    def create(self, validated_data):
        return Article.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.title)
        instance.email = validated_data.get('email', instance.title)
        instance.date = validated_data.get('date', instance.title)
        instance.save()
        return instance"""


