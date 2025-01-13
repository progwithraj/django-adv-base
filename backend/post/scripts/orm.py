from colorama import Fore
from customUser.models import CustomUser
from django.db import models
from django.db.models.base import connection
from post.models import Category


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
    # users = CustomUser.objects.all()
    categories = Category.objects.prefetch_related("posts").all()
    # i want to find the category which has the most posts
    categories_with_most_posts = (
        Category.objects.annotate(all_post_counts=models.Count("posts"))
        .order_by("-all_post_counts")
        .first()
    )
    print(Fore.CYAN + f"categories_with_most_posts: {categories_with_most_posts}")
    print(Fore.GREEN + f"users: {categories[0].post_counts}")
    # user with most posts
    user_with_most_posts = (
        CustomUser.objects.annotate(all_post_counts=models.Count("posts"))
        .order_by("-all_post_counts")
        .first()
    )
    print(Fore.RED + f"user_with_most_posts: {user_with_most_posts}")
    print(
        Fore.RED
        + f"length: {len(connection.queries)} \n queries: {connection.queries}, "
    )
