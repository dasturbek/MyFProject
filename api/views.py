from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from .serializers import PostModelSerializer,AuthorSerializer
from home.models import  PostModel
from .permissions import IsOwnerOrReadOnly

# this is not using
class PostApiViewSet(viewsets.ModelViewSet):
    queryset = PostModel.objects.all()
    serializer_class = PostModelSerializer
 # 

   
class AuthorApiViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = AuthorSerializer

@api_view(['GET', 'DELETE'])
def get(request):
    print(request.user)
    queryset = PostModel.objects.all().order_by('-id')
    postserializer = PostModelSerializer(queryset, many=True)

    if request.method == 'DELETE':
        queryset.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    if request.method == 'GET':
        return Response(postserializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def detail(request, pk):
    try:
        queryset = PostModel.objects.get(pk=pk)
        postserializer = PostModelSerializer(queryset)
        return Response(postserializer.data)
    except ObjectDoesNotExist:
        return Response({'status': status.HTTP_404_NOT_FOUND})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def post(request):
    serializer_data = PostModelSerializer(data=request.data)
    # if PostModel.objects.filter(serializer_data).exists():
    #     return Response(status=status.HTTP_403_FORBIDDEN)
    if serializer_data.is_valid():
        serializer_data.save()
        return Response(serializer_data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['PUT',"GET"])
@permission_classes([IsAuthenticated, IsOwnerOrReadOnly])
def put(request, pk):
    try:
        queryset = PostModel.objects.get(pk=pk)
        if request.method == "GET":
            postserializer = PostModelSerializer(queryset)
            return Response(postserializer.data)
        if request.method == "PUT":
            serializer_data = PostModelSerializer(instance=queryset, data=request.data)
            if serializer_data.is_valid():
                serializer_data.save()
                return Response(serializer_data.data)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
    except ObjectDoesNotExist:
        return Response({'status': status.HTTP_404_NOT_FOUND})
        
@api_view(['PATCH', 'GET'])
@permission_classes([IsAuthenticated, IsOwnerOrReadOnly])
def patch(request, pk):
    try:
        queryset = PostModel.objects.get(pk=pk)
        if request.method == "GET":
            postserializer = PostModelSerializer(queryset)
            return Response(postserializer.data)
        if request.method == "PATCH":
            print(request.data)
            serializer_data = PostModelSerializer(instance=queryset, data=request.data, partial=True)
            if serializer_data.is_valid():
                serializer_data.save()
                return Response(serializer_data.data)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
    except ObjectDoesNotExist:
        return Response({'status': status.HTTP_404_NOT_FOUND})

@api_view(['DELETE', 'GET'])
@permission_classes([IsAuthenticated, IsOwnerOrReadOnly])
def delete(request, pk):
    try:
        queryset = PostModel.objects.get(pk=pk)   
        if request.method == 'DELETE':
            queryset.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        else:
            postserializer = PostModelSerializer(queryset)
            return Response(postserializer.data)
    except ObjectDoesNotExist:
        return Response({'status': status.HTTP_404_NOT_FOUND})