from django.shortcuts import render
from .models import Product, Purchase

import pandas as pd


def chart_select_view(request):

    error_messages = []
    df = None

    product_df = pd.DataFrame(Product.objects.all().values())
    product_df.rename({
        'id': 'product_id',
        'date': 'date_product_added',
    })
    product_df['product_id'] = product_df['id']
    purchase_df = pd.DataFrame(Purchase.objects.all().values())

    if purchase_df.shape[0] > 0:
        df = pd.merge(purchase_df, product_df, on='product_id').drop(
            ['id_y', 'date_y'], axis=1).rename(
            {'id_x': 'id', 'date_x': 'date'}, axis=1)
        if request.method == 'POST':
            chart_type = request.POST['sales']
            date_from = request.POST['date_from']
            date_to = request.POST['date_to']

            df['date'] = df['date'].apply(lambda x: x.strftime('%Y-%m-%d'))
            df2 = df.groupby('date', as_index=False)['total_price'].agg('sum')
            print(df2)

            

            if chart_type != "":
                if date_from != "" and date_to != "":
                    df = df[(df['date'] > date_from) & (df['date'] < date_to)]
                    df2 = df.groupby('date', as_index=False)['total_price'].agg('sum')
                    if df2.shape[0] == 0:
                        error_messages.append("No data for the selected date range")
                else:
                    pass
            else:
                error_messages.append("Please select a chart type to display")
    else:
        error_message.append("No records in database")

    if len(error_messages) == 0:
        error_messages = None

    context = {
            'error_messages': error_messages,
    }

    return render(request, 'products/main.html', context)