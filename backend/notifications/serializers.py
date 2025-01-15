from .models import Notifications
from rest_framework import serializers

"""
NOTE: here we are defining depth for the serializer to get the nested data ,
its only required when the model has some foreign key/one-to-one/one-to-many/many-to-many relationships
"""


# The NotificationsSerializer class defines depth based on request method for handling relationships in the model.
class NotificationsSerializer(serializers.ModelSerializer):
    """here we are defining depth as the model has some foreign key/one-to-one/one-to-many/many-to-many relationships"""

    class Meta:
        model = Notifications
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(NotificationsSerializer, self).__init__(
            *args, **kwargs
        )  # calling the parent class constructor
        request = self.context.get(
            "request"
        )  # getting the request object from the context
        if request and request.method == "POST":  # checking the request method
            self.Meta.depth = 0  # setting the depth to 0 for POST request
        else:
            self.Meta.depth = 1  # setting the depth to 1 for other types of request (#! we may need to change this later)
