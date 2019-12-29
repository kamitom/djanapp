from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from faker import Faker

# Create your views here.


def index(request):
    fake = Faker()
    # return HttpResponse('Hello, djanapp. You are at the polls index.')
    context = {
        'data_tomjr_test': "fake name is: " + fake.name(),
    }

    template = loader.get_template('polls/hello.html')
    return HttpResponse(template.render(context, request))


def index4(request):
  # 以下寫法也可以
    fake4 = Faker()
    return render(request, 'polls/hello_django.html', {
        'data_tomjr_test4': "fake name: " + fake4.name(),
    })


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
