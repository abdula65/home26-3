from django.db import models


class Cars(models.Model):
    CAR_TYPE = (
        ('Жигули', 'Жигули'),
        ("Мазда", "Мазда"),
        ("Тойота", "Тойота"),
        ("Лексус", "Лексус"),
        ("Мерседес", "Мерседес"),
    )
    title = models.CharField("Название Марки Машины", max_length=100)
    description = models.TextField("Описание Машины")
    image = models.ImageField(upload_to='')
    car_type = models.CharField(max_length=100, choices=CAR_TYPE)
    created_data = models.DateTimeField(auto_now_add=True)
    cost = models.PositiveIntegerField()
    video = models.URLField()

    def __str__(self):
        return self.title
