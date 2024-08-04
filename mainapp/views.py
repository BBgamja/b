from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def getIndexPage(request):
    msg="""
            <b>
                firstapp 내에 views.py의 getIndex가 호출되었습니다.
            </b>
        """
    return render(
        request,
        "mainapp/index.html",
        {}
    )