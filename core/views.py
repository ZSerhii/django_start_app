from django.shortcuts import render, redirect
from datetime import datetime, date
from core.forms import ContactUsForm
from core.models import Feedback


def django_start_page_view(request):
    # import import ipdb; ipdb.set_trace()
    message = request.GET.get('message')

    if message:
        pass

    new_year_date = date(2020, 1, 1)

    return render(request, 'django_start.html', context={
        'name': 'Serhii',
        'now': datetime.now(),
        'message': message,
        'new_year_date': new_year_date
    })


def about_page_view(request):
    return render(request, 'about.html', context={
        'name': 'Serhii',
        'now': datetime.now()
    })


def contacts_page_view(request):
    last_message = None

    if request.method == "POST":
        form = ContactUsForm(request.POST)

        if form.is_valid():
            last_message = request.POST.get("message")

            Feedback.objects.create(name=request.POST.get("name"), text=last_message)

            # return redirect('feedbacks')
            
            response = redirect('feedbacks')
            response['Location'] += '?from=contacts-us'

            return response
    else:
        form = ContactUsForm()

    return render(request, 'contacts.html', context={
        'message': last_message,
        'form': form
    })


def feedbacks_page_view(request):
    has_contacted = (request.GET.get('from') == 'contacts-us')

    feedbacks = Feedback.objects.filter(status=1)

    return render(request, 'feedbacks.html', context={
        'feedbacks': feedbacks,
        'has_contacted': has_contacted,
        'now': datetime.now()
    })
