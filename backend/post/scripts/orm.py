from colorama import Fore
from django.db.models.base import connection
from post.models import Category
from customUser.models import CustomUser


def run():
    # posts = Posts.objects.all()
    # print(Fore.RED + f"posts: {posts[0].__dict__}")
    # user = CustomUser.objects.filter(id=8).prefetch_related("posts").first()
    # user = CustomUser.objects.filter(id=8).first()
    # print(Fore.CYAN + f"user: {user.__dict__}")
    # print(
    #     Fore.CYAN
    #     + f"user post slugs: {user.posts.all().values_list('profile', flat=True)}"
    # )
    # all users with their posts
    users = CustomUser.objects.all()
    categories = Category.objects.prefetch_related("posts").all()
    print(Fore.GREEN + f"users: {categories[0].post_counts}")
    print(
        Fore.RED
        + f"length: {len(connection.queries)} \n queries: {connection.queries}, "
    )
