from django.shortcuts import render, redirect
from item.models import Category, Item
from .forms import SignUpForm

# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    
    return render(request, 'base/index.html', {
        'categories': categories,
        'items': items,
    })

def contact(request):
    return render(request, 'base/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            # didnt add brackets to save, very crucial
            form.save()
            return redirect('/login/')
        
    else:
        form = SignUpForm()

    return render(request, 'base/signup.html', {
        'form': form,
    })

def categorical(request, pk):
    categories = Category.objects.all()
    chosen_category = Category.objects.get(pk=pk)
    items = Item.objects.filter(category=chosen_category)

    return render(request, 'base/categories.html', {
        'categories': categories,
        'items': items,
        'chosen_category':chosen_category,
    })
