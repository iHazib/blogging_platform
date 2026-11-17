from rest_framework import serializers
from .models import Post

# serialization is the process to convert model instances into JSON format to be sent over the network. 

class PostSerializer(serializers.ModelSerializer): # ModelSerializer can fetch all the fields of the model on it's own, and we can also specify the fields to be serialized.

    # this is not a model field, but only to show the username of the author instead of the author id.
    author_username = serializers.ReadOnlyField(source='author.username') 

    class Meta:
        model = Post

        # fields visible to frontend, added author_username in this.
        fields = ['id', 'title', 'content', 'publication_date', 'author', 'author_username'] # fields to be serialized.

        read_only_fields = ['author', 'publication_date'] # immutable fields from the frontend. They are set through the backend directly.

