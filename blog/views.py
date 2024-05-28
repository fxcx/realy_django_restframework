from django.shortcuts import render

# Create your views here.
def reder_article(req):
    return render(req, 'article.html')