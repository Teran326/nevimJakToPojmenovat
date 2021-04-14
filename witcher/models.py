from django.db import models


class Name(models.Model):
    name = models.CharField(max_length=60, verbose_name="Jméno postavy",
                            help_text="Zadej jméno postavy. např. Onderic")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Race(models.Model):
    race = models.CharField(max_length=20, verbose_name="Název rasy",
                            help_text="Zadej název rasy, kterou má tvá postava.")

    class Meta:
        ordering = ["race"]

    def __str__(self):
        return self.race


class Profession(models.Model):
    profession = models.CharField(max_length=50, verbose_name="Název povolání",
                                  help_text="Zadej název povolání, kterou tvá postava vykonává.")
    description = models.CharField(max_length=1000, verbose_name="Popis povoláni")
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    name = models.OneToOneField(Name, on_delete=models.CASCADE, help_text="Zadej název postavy")

    class Meta:
        ordering = ["name", "profession"]

    def __str__(self):
        return f"Name: {self.name}, profession: {self.profession}, description: {self.description}, race: {self.race}"
