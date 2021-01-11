from django.shortcuts import render

from .forms import CsvForm


def upload_file_view(request):
    form = CsvForm(request.POST or None)

    context = {
        'form': form,
    }

    return render(request, 'csvs/upload.html', context)