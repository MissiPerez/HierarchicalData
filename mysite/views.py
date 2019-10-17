from django.shortcuts import render
from django.http import HttpResponseRedirect
from mysite.models import File
from mysite.forms import FileForm


def show_files(request):
    return render(request, "files.html", {'files': File.objects.all()})
    

def add_file(request):
    form = FileForm()
    if request.method == 'POST':
        form = FileForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            File.objects.create(
                file_name=data['file_name'],
                parent=data["parent"]
            )
            return HttpResponseRedirect('/')
    else:
        form = FileForm()

    return render(request, "add_file.html", {'form': form })