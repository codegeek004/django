from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import CreatePollForm
from .models import Poll

def index(request):
    return render(request, 'poll/index.html') 

def home(request):
    polls = Poll.objects.all()
    context = {
        'polls' : polls
    }
    return render(request, 'poll/home.html', context)

def create(request):
    print('create mai gaya')
    if request.method == 'POST':
        print('post mai gaya')
        form = CreatePollForm(request.POST)
        print('form: ', form)
        if form.is_valid():
            print('form is valid k andar')
            form.save()
            return redirect('poll:home')
    else:
        print('else mai gaya')
        form = CreatePollForm()
    context = {
        'form' : form
    }
    return render(request, 'poll/create.html', context)

def vote(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)

    if request.method == 'POST':

        selected_option = request.POST['poll']
        if selected_option == 'option1':
            poll.option_one_count += 1
        elif selected_option == 'option2':
            poll.option_two_count += 1
        elif selected_option == 'option3':
            poll.option_three_count += 1
        else:
            return HttpResponse(400, 'Invalid form')

        poll.save()

        return redirect('poll:results', poll.id)

    context = {
        'poll' : poll
    }
    return render(request, 'poll/vote.html', context)

def results(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    context = {
        'poll' : poll
    }
    return render(request, 'poll/results.html', context)
