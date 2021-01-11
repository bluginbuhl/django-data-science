import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import base64

def get_alert_message(title, message, alert_level, icon=None):
    return {'title': title, 'text': message, 'alert_level': alert_level, 'icon': icon}

def get_image():
    buffer = BytesIO()  # create a bytes buffer for the image to save
    plt.savefig(buffer, format='png')
    buffer.seek(0)  # set the cursor to beginning of stream
    image_png = buffer.getvalue()  # retrieve contents of 'file'

    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')

    buffer.close()

    return graph

def get_simple_plot(chart_type, *args, **kwargs):
    # https://matplotlib.org/faq/usage_faq.html#what-is-a-backend
    plt.switch_backend('AGG')
    fig = plt.figure(figsize=(10, 4))

    x = kwargs.get('x')
    y = kwargs.get('y')
    data = kwargs.get('data')

    if chart_type == 'bar':
        plt.title("Bar Plot")
        plt.ylabel("Total Sales / [$]")
        plt.bar(x, y)
    elif chart_type == 'line':
        plt.title("Line Plot")
        plt.ylabel("Total Sales / [$]")
        plt.plot(x, y)
    else:
        plt.title("Count")
        sns.countplot('name', data=data)

    plt.tight_layout()
    plt.ion()

    graph = get_image()
    return graph