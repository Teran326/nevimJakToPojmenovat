from django.db import models
from django.contrib.auth.models import User
from datetime import date
# from django.urls import reverse


def attachment_path(instance, filename):
    return"witcher/" + str(instance.profession.id) + "/attachments/" + filename


def poster_path(instance, filename):
    return"profession/" + str(instance.id) + "/poster/" + filename


class Race(models.Model):
    race = models.CharField(max_length=20, verbose_name="Název rasy", default="člověk",
                            help_text="Zadej název rasy, kterou má tvá postava.")
    difference = models.CharField(max_length=60, null=True, blank=True, verbose_name="Odlišnost")

    class Meta:
        ordering = ["race"]

    def __str__(self):
        return f"Race: {self.race}, difference: {self.difference}"


class Profession(models.Model):
    profession = models.CharField(max_length=50, verbose_name="Název povolání",
                                  help_text="Zadej název povolání, kterou tvá postava vykonává.")
    description = models.TextField(max_length=1000, blank=True, null=True, verbose_name="Popis postavy.")
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    name = models.CharField(max_length=60, verbose_name="Jméno postavy")
    poster = models.ImageField(upload_to=poster_path, blank=True, null=True, verbose_name="Poster")

    class Meta:
        ordering = ["name", "profession", "race"]

    def __str__(self):
        return f"Name: {self.name}, profession: {self.profession}, description: {self.description}," \
               f" race: {self.race}, difference: {self.race}"


class Attachment(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulek")
    file = models.FileField(upload_to=attachment_path, null=True, verbose_name="Soubor")
    TYPE_OF_ATTACHMENT = (
        ('obrazek', 'Obrazek'),
        ('video', 'Video'),
        ('ostatni', 'Ostatni'),
    )
    type = models.CharField(max_length=10, choices=TYPE_OF_ATTACHMENT, blank=True, default='obrazek',
                            help_text='Vyberte povolený druh souboru', verbose_name="Typ souboru")
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE)

    class Meta:
        ordering = ["title", "type"]

    def __str__(self):
        return f"{self.title}, ({self.type})"
