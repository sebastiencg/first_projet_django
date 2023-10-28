from rest_framework.serializers import ModelSerializer

from siteweb.models import Message, Category, User, Response


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class ResponseSerializer(ModelSerializer):
    class Meta:
        model = Response
        fields = ['id', 'content', 'author']

    author = UserSerializer()


class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

    category = CategorySerializer()
    author = UserSerializer()
    responses = ResponseSerializer(many=True)


class MessageDeSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

