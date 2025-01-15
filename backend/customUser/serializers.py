from rest_framework import serializers
from coreApp.utility import check_none_or_empty
from .models import CustomUser

# kept as reference/backup
# class CustomUserModelSerializerBackup(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True, required=True)
#     password2 = serializers.CharField(write_only=True, required=True)

#     class Meta:
#         visible_fields = [
#             "id",
#             "email",
#             "phone",
#             "username",
#             "nickname",
#             "password",
#             "password2",
#             "last_login",
#             "is_superuser",
#             "is_active",
#         ]
#         model = CustomUser
#         fields = visible_fields
#         extra_kwargs = {
#             "email": {
#                 "required": True,
#                 "error_messages": {
#                     "required": "Email address is required",
#                     "blank": "Email address cannot be blank",
#                     "unique": "Email address already exists",  # Add this
#                 },
#             },
#             "username": {
#                 "required": True,
#                 "error_messages": {
#                     "required": "Username is required",
#                     "blank": "Username cannot be blank",
#                     "unique": "Username already exists",  # Add this
#                 },
#             },
#             "password": {
#                 "write_only": True,  # to not expose password
#                 "required": True,
#                 "error_messages": {
#                     "required": "Password is required",
#                     "blank": "Password cannot be blank",
#                 },
#             },
#         }

#     def validate(self, attrs):
#         """
#         The function validates if the passwords provided in the attributes match and raises an error if they
#         do not.

#         :param attrs: The `attrs` parameter in the `validate` method likely contains a dictionary of
#         attributes or fields that are being validated. In this specific code snippet, it seems that the
#         method is checking if the "password" field matches the "password2" field in the dictionary `attrs`.
#         If the passwords do
#         :return: The `validate` method is returning the result of calling the `validate` method of the
#         superclass (parent class) of the current class.
#         """
#         if attrs["password"] != attrs["password2"]:
#             raise serializers.ValidationError("Passwords do not match")
#         # calling super validate method such that rest of the fields are validated
#         return super().validate(attrs)

#     def validate_email(self, value):
#         """Validate email"""
#         if not value:
#             raise serializers.ValidationError("Email address is required")
#         if CustomUser.objects.filter(email=value.lower()).exists():  # Add .lower()
#             raise serializers.ValidationError("Email address already exists")
#         return value.lower()  # Normalize email to lowercase

#     def validate_username(self, value):
#         """Validate username"""
#         if not value:
#             raise serializers.ValidationError("Username is required")
#         if CustomUser.objects.filter(username=value).exists():
#             raise serializers.ValidationError("Username already exists")
#         return value

#     def validate_password(self, value):
#         """Validate password field"""
#         if not value:
#             raise serializers.ValidationError("Password is required")
#         if len(value) < 8:
#             raise serializers.ValidationError(
#                 "Password must be at least 8 characters long"
#             )
#         return value

#     def create(self, validated_data):
#         password = validated_data.pop("password", None)
#         user = CustomUser(**validated_data)
#         if check_none_or_empty(password):
#             user.set_password(password)
#             user.save()
#         return user

#     def update(self, instance, validated_data):
#         password = validated_data.pop("password", None)
#         user = super().update(instance, validated_data)
#         if check_none_or_empty(password):
#             user.set_password(password)
#             user.save()
#         return user


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        visible_fields = [
            "id",
            "email",
            "phone",
            "username",
            "nickname",
            "password",
            "password2",
            "last_login",
            "is_superuser",
            "is_active",
        ]
        model = CustomUser
        fields = visible_fields
        extra_kwargs = {
            "email": {
                "required": True,
                "error_messages": {
                    "required": "Email address is required",
                    "blank": "Email address cannot be blank",
                    "unique": "Email address already exists",  # Add this
                },
            },
            "username": {
                "required": True,
                "error_messages": {
                    "required": "Username is required",
                    "blank": "Username cannot be blank",
                    "unique": "Username already exists",  # Add this
                },
            },
            "password": {
                "write_only": True,  # to not expose password
                "required": True,
                "error_messages": {
                    "required": "Password is required",
                    "blank": "Password cannot be blank",
                },
            },
        }

    def validate(self, attrs):
        """
        The function validates if the passwords provided in the attributes match and raises an error if they
        do not.

        :param attrs: The `attrs` parameter in the `validate` method likely contains a dictionary of
        attributes or fields that are being validated. In this specific code snippet, it seems that the
        method is checking if the "password" field matches the "password2" field in the dictionary `attrs`.
        If the passwords do
        :return: The `validate` method is returning the result of calling the `validate` method of the
        superclass (parent class) of the current class.
        """
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError("Passwords do not match")
        # calling super validate method such that rest of the fields are validated
        return super().validate(attrs)

    def validate_email(self, value):
        """Validate email"""
        if not value:
            raise serializers.ValidationError("Email address is required")
        if CustomUser.objects.filter(email=value.lower()).exists():  # Add .lower()
            raise serializers.ValidationError("Email address already exists")
        return value.lower()  # Normalize email to lowercase

    def validate_username(self, value):
        """Validate username"""
        if not value:
            raise serializers.ValidationError("Username is required")
        if CustomUser.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already exists")
        return value

    def validate_password(self, value):
        """Validate password field"""
        if not value:
            raise serializers.ValidationError("Password is required")
        if len(value) < 8:
            raise serializers.ValidationError(
                "Password must be at least 8 characters long"
            )
        return value

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        user = CustomUser(**validated_data)
        if check_none_or_empty(password):
            user.set_password(password)
            user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        user = super().update(instance, validated_data)
        if check_none_or_empty(password):
            user.set_password(password)
            user.save()
        return user


class CustomUserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"
        extra_kwargs = {
            "password": {"write_only": True},
        }
