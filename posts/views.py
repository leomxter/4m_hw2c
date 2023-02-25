from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    # my_list = 1234
    body = '<h1>Hello</h1>'
    # body = """
    # <!DOCTYPE html>
    #     <html>
    #         <head>
    #             <title>Geek TEST</title>
    #         </head>
    #         <body>

    #             <h1>Заголовог первого уровня</h1>
    #             <p>My first paragraph.</p>

    #         </body>
    #     </html>
    # """
    headers = {'name': 'Alex',
    # "Content-Type": "application/vnd.ms-excel",
    # "Content-Dispositon": "attachment; file-name: file.xls"
    }

    return HttpResponse(body, headers = headers, status = 200)

def get_index(request):
    context = {
        "title": 'Main Page',
        "my_list": [1, 2, 3, 4],
    }
    return render(request, 'posts/index.html', context=context)


def get_contacts(request):
    context = {
        "title": 'Контакты'
    }
    return render(request, 'posts/contacts.html', context=context)

def get_about(request):
    context = {
        "title": 'Страница о нас'
    }
    return render(request, 'posts/about.html', context=context)