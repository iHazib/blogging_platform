from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from .serializers import PostSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from .permissions import IsWriterOrReadOnly


# def hello_world(request):
#     return render(request, 'articles/article_text.html')


# class PostViewSet(viewsets.ModelViewSet):
#     queryset = Post.objects.all().order_by('-publication_date')
#     serializer_class = PostSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]

#     def perform_create(self, serializer):
#         if self.request.user.role != 'writer':
#             raise PermissionDenied("Only writer can create posts.")
#         serializer.save(author=self.request.user)

#     def perform_update(self, serializer):
#         if self.request.user.role != 'writer' or serializer.instance.author != self.request.user:
#             raise PermissionDenied("You cannot delete someone else post")   



# @api_view(['GET', 'POST']) # a decorator to specify that this view can handle GET and POST requests. # model viewsets
# def post_list_create(request): 

#     if request.method == 'GET':
#         posts = Post.objects.all().order_by('-publication_date') # ordering the posts by publication date.
#         serializer = PostSerializer(posts, many=True) # here many=True is used to specify that we are serializing multiple objects.
#         return Response(serializer.data)

#     elif request.method == 'POST':

#         if not request.user.is_authenticated: # checking if the user is authenticated or not. If not, return a 401.
#             return Response({'error': 'Authentication required'}, status=status.HTTP_401_UNAUTHORIZED)

#         if request.user.role != 'writer': # checking if the user is a writer or not. If not, return a 403. 
#             return Response({'error': 'Only writers can create posts'}, status=status.HTTP_403_FORBIDDEN)

#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid(): # runs checks on the data sent from the frontend to see if it is valid or not. 
#             serializer.save(author=request.user) # the author is the user sending the request, so we set the author field to the current user. 
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# @api_view(['GET', 'PUT', 'DELETE'])
# def post_detail(request, pk): # pk is the primary key of the post we want to retreive, update or delete.
#     try:
#         post = Post.objects.get(pk=pk) # getting the post through pk, if pk does not exist, it throws the exception.
#     except Post.DoesNotExist:
#         return Response({"error": "Post not found!"}, status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET': 
#         serializer = PostSerializer(post) # converting the post obj into JSON.
#         return Response(serializer.data)

#     elif request.method == 'PUT': 
#         if not request.user.is_authenticated or request.user.role != 'writer' or post.author != request.user: # checking if the user is authenticated, is a writer and author of the post. 
#             return Response({"error": "Only the author can edit this post"}, status=status.HTTP_403_FORBIDDEN)

#         serializer = PostSerializer(post, data=request.data) # request data is the edited data sent from the frontend. We here are updating the edited data as original data. 
#         if serializer.is_valid(): # checks is valid or not. 
#             serializer.save() 
#             return Response(serializer.data) # returns the updated post data.
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         # checking if the user is authenticated, is a writer and author of the post. If not, return a 403.

#         if not request.user.is_authenticated or request.user.role != 'writer' or post.author != request.user:
#             return Response({"error": "Only the author can delete this post"}, status=status.HTTP_403_FORBIDDEN)
        
#         post.delete()
#         return Response({"message": "Post deleted successfully!"}, status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET'])
# def my_posts(request):
#     if not request.user.is_authenticated:
#         return Response({"message": "User not logged in."}, status=status.HTTP_401_UNAUTHORIZED)

#     posts = Post.objects.filter(author=request.user).order_by('-publication_date')

#     serializer = PostSerializer(posts, many=True)

#     return Response(serializer.data)

class PostViewSet(viewsets.ModelViewSet):
    
    queryset = Post.objects.all().order_by('-publication_date') # getting all posts in the queryset.
    
    serializer_class = PostSerializer 
    
    permission_classes = [IsWriterOrReadOnly] # deployed gatekeeper class here for all the checks happening beforehand. 

    def perform_create(self, serializer):
        # there are no security checks here

        serializer.save(author=self.request.user)   # saving the logged in user as author.     