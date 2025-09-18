from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    get_date = models.DateField()
    color = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.name} / {self.category}"
    
    class Meta:
        ordering = ["category", "name"]
        verbose_name = "Вещь"
        verbose_name_plural = "Вещи"

