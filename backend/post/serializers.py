from .models import Posts, Category, Comments, Bookmarks
from rest_framework import serializers

"""
NOTE: here we are defining depth for the serializer to get the nested data ,
its only required when the model has some foreign key/one-to-one/one-to-many/many-to-many relationships
"""


# The CategorySerializer class does not require defining depth as there are no external relationships.
class CategorySerializer(serializers.ModelSerializer):
    """here no need to define  depth as no external relationship is there"""

    class Meta:
        model = Category
        fields = "__all__"


# The PostsSerializer class defines depth based on request method for handling relationships in the model.
class PostsSerializer(serializers.ModelSerializer):
    """here we are defining depth as the model has some foreign key/one-to-one/one-to-many/many-to-many relationships"""

    class Meta:
        model = Posts
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(PostsSerializer, self).__init__(
            *args, **kwargs
        )  # calling the parent class constructor
        request = self.context.get(
            "request"
        )  # getting the request object from the context
        if request and request.method == "POST":  # checking the request method
            self.Meta.depth = 0  # setting the depth to 0 for POST request
        else:
            self.Meta.depth = 1  # setting the depth to 1 for other types of request (#! we may need to change this later)


# The CommentsSerializer class defines depth based on request method for handling relationships in the model.
class CommentsSerializer(serializers.ModelSerializer):
    """here we are defining depth as the model has some foreign key/one-to-one/one-to-many/many-to-many relationships"""

    class Meta:
        model = Comments
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(CommentsSerializer, self).__init__(
            *args, **kwargs
        )  # calling the parent class constructor
        request = self.context.get(
            "request"
        )  # getting the request object from the context
        if request and request.method == "POST":  # checking the request method
            self.Meta.depth = 0  # setting the depth to 0 for POST request
        else:
            self.Meta.depth = 1  # setting the depth to 1 for other types of request (#! we may need to change this later)


# The BookmarksSerializer class defines depth based on request method for handling relationships in the model.
class BookmarksSerializer(serializers.ModelSerializer):
    """here we are defining depth as the model has some foreign key/one-to-one/one-to-many/many-to-many relationships"""

    class Meta:
        model = Bookmarks
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(BookmarksSerializer, self).__init__(
            *args, **kwargs
        )  # calling the parent class constructor
        request = self.context.get(
            "request"
        )  # getting the request object from the context
        if request and request.method == "POST":  # checking the request method
            self.Meta.depth = 0  # setting the depth to 0 for POST request
        else:
            self.Meta.depth = 1  # setting the depth to 1 for other types of request (#! we may need to change this later)


# a normal serialzer for checking
class AuthorStats(serializers.Serializer):
    views = serializers.IntegerField(default=0)
    posts = serializers.IntegerField(default=0)
    likes = serializers.IntegerField(default=0)
    bookmarks = serializers.IntegerField(default=0)
