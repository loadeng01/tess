from django.shortcuts import render
from post.models import Post
#
#
def posts_list(request):
    queryset = Post.objects.all()
    return render(request, 'listing.html', {'posts': queryset})
#
#
# def get_hel(request):
#     return render(request, 'hello.html')
#
#
# # REST
#
#
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .models import Post
# from .serializers import PostSerializer
# from django.shortcuts import get_object_or_404
#
#
# @api_view(['GET'])
# def posts_list_api_view(request):
#     queryset = Post.objects.all()
#     serializer = PostSerializer(queryset, many=True)
#     return Response(serializer.data)
#
#
# @api_view(['GET'])
# def post_details_api_view(request, id):
#     post = get_object_or_404(Post, id=id)
#     serializer = PostSerializer(post)
#     return Response(serializer.data)
#     # try:
#     #     post = Post.objects.get(id=id)
#     #     serializer = PostSerializer(post)
#     # except Post.DoesNotExist:
#     #     return Response('no id for this post')
#     # else:
#     #     return Response(serializer.data)
#
#
# # @api_view(['POST'])
# # def create_post_api_view(request):
# #     serializer = PostSerializer(data=request.data)
# #     serializer.is_valid(raise_exception=True)
# #     serializer.save()
# #     return Response(serializer.data, status=200)
# #
# # @api_view(['DELETE'])
# # def delete_post_api_view(request, id):
# #     post = get_object_or_404(Post, id=id)
# #     post.delete()
# #     return Response(status=204)
#
# # @api_view(['PUT'])
# # def update_post_api_view(request, id):
# #     post = get_object_or_404(Post, id=id)
# #     serializer = PostSerializer(post, data=request.data)
# #     serializer.is_valid(raise_exception=True)
# #     serializer.save()
# #     return Response(serializer.data, status=201)
# #
# #
# # @api_view(['PATCH'])
# # def update_post_api_view(request, id):
# #     post = get_object_or_404(Post, id=id)
# #     serializer = PostSerializer(post, data=request.data, partial=True)
# #     serializer.is_valid(raise_exception=True)
# #     serializer.save()
# #     return Response(serializer.data, status=201)
#
# # @api_view(['PUT', 'PATCH'])
# # def update_post_api_view(request, id):
# #     post = get_object_or_404(Post, id=id)
# #     partial = True if request.method == 'PATCH' else False
# #     serializer = PostSerializer(post, data=request.data, partial=partial)
# #     serializer.is_valid(raise_exception=True)
# #     serializer.save()
# #     return Response(serializer.data, status=201)


# from rest_framework.response import Response
# from .serializers import PostSerializer
# from django.shortcuts import get_object_or_404
# from rest_framework.views import APIView
#
#
# class PostListAPIView(APIView):
#     def get(self, request):
#         queryset = Post.objects.all()
#         serializer = PostSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#
# class PostDetailsAPIView(APIView):
#     def get(self, request, id):
#         post = get_object_or_404(Post, id=id)
#         serializer = PostSerializer(post)
#         return Response(serializer.data)
#
#
# class CreatePostAPIView(APIView):
#     def post(self, request):
#         serializer = PostSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=201)
#
#
# class DeletePostAPIView(APIView):
#     def delete(self, request, id):
#         post = get_object_or_404(Post, id=id)
#         post.delete()
#         return Response(status=204)
#
#
# class UpdatePostAPIView(APIView):
#     def put(self, request, id):
#         post = get_object_or_404(Post, id=id)
#         serializer = PostSerializer(post, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=201)
#
#     def patch(self, request, id):
#         post = get_object_or_404(Post, id=id)
#         serializer = PostSerializer(post, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=201)
    



# GenericAPIView


from rest_framework import generics
from rest_framework.response import Response
from .serializers import PostSerializer


class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailsAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'


class CreatePostAPIView(generics.CreateAPIView):
    serializer_class = PostSerializer


class DeletePostAPIView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'


class UpdatePostAPIView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        if request.method == 'PATCH':
            kwargs['partial'] = True
        super().update(request, *args, **kwargs)


# class PartialPostAPIView(generics.UpdateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     lookup_field = 'id'
#     partial = True




























