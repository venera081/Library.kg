from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import random



def current_time_view(request):
    if request.method == 'GET':
        now = datetime.now().strftime('%H:%M:%S')
        return HttpResponse(now)

def random_number_view(request):
    if request.method == 'GET':
        number = random.randint(1, 500)  
        return HttpResponse(str(number))
    
def myself_story_view(request):
    if request.method == 'GET':
        return HttpResponse('Меня зовут Венера, мне 15 лет. Многие думают что я русская, но это совсем не так - во мне течет таджиская, узбекская, татарская, и ' \
        'башкирская кровь. Я занимаюсь программированием и хочу стать разработчиком и зарабатывать на этом в будущем. ' \
        'Но если честно почему я начала заниматся программированием и выбрала направление backend, потому что меня тянет к робототехнике.' \
        'Но кроме этого я люблю заниматся танцами и учить к-поп хореграфии, а также я хорошо плету из бисера')
    


