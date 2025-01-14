from coreApp.utility import check_none_or_empty
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        """
        The function creates a user with an email, username, and optional password and additional
        fields.

        :param email: The `email` parameter is used to specify the email address of the user being
        created. It is a required field and must be provided when creating a new user. If the `email`
        parameter is not provided, a `ValueError` will be raised with the message 'Users must have an
        email
        :param username: The `username` parameter in the `create_user` method is used to specify the
        username for the user being created. It is a required field and must be provided when calling
        this method to create a new user
        :param password: The `password` parameter in the `create_user` method is used to set the
        password for the user being created. It is an optional parameter, as indicated by the `=None` in
        the method signature. If a password is provided, it will be set for the user using the `set
        :return: The `create_user` method is returning the user object that has been created and saved
        in the database.
        """
        if not email:
            raise ValueError(_("Users must have an email address"))
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        """
        The function `create_superuser` creates a superuser with specific default attributes and raises
        errors if required attributes are not set.

        :param email: The `create_superuser` method is used to create a superuser in a system. The
        method takes several parameters:
        :param username: The `create_superuser` method is a custom method for creating a superuser in a
        Django project. The parameters for the method are as follows:
        :param password: The `create_superuser` method is a custom method for creating a superuser in a
        Django project. It sets default values for certain fields like 'is_staff', 'is_superuser',
        'is_active', and 'dept' if they are not provided in the `extra_fields` parameter
        :return: The `create_superuser` method is returning the result of calling the `create_user`
        method with the provided arguments and extra fields.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, username, password, **extra_fields)

    def get_by_natural_key(self, username):
        return self.get(email=username)


class CustomUser(AbstractUser):
    username = models.CharField(unique=True, max_length=150)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    nickname = models.CharField(max_length=150, blank=True)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = CustomUserManager()

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"
        db_table = "Users"

    @property
    def get_full_name(self):
        """
        The `get_full_name` function in Python returns the full name by combining the `first_name` and
        `last_name` attributes with a space in between.
        :return: The `get_full_name` property is being returned, which concatenates the `first_name` and
        `last_name` attributes of the object with a space in between.
        """
        return f"{self.first_name} {self.last_name}"

    @property
    def get_nickname(self):
        """
        The function `get_nickname` returns the nickname if it exists, otherwise it extracts the email
        name from the email address.
        :return: The `get_nickname` method returns the nickname if it is not empty or the email name
        (part before '@' in the email) if the nickname is empty or not provided.
        """
        email_name, _ = self.email.split("@")
        return email_name

    @property
    def get_all_posts(self):
        """
        This function returns all posts associated with a given object.
        :return: A list of all posts associated with the object calling the `get_all_posts` method.
        """
        return self.posts.all()

    @property
    def get_all_comments(self):
        """
        This function returns all comments associated with a given object.
        :return: A list of all comments associated with the object.
        """
        return self.comments.all()

    @property
    def get_all_bookmarks(self):
        """
        This function uses a property decorator to return all bookmarks associated with the object.
        :return: The `get_all_bookmarks` method is returning all the bookmarks associated with the
        current instance of the class. It is using the `all()` method to retrieve all the bookmarks.
        """
        return self.bookmarks.all()

    @property
    def get_all_likes_count(self):
        """
        The function `get_all_likes_count` returns the count of likes for a user.
        :return: The `get_all_likes_count` method is returning the count of likes for a user.
        """
        return self.likes.count()

    def __str__(self):
        """
        The above function is a Python special method that returns the email attribute of an object when
        it is converted to a string.
        :return: The email attribute of the object is being returned as a string.
        """
        return self.username

    def save(self, *args, **kwargs):
        """
        The `save` function checks if certain fields are empty and assigns a default value before
        calling the parent class's `save` method.
        """
        if check_none_or_empty(self.nickname):
            self.nickname = self.get_nickname
        if check_none_or_empty(self.username):
            self.username = self.get_nickname

        super(CustomUser, self).save(*args, **kwargs)
