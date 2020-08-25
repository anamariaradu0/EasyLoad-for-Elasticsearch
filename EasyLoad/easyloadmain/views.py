from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Command
from .forms import CommandForm
from django.core.files.storage import default_storage


# Create your views here.
def index(response, id):
    ls = Command.objects.get(id=id)
    return render(response, "easyloadmain/base.html", {"name":ls.name})


def home(response):
    return render(response, "easyloadmain/home.html", {"name":"test"})


def command(response):
    if response.method == "POST":
        form = CommandForm(response.POST, response.FILES)
        if form.is_valid():
            file = response.FILES['file']
            file_name = default_storage.save(file.name, file)
            n = form.cleaned_data
            print(n)
            f = Command(name=n)
            f.save()
            return success(response)
    else:
        form = CommandForm()
    return render(response, "easyloadmain/command.html", {"form":form})


def success(response):
    return render(response, "easyloadmain/success.html", {"name": "test"})




