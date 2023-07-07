from  rest_framework import serializers
from custom_app.models import Post,Author

class PostSerializer(serializers.ModelSerializer):
    author_name = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = ['id','author','blog','created','author_name','updated']
       
    def get_author_name(self,obj):
            #import pdb;pdb.set_trace()
        
        return f"{obj.author}"
            #author = Author.objects.get(author__id=obj.author)