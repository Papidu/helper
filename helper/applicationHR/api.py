#from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view #permission_classes #Views DRF
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import User, Summary, Cards
from .serializers import UserSerializer, SummarySerializer, CardsSerializer, RegistrationSerializer
from rest_framework import permissions


@api_view(['POST',])
#@permission_classes((AllowAny))
def registratioUser_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = "successfully registered a new user."
            data['phone'] = user.phone
            data['username'] = user.username
            data['password'] = user.password
            token = Token.objects.get(user=user).key
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data)

class UserList(APIView):
    #permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        model = User.objects.all()
        serializer = UserSerializer(model, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
class SummaryList(APIView):
    #permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        model = Summary.objects.all()
        serializer = SummarySerializer(model, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SummarySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
class CardsList(APIView):
    #permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        model = Summary.objects.all()
        serializer = CardsSerializer(model, many=True)
        return Response(serializer.data)

class PersonalList( APIView ):
    #permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        model = User.objects.all()
        serializer = UserSerializer(model, many=True)
        return Response(serializer.data)



class UserDetail(APIView):
    #permission_classes = [permissions.IsAuthenticated]
    def get_user(self, username):
        try:
            model = User.objects.get(id=username)
            return model
        except User.DoesNotExist:
            return Response(f'User with {username} is not found on database', status=status.HTTP_404_NOT_FOUND)

    def get(self, request, phone):
        if not self.get_user(phone):
            Response(f'User with {phone} is not found on database', status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(self.get_user(phone))
        return Response(serializer.data)

    def post(self, request, phone):
        if not self.get_user(phone):
            Response(f'User with {phone} is not found on database', status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(self.get_user(phone), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def delete(self, request, employee_id):
        if not self.get_user(employee_id):
            Response(f'User with {employee_id} is not found on database', status=status.HTTP_404_NOT_FOUND)
        model = self.get_user(employee_id)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)