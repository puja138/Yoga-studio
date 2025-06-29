from django.shortcuts import render, redirect
from .models import YogaCard
from .forms import JoinForm
from django.contrib import messages


def home(request):
    cards = YogaCard.objects.all()
    form = JoinForm()

    if request.method == 'POST':
        form = JoinForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully joined our community!')
            return redirect('home')

    return render(request, 'index.html', {
        'cards': cards,
        'form': form
    })

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Example: print ya email bhej sakte ho
        print(f"New Contact Form: {name}, {email}, {message}")

        # Optional: send_mail() call karo
        # send_mail('New Contact', message, email, ['your@email.com'])

        return render(request, 'contact_success.html', {'name': name})

    return render(request, 'home.html')