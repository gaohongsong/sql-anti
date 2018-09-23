from django.shortcuts import render, render_to_response

from app_mtpp.models import Food, MpttFood


def display(foods):
    display_list = []

    for food in foods:
        display_list.append(food.title)

        children = food.children.all()
        if children.exists():
            display_list.append(display(children))

    return display_list


def unordered_list(request):
    foods = Food.objects.filter(parent=None)

    if not foods.exists():
        Food.init_test_data()

    var = display(foods)

    return render_to_response('app_mtpp/unordered_list.html', {'var': var})


def mptt_list(request):

    nodes = MpttFood.objects.all()

    return render_to_response('app_mtpp/mptt_list.html', {'nodes': nodes})
