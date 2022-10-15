from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import List, Item
from . forms import ListForm, ItemForm
# Create your views here.

def home(request):
    lists = List.objects.all()
    form = ListForm

    if request.method == "POST":
        form = ListForm(request.POST)
        if form.is_valid():
            t = List(lists = form.cleaned_data["lists"].upper())
            t.save()
            return redirect ("home")
    return render(request, "home/home.html", {
        "lists" : lists, "form" : form
    })

def detail(request, pk):
    title_container = List.objects.get(id = pk)
    id_number = title_container.id
    my_lists = Item.objects.filter(list=title_container)
    form = ItemForm
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            t = Item(todos = form.cleaned_data["todos"].capitalize(), list=title_container)
            t.save()
            return redirect ("detail", title_container.id)
    return render(request, "detail/detail.html",{
        "header" : title_container, "my_lists" : my_lists, "form" : form,
    })

def deleteItem(request, pk):
    item = Item.objects.get(id = pk)
    item.delete()
    return redirect ("detail", item.list.id)

def deleteList(request, pk):
    list = List.objects.get(id = pk)
    list.delete()
    return redirect ("home")

def update(request, pk):
    item = Item.objects.get(id = pk)
    form = ItemForm (instance = item)
    if request.method == "POST":
        form = ItemForm(request.POST, instance = item)
        if form.is_valid():
            form.save()
        return redirect ("detail", item.list.id)
    return render(request, "update/update.html", {
        "item" : item, "form" : form
    })