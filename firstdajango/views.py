from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return HttpResponse('hello')
def homepage(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def count(request):
    fulltext=request.GET["fulltext"]
    lst=fulltext.split()
    count_word=dict()
    for i in lst:
        if i not in count_word:
            count_word[i]=1
        else:
            count_word[i]+=1

    return render(request,'count.html',{'fulltext':fulltext,'words':count_word.items()})