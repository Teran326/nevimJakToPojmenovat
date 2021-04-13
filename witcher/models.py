from django.db import models

class Jmeno(models.Model):
    jmeno = models.CharField(max_length=60, null=False, verbose_name="Jméno postavy", help_text="Zadej jméno postavy. např. Onderic")
    class Meta:
        ordering = ["jmeno"]
    def __str__(self):
        return self.name