from django.shortcuts import render

import pandas as pd

from .models import Product, Purchase
from .utils import get_alert_message, get_simple_plot


def chart_select_view(request):

    welcome_message = get_alert_message("Welcome!", "Please select a chart type and date range to display data", "green", "heart")

    messages = []
    graph = None
    df = None

    product_df = pd.DataFrame(Product.objects.all().values())
    product_df.rename({
        'id': 'product_id',
        'date': 'date_product_added',
    })
    product_df['product_id'] = product_df['id']
    purchase_df = pd.DataFrame(Purchase.objects.all().values())

    if request.method == 'GET':
        messages.append(welcome_message)

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

            if chart_type != "":
                if date_from != "" and date_to != "":
                    df = df[(df['date'] > date_from) & (df['date'] < date_to)]
                    df2 = df.groupby('date', as_index=False)['total_price'].agg('sum')
                    if df2.shape[0] == 0:
                        e = get_alert_message("Error", "No data for the selected date range", "red", "times")
                        messages.append(e)
                # function to get chart
                graph = get_simple_plot(chart_type, x=df2['date'], y=df2['total_price'], data=df)
            else:
                e = get_alert_message("Select Chart Type", "Please select a chart type from the dropdown menu", "yellow", "warning")
                messages.append(e)
    else:
        e = get_alert_message("Error:", "No records in the database", "yellow", "warning")
        messages.append(e)

    if len(messages) == 0:
        messages = None

    context = {
            'messages': messages,
            'graph': graph
    }

    return render(request, 'products/main.html', context)