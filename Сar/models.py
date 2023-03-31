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
    reviews = models.TextField('Отзывы', blank=True, null=True)

    def __str__(self):
        return self.title


class CarReview(models.Model):
    RATINGS = (
        ('*', '*'),
        ('**', '**'),
        ('***', '***'),
        ('****', '****'),
        ('*****', '*****')
    )

    car_review = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="comment_object", null=True)
    text = models.TextField(null=True)
    rate_stars = models.CharField(max_length=100, choices=RATINGS, default=False)
    created_date = models.DateTimeField(auto_now_add=True, null=True)


def __str__(self):
    return self.rate_stars


class User(models.Model):
    name = models.CharField("Ваше имя:", max_length=100)
    lastname = models.CharField("Ваша фамилия:", max_length=100)
    email = models.CharField("Ваш e-mail:", max_length=100)
    feedback_text = models.TextField("Ваш отзыв:", max_length=200)

    def __str__(self):
        return self.title
