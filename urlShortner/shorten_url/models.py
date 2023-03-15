import random
import string
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class ShortUrlModel(models.Model):
    ID_LENGTH = 6
    short_id = models.CharField(max_length=ID_LENGTH, blank=False, unique=True)
    url = models.URLField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    count = models.IntegerField(default=0)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return f'<short id: {self.short_id} url: {self.url}>'

    def increase_short_id_counter(self) -> None:
        """When a user request a original url with the short_id."""
        self.count += 1
        self.save()

    @classmethod
    def generate_short_id(cls) -> str:
        """
        Generate a short id used to shorten the original url
        making sure short id is not in used.
        """

        CHARACTERS = (
                string.ascii_uppercase
                + string.ascii_lowercase
                + string.digits
        )

        while True:
            short_id = ''.join(
                random.choice(CHARACTERS)
                for _ in range(cls.ID_LENGTH)
            )

            try:
                cls.objects.get(short_id=short_id)
            except ObjectDoesNotExist:
                return short_id
