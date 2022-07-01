from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import PostsSerializer
from .models import Posts

# Create your views here.
@api_view(['GET'])
def getPosts(request):
    posts = Posts.objects.all()
    serializer = PostsSerializer(posts, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def createPosts(request):
    serializer = PostsSerializer(data=request.data)
    # 클라이언트가 입력한 데이터가 유효하면, 게시글 생성(Create)
    if serializer.is_valid():
        serializer.save() # 자동으로 Create
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    # 유효하지 않은 데이터면, 400 Error 반환
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def updatePosts(request):
    print(request.data)
    posts = Posts.objects.get(pk = request.data['id'])
    serializer = PostsSerializer(posts, data=request.data)
    
    # 클라이언트가 입력한 데이터가 유효하면, 게시글 생성(Create)
    if serializer.is_valid():
        serializer.save() # update
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    # 유효하지 않은 데이터면, 400 Error 반환
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getPostById(request, post_id):
    post = Posts.objects.get(pk=post_id)
    serializer = PostsSerializer(post)
    return Response(serializer.data)

@api_view(['GET'])
def deletePost(request, post_id):
    post = Posts.objects.get(pk = post_id)
    post.delete()
    return Response({'message':'sucess', 'code' : 200})