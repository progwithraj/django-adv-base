from customUser.models import CustomUser
from rest_framework.response import Response


# Create your views here.
def index(request):
    user_posts = CustomUser.objects.prefetch_related("posts").last()
    return Response(data=user_posts)
