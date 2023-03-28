from django.http import JsonResponse
from .models import Post
from .serializers import PostSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def posts_list(request):
    posts = Post.objects.all()
    serialize = PostSerializer(posts, many=True)
    return JsonResponse(serialize.data, safe=False)

@api_view(['POST'])
def add_post(request):
    serialize = PostSerializer(data=request.data)
    if serialize.is_valid():
        serialize.save()
        return Response(serialize.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialize.errors)
    
@api_view(['GET'])
def getpost(request, pk):
    try:
        singlepost = Post.objects.get(pk=pk)
        serialize = PostSerializer(singlepost)
        return Response(serialize.data)
    except Post.DoesNotExist:
        return Response({'error':'Id not found in DB'})
        
@api_view(['PUT'])
def editpost(request, pk):    
        singlepost = Post.objects.get(pk=pk)
        serialize = PostSerializer(singlepost, data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        else:
            return Response(serialize.errors)
        
@api_view(['DELETE'])
def deletepost(request, pk):    
        singlepost = Post.objects.get(pk=pk)
        singlepost.delete()
        return Response({'deleted': True})

@api_view(['GET'])
def search(request):
    query = request.GET['search']
    posts = Post.objects.filter(title__icontains=query)
    serialize = PostSerializer(posts, many=True)
    return JsonResponse(serialize.data, safe=False)