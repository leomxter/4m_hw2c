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

    return HttpResponse(body, headers = headers, status = 500)

def get_index(request):
    print(request.user)
    if request.method == "GET":
        return HttpResponse("Main Page")
    else:
        return HttpResponse("Не тот метод запроса")

def get_contacts(request):
    return HttpResponse("Contacts")

def get_about(request):
    return HttpResponse("About")
