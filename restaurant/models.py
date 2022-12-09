from datetime import timedelta

from django.db import models


class User(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.email


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    card_number = models.CharField(max_length=16)

    def __str__(self):
        return self.name


class Worker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    position = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=20)
    extra_price = models.IntegerField()
    calories = models.IntegerField(verbose_name='Количество калорий')


    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=20)
    start_price = models.IntegerField()
    type_of_cuisine = models.CharField(max_length=20, verbose_name='Тип кухни')
    calories = models.IntegerField(verbose_name='Количество калорий')

    def __str__(self):
        return self.name


class Order(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='foods')
    ingredients = models.ManyToManyField(Ingredient, related_name='ingredients', verbose_name='Добавленные ингридиенты')
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    order_date_time = models.DateTimeField(auto_now_add=True)
    vegeterian = models.BooleanField(default=False)
    food_status = models.CharField(max_length=30, verbose_name='тип блюда', default='Перекус')
    final_price = models.IntegerField(verbose_name='Финальная стоимость', default=0)



class Order_prox(Order):
    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        self.final_price = self.foods.start_price




