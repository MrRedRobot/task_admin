from django.db import models

class Comentary(models.Model):
    comentary_text = models.TextField(null=False)

    def __str__(self):
        return self.comentary_text