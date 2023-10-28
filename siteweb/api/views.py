from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from siteweb.api.serialzers import MessageSerializer, MessageDeSerializer
from siteweb.models import Message, User, Category


@api_view(['GET'])
def get_messages(request):
    messages = Message.objects.all()
    serialized_messages = MessageSerializer(messages, many=True)
    return Response(serialized_messages.data)


@api_view(['GET'])
def get_message(request, id):
    message = Message.objects.get(id=id)
    serialized_message = MessageSerializer(message, many=False)

    return Response(serialized_message.data)


@permission_classes([IsAuthenticated])
@api_view(['POST'])
def new_message(request):
    if request.method == 'POST':
        newMessage = Message()
        user = request.user.id
        newMessage.author = User.objects.get(id=user)
        message = MessageDeSerializer(instance=newMessage, data=request.data)
        print(user)

        if message.is_valid():
            message.save()
            return Response(message.data)
    return Response('error')
