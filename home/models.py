from django.conf import settings
from django.db import models

# Create your models here.

from django.db import models


class CustomText(models.Model):
    """
    Boilerplate model to populate the index homepage to demonstrate that the app was
    successfuly built. All references to it should be removed in order to remove this
    app from the project.
    """

    title = models.CharField(
        max_length=150,
    )

    def __str__(self):
        return self.title

    @property
    def api(self):
        return f"/api/v1/customtext/{self.id}/"

    @property
    def field(self):
        return "title"


class HomePage(models.Model):
    """
    Boilerplate model to populate the index homepage to demonstrate that the app was
    successfuly built. All references to it should be removed in order to remove this
    app from the project.
    """

    body = models.TextField()

    @property
    def api(self):
        return f"/api/v1/homepage/{self.id}/"

    @property
    def field(self):
        return "body"


class Item(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=256,
    )
    isSelected = models.BooleanField()
    picture = models.BinaryField()
    roomId = models.OneToOneField(
        "home.Room",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="item_roomId",
    )


class Room(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=256,
    )
    width = models.IntegerField()
    length = models.IntegerField()
    isSelected = models.BooleanField()
