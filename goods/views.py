from django.shortcuts import render, HttpResponse

from goods.models import *


def login(request):
    pass


def index(request):
    return render(request, "index.html")


def production(request):
    production = Production.objects.filter().values("name")
    return render(request, "production.html", locals())


# 添加生产厂家
def add_production(request):
    if request.method == 'GET':

        return render(request, "production.html")

    else:
        production = Production.objects.filter("name")
        Production.objects.create(name=request.POST.get("name"), addr=request.POST.get("addr"),
                                  boss=request.POST.get("boss"), id=request.POST.get("id"))

        return render(request, "index.html", locals())


# 删除生产厂家
def delete_production(request):
    if request.method == 'GET':

        return render(request, "production.html")

    else:
        production = Production.objects.filter("name")
        Production.objects.filter(name=request.POST.get("name")).delete()
        return render(request, "index.html", locals())


# 添加配料
def add_ingre(request):
    if request.method == 'GET':

        return render(request, "ingre.html")

    else:
        Ingre.objects.create(name=request.POST.get("name"), color=request.POST.get("color"))
        return render(request, "index.html")


# 删除配料
def delete_ingre(request):
    if request.method == 'GET':

        return render(request, "delete_ingre.html")

    else:
        name_ = request.POST.get("name")
        print(name_)
        Ingre.objects.filter(name=name_).delete()
        return render(request, "index.html")


# 添加食品
def add_food(request):
    if request.method == 'GET':

        return render(request, "add_food.html")

    else:
        name_ = request.POST.get("name")
        price_ = request.POST.get("price")
        date_ = request.POST.get("date")
        id_ = request.POST.get("id")
        production_ = request.POST.get("production")
        pro_obj = Production.objects.filter(name=production_)
        if len(pro_obj) != 0:
            food_obj = Food.objects.create(name=name_, price=int(price_), date=date_,
                                           id=id_, production=pro_obj[0])
            ingre_obj = Ingre.objects.all()
            food_obj.ingre.add(*ingre_obj)
        return render(request, "index.html")


# 删除食品
def delete_food(request):
    if request.method == 'GET':

        return render(request, "delete_food.html")

    else:
        Food.objects.filter(name=request.POST.get("name")).delete()
        return render(request, "index.html")
