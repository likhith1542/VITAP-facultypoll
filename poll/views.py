from django.shortcuts import render,redirect

from .forms import CreatePollForm
from .models import Poll
from django.http import HttpResponse

# Create your views here.
def home(request):
    polls=Poll.objects.all()
    context={
        'polls' : polls
    }
    return render(request,'poll/home.html',context)


def create(request):
    if request.method == 'POST':
        form=CreatePollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=CreatePollForm()
    context = {
        'form' : form,
    }
    return render(request, 'poll/create.html', context)


def results(request,poll_id):
    poll=Poll.objects.get(pk=poll_id)
    context = {
        'poll' : poll
    }
    return render(request, 'poll/results.html', context)


def vote(request,poll_id):
    poll=Poll.objects.get(pk=poll_id)
    if request.method=='POST':
        selected_option=request.POST['poll']
        if selected_option=='option1':
            poll.option_one_count +=1
        elif selected_option=='option2':
            poll.option_two_count += 1
        elif selected_option == 'option3':
            poll.option_three_count +=1
        elif selected_option == 'option4':
            poll.option_four_count += 1
        elif selected_option == 'option5':
            poll.option_five_count +=1
        elif selected_option=='option6':
            poll.option_six_count += 1
        elif selected_option=='option7':
            poll.option_seven_count +=1
        elif selected_option=='option8':
            poll.option_eight_count +=1
        elif selected_option=='option9':
            poll.option_nine_count +=1
        elif selected_option == 'option10':
            poll.option_ten_count += 1
        else:
            return HttpResponse(400,'Invalid form')
        poll.save()

        return redirect('results',poll.id)
    context = {
        'poll' : poll
    }
    return render(request, 'poll/vote.html', context)
