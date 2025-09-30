from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.category}"
    
    class Meta:
        ordering = ["category"]
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Item(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    category_fk = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="items", verbose_name="Категория")
    get_date = models.DateField(verbose_name="Дата появления")
    color = models.CharField(max_length=20, blank=True, null=True, verbose_name="Цвет")

    def __str__(self):
        return f"{self.name} / {self.category_fk.category}"
    
    class Meta:
        ordering = ["name"]
        verbose_name = "Вещь"
        verbose_name_plural = "Вещи"


