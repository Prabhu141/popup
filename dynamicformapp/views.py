


from .models import Item


from django.shortcuts import render, redirect
from .forms import ItemForm

def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')  # Redirect to a view that lists all items
    else:
        form = ItemForm()

    return render(request, 'add_item.html', {'form': form})


def item_list(request):
    items = Item.objects.all()
    return render(request, 'item_list.html', {'items': items})