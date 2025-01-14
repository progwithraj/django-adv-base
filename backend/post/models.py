import shortuuid
from coreApp.utility import check_none_or_empty
from customUser.models import CustomUser
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext as _
from django_prose_editor.fields import ProseEditorField
from userProfile.models import UserProfile


# The `Category` class defines a model with fields for title, image, and slug, along with methods for
# string representation, generating a slug, and saving the instance.
class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name=_("Title of the category"))
    image = models.FileField(
        upload_to="category_images",
        blank=True,
        null=True,
        verbose_name=_("image of the category"),
    )
    slug = models.SlugField(
        unique=True, blank=True, null=True, verbose_name=_("slug of the category")
    )

    class Meta:
        verbose_name_plural = "Categories"
        db_table = "Categories"
        ordering = ["title"]

    def __str__(self):
        return self.title

    def get_slug(self):
        return slugify(self.title)

    @property
    def post_counts(self):
        """
        The function `post_counts` returns the count of posts associated with the object.
        :return: The `post_counts` method is returning the count of posts associated with the object
        instance (`self`).
        its utilizing the relationship between the `Category` object and its related `Posts` objects.
        """
        return self.posts.count()

    def save(self, *args, **kwargs):
        if check_none_or_empty(self.slug):
            self.slug = self.get_slug()
        super(Category, self).save(*args, **kwargs)


# The `Posts` class defines a model with fields for user, profile, category, title, description,
# status, views, likes, image, slug, created_at, and updated_at, along with methods for string
# representation and slug generation.
class Posts(models.Model):
    STATUS_CHOICES = (
        ("Active", "Active"),
        ("Draft", "Draft"),
        ("Disabled", "Disabled"),
    )
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="posts",
        verbose_name=_("The Creator of the post"),
    )
    profile = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="posts",
        verbose_name=_("Profile details of the post creator user"),
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="posts",
        verbose_name=_("Category of the post"),
    )
    title = models.CharField(max_length=100, verbose_name=_("Title of the post"))
    description = models.TextField(
        null=True, blank=True, verbose_name=_("Description of the post")
    )
    status = models.CharField(
        choices=STATUS_CHOICES,
        default="Active",
        verbose_name=_("Current Status of the post"),
    )
    views = models.IntegerField(default=0, verbose_name=_("No of views of the post"))
    likes = models.ManyToManyField(
        CustomUser,
        blank=True,
        related_name="likes",
        verbose_name=_("Users who liked the post"),
    )
    image = models.FileField(
        upload_to="post_images",
        blank=True,
        null=True,
        verbose_name=_("image of the post"),
    )
    slug = models.SlugField(
        unique=True, blank=True, null=True, verbose_name=_("slug of the post")
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_("The creation date of the post")
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=_("Updated date of the post")
    )

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"  # plural form of table name
        db_table = "Posts"
        ordering = [
            "-created_at"
        ]  # this is to set default queryset ordering by created_at in desc order
        indexes = [
            models.Index(fields=["user", "category"]),
            models.Index(fields=["user", "profile"]),
            models.Index(fields=["user", "status"]),
        ]  # this is for indexing, it will help in better performing queries
        # db_table = 'Posts' # this is to set a custom name for the table in db
        # permissions = [
        #     ("can_publish", "Can publish posts"),
        #     ("can_edit", "Can edit posts"),
        # ]

    def __str__(self):
        """
        The `__str__` function in Python returns the title of an object when it is converted to a
        string.
        :return: The `__str__` method is returning the `title` attribute of the object.
        """
        return self.title

    @property
    def like_count(self):
        """
        The function `like_count` returns the count of likes associated with the object.
        :return: The `like_count` method is returning the count of likes associated with the object
        instance (`self`).
        """
        return self.likes.count()

    def get_slug(self):
        """
        The function `get_slug` generates a unique slug by combining a slugified title with a portion of
        a UUID.
        :return: The `get_slug` method is returning a slugified version of the `title` attribute of the
        object concatenated with the first 4 characters of a randomly generated UUID.
        """
        return slugify(self.title) + "-" + shortuuid.uuid()[:4]

    def save(self, *args, **kwargs):
        """
        The function `__save__` checks if the `slug` attribute is empty and generates a new slug if
        necessary before saving the `Category` object.
        """
        if check_none_or_empty(self.slug):
            print("slug is empty", self.get_slug())
            self.slug = self.get_slug()
        super(Posts, self).save(*args, **kwargs)


# The `Comments` class defines a model for storing comments made by users on posts, including fields
# for user, post, comment text, timestamps, slug, and replies.
class Comments(models.Model):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name=_("User who made the comment"),
    )
    post = models.ForeignKey(
        Posts,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name=_("Post at which the comment is made"),
    )
    comment = ProseEditorField(verbose_name=_("Actual comment text on the post"))
    created_at = models.DateTimeField(
        verbose_name=_("The creation date of the comment"), auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name=_("Updated date of the comment"), auto_now=True
    )
    slug = models.SlugField(
        verbose_name=_("Slug of the comment"), unique=True, blank=True, null=True
    )
    in_reply_to = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        verbose_name=_("Reply to this comment"),
        related_name="replies",
    )

    class Meta:
        verbose_name_plural = "Comments"
        db_table = "Comments"
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["user", "post"]),
        ]

    def get_slug(self):
        """
        The function `get_slug` generates a unique slug by combining a slugified username and comment with a portion of
        a UUID.
        :return: The `get_slug` method is returning a slugified version of the `username` , `comment` attribute of the
        object concatenated with the first 4 characters of a randomly generated UUID.
        """
        return (
            slugify(self.user.username + self.comment[:15]) + "-" + shortuuid.uuid()[:4]
        )

    def __str__(self):
        return (
            self.user.username + " - " + self.comment[:15]
        )  # return username and first 15 characters of comment

    def reply_count(self):
        return self.replies.count()

    def save(self, *args, **kwargs):
        if check_none_or_empty(self.slug):
            self.slug = self.get_slug()
        super(Comments, self).save(*args, **kwargs)


class Bookmarks(models.Model):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="bookmarks",
        verbose_name=_("User who added the bookmark"),
    )
    post = models.ForeignKey(
        Posts,
        on_delete=models.CASCADE,
        related_name="bookmarks",
        verbose_name=_("Post at which the bookmark is made"),
    )
    bookmarked_at = models.DateTimeField(
        verbose_name=_("The creation date of the bookmark"), auto_now_add=True
    )

    class Meta:
        verbose_name = "Bookmark"
        verbose_name_plural = "Bookmarks"
        db_table = "Bookmarks"
        ordering = ["-bookmarked_at"]
        indexes = [
            models.Index(fields=["user", "post"]),
        ]

    def __str__(self):
        return f"{self.user.username} - {self.post.title}"

    def save(self, *args, **kwargs):
        super(Bookmarks, self).save(*args, **kwargs)
