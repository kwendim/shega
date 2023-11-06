from django.db import models

class Code(models.Model):
    code = models.CharField(max_length=8, unique=True)
    code_type = models.CharField(max_length=255, blank=True, null=True)
    is_redeemed = models.BooleanField(default=False)
    is_claimed = models.BooleanField(default=False)

    def __str__(self):
        return "self.code + self.code_type"