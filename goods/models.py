from django.db import models


# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    sum = models.IntegerField()
    id = models.CharField(max_length=30, primary_key=True)

    # 一对多
    warehouse = models.ForeignKey('Warehouse', on_delete=models.CASCADE)
    production = models.ForeignKey('Production', on_delete=models.CASCADE)
    class1 = models.ForeignKey('Class1', on_delete=models.CASCADE)
    # 多对多
    ingre = models.ManyToManyField('Ingre')


class Drink(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    sum = models.IntegerField()
    id = models.CharField(max_length=30, primary_key=True)

    # 一对多
    warehouse = models.ForeignKey('Warehouse', on_delete=models.CASCADE)
    production = models.ForeignKey('Production', on_delete=models.CASCADE)
    class1 = models.ForeignKey('Class1', on_delete=models.CASCADE)
    # 多对多
    ingre = models.ManyToManyField('Ingre')


class Electrical(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    sum = models.IntegerField()
    id = models.CharField(max_length=30, primary_key=True)

    # 一对多
    warehouse = models.ForeignKey('Warehouse', on_delete=models.CASCADE)
    production = models.ForeignKey('Production', on_delete=models.CASCADE)
    class1 = models.ForeignKey('Class1', on_delete=models.CASCADE)
    # 多对多
    ingre = models.ManyToManyField('Ingre')


class Production(models.Model):
    name = models.CharField(max_length=30)
    addr = models.CharField(max_length=30)
    boss = models.CharField(max_length=30)
    id = models.CharField(max_length=30, primary_key=True)


class Ingre(models.Model):
    name = models.CharField(max_length=30, primary_key=True)
    color = models.CharField(max_length=30)


class Class1(models.Model):
    borderid = models.CharField(max_length=30, primary_key=True)
    typeid = models.CharField(max_length=30)


class Warehouse(models.Model):
    name_id = models.CharField(max_length=30)
    id = models.CharField(max_length=30, primary_key=True)
    in_time = models.DateField()
    no_time = models.DateField()
