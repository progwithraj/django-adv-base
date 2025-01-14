from django.db import models
from django.utils.translation import gettext_lazy as _
from customUser.models import CustomUser
from post.models import Posts
# Create your models here.


class Notifications(models.Model):
    NOTIFICATION_TYPES = (
        ("Like", "Like"),
        ("Comment", "Comment"),
        ("Bookmark", "Bookmark"),
    )
    user = models.ForeignKey(
        CustomUser,
        verbose_name=_("User who received the notification"),
        on_delete=models.CASCADE,
    )
    post = models.ForeignKey(
        Posts,
        verbose_name=_("Post at which the notification is made"),
        on_delete=models.CASCADE,
    )
    type = models.CharField(
        max_length=100,
        verbose_name=_("Type of the notification"),
        choices=NOTIFICATION_TYPES,
    )
    is_seen = models.BooleanField(
        default=False, verbose_name=_("If the notification is seen or not")
    )
    arrived_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_("The arrival date of the notification")
    )

    class Meta:
        verbose_name = _("Notification")
        verbose_name_plural = _("Notifications")
        db_table = "Notifications"
        ordering = ["-arrived_at"]

    def __str__(self):
        return f"{self.post.title} - {self.type}"
