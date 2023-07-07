from django.shortcuts import render
from custom_app.models  import Post,Author
# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from custom_app.serializers import PostSerializer
from rest_framework import status
class PostData(APIView):
    def get(self,request,author_fk=None,post_pk=None,*args, **kwargs):
        if author_fk is not None:
            queryset = Post.objects.filter(author=author_fk)
            serializer = PostSerializer(queryset,many=True).data
            
            return Response(serializer)
        
        if post_pk is not None:
            try:
                queryset = Post.objects.get(id=post_pk)
            except Post.DoesNotExist:
                print("Data Not Exist")
            
            else:
                serializer = PostSerializer(queryset).data
                return Response(serializer)
    #USE FOR PATCH METHOD
    def post(self,request,post_pk,*args, **kwargs):
        instance = Post.objects.get(id=post_pk)
        if request.data.get('delete') == 'delete':
           instance.delete()
           return Response('Data Deleted',status=status.HTTP_200_OK)
        else:
            serializer = PostSerializer(instance,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
   
        

    
    

            
            
            
