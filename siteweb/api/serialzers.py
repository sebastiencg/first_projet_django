from rest_framework.serializers import ModelSerializer

from siteweb.models import Message, Category, User


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class MessageSerializer(ModelSerializer):
    category = CategorySerializer()
    author = UserSerializer()

    class Meta:
        model = Message
        fields = '__all__'
