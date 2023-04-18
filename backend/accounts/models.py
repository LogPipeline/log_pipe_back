from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

# Create your models here.
class UserProfileInformation(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = _("UserProfileInformation")
        verbose_name_plural = _("UserProfileInformations")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("UserProfileInformation_detail", kwargs={"pk": self.pk})
