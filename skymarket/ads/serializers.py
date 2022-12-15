from rest_framework import serializers

from ads.models import Ad, Comment
from users.models import User


# TODO Сериалайзеры. Предлагаем Вам такую структуру, однако вы вправе использовать свою

class CommentDetailSerializer(serializers.ModelSerializer):
    author_first_name = serializers.CharField(read_only=True, source='author.first_name')
    author_last_name = serializers.CharField(read_only=True, source='author.last_name')
    author_image = serializers.CharField(read_only=True, source='author.image')
    ad = serializers.CharField(read_only=True, source='ad.id')
    author = serializers.CharField(read_only=True, source='author.id')

    class Meta:
        model = Comment
        fields = ["pk",
                  "text",
                  "author",
                  "created_at",
                  "author_first_name",
                  "author_last_name",
                  "ad",
                  "author_image"]


class CommentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['text']


class CommentDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['pk']


class AdSerializer(serializers.ModelSerializer):
    author = serializers.CharField(read_only=True, source='author.id')

    class Meta:
        model = Ad
        fields = ["image", "title", "price", "description", "author"]


class AdListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ["pk", "image", "title", "price", "description", "author"]


class AdDetailSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(read_only=True, source='author.first_name')
    last_name = serializers.CharField(read_only=True, source='author.last_name')
    phone = serializers.CharField(read_only=True, source='author.phone')

    class Meta:
        model = Ad
        fields = ["pk", "image", "title", "price", "phone", "description", "first_name", "last_name",
                  "author_id"]
        # def update(self, instance, validated_data):
        #     self.author_last_name = A


class AdDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ['id']


class AdForCurrentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ("pk", "image", "title", "price", "description")
