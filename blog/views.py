from django.shortcuts import render
import json


def index(request):
    return render(request, 'blog/index.html')
    
def exercices(request, id):
    data = {'mthMid3ex15p153':  {'title': 'التمرين 15 ص 153',
                                 'content': 'picture.jpg'}}
    context = {'data': json.dumps(data)}           
    return render(request, 'blog/exercices.html', context)
