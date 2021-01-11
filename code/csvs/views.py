from django.shortcuts import render
from django.contrib.auth.models import User

import csv

from .forms import CsvForm
from .models import Csv

from products.models import Product, Purchase
from products.utils import get_alert_message


def upload_file_view(request):
    messages = []
    form = CsvForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        form = CsvForm()
        try:
            obj = Csv.objects.get(activated=False)

            with open(obj.file_name.path, 'r') as f:
                reader = csv.reader(f, delimiter=';')
                for row in reader:
                    print(row)
                    user = User.objects.get(id=row[3])
                    product, _ = Product.objects.get_or_create(name=row[0])
                    product.save()
                    Purchase.objects.create(
                        product=product,
                        price=int(row[2]),
                        quantity=int(row[1]),
                        salesperson=user,
                        date=row[4]
                    )

            obj.activated = True
            obj.save()

            m = get_alert_message("Success!", "File uploaded successfully", "green", "check")
            messages.append(m)
        except Exception as e:
            message = get_alert_message("Error:", f"There was a problem uploading the file:\n{e}", "red", "times")
            messages.append(message)


    context = {
        'form': form,
        'messages': messages,
    }

    return render(request, 'csvs/upload.html', context)