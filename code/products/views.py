from django.shortcuts import render
from .models import Product, Purchase

import pandas as pd


def chart_select_view(request):
    product_df = pd.DataFrame(Product.objects.all().values())
    product_df.rename({
        'id': 'product_id',
        'date': 'date_product_added',
    })
    product_df['product_id'] = product_df['id']
    purchase_df = pd.DataFrame(Purchase.objects.all().values())

    df = pd.merge(purchase_df, product_df, on='product_id').drop
    (['id_y', 'date_y'], axis=1).rename(
        {'id_x': 'id', 'date_x': 'date'}, axis=1)

    context = {
        'products': product_df.to_html(),
        'purchases': purchase_df.to_html(),
        'df': df.to_html(),
    }
    return render(request, 'products/main.html', context)