from django.shortcuts import render
from .forms import *
from django.contrib.auth.decorators import login_required


def index(request):
    if request.method == 'POST':
        form = ApplicationForms(request.POST, request.FILES)
        message = 'Ошибка'
        if form.is_valid():
            form.save(commit=False)
            message = 'Заявка отправлена'
    else:
        form = ApplicationForms()
        message = 'Заполните форму'
    return render(request, 'app_OMSU/index.html',
                  {'form': form, 'message': message})


@login_required
def get_reports(request):
    reports = Report.objects.all()
    return render(request, 'app_OMSU/reports.html', {'reports': reports})


@login_required
def get_applications(request):
    applications = Application.objects.all()
    return render(request, 'app_OMSU/applications.html', {'applications': applications})


@login_required
def get_card_animals(request):
    card_animals = CardAnimal.objects.all()
    return render(request, 'app_OMSU/card_animals.html', {'card_animals': card_animals})


@login_required
def get_report(request, report_id):
    report = Report.objects.get(pk=report_id)
    return render(request, 'app_OMSU/get_report.html', {'report': report})


@login_required
def get_application(request, application_id):
    application = Application.objects.get(pk=application_id)
    return render(request, 'app_OMSU/get_application.html', {'application': application})


@login_required
def get_animal(request, animal_id):
    animal = CardAnimal.objects.get(pk=animal_id)
    return render(request, 'app_OMSU/get_animal.html', {'animal': animal})
