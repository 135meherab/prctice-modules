import datetime
from django.shortcuts import render


# Create your views here.
def home(request):
    # cntext = {'name': 'meherab', 'github': 'github.com/135meherab'}
    
    cntext = {
        'len': ['a','b','c','d','e','f'],
        'add': 8,
        'add_slashes': "i' am meherab",
        'cut': 'String with spaces',
        'date': datetime.datetime.now(),
        'setd': '',
        'sort': [
                    {'name': 'zed', 'age': 19},
                    {'name': 'amy', 'age': 22},
                    {'name': 'joe', 'age': 31},
                ],
        'html': '<p>You are <em>pretty</em> smart!</p>',
        'linenumber': """Arnold
                        Brandy
                        Caleb
                        Dexter""",
        'string': 'I Am Master Yoda',
        'title': "It's a new day",
        'time': '2022-01-02T10:30:00.000123',


        }

    return render(request, 'app/home.html', cntext)