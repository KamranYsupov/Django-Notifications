from rest_framework import serializers

from news.models import News


class NewsSerializer(serializers.ModelSerializer):
    author_username = serializers.SerializerMethodField()

    @staticmethod
    def get_author_username(obj):
        return obj.author.username

    class Meta:
        model = News
        fields = [
            'id',
            'title',
            'content',
            'author_username',
            'time_create'
        ]