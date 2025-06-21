from django.shortcuts import render, redirect
from .models import YogaCard
from .forms import JoinForm
from django.contrib import messages


def home(request):
    cards = YogaCard.objects.all()
    return render(request, 'index.html', {'cards': cards})

    
def index(request):
    if request.method == 'POST':
        form = JoinForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully joined our community!')
            return redirect('home')  # or your index page name
    else:
        form = JoinForm()
    return render(request, 'index.html', {'form': form})