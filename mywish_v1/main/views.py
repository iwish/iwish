from django.shortcuts import render_to_response

def index(req):
    html = "templates/index.html"
    context = {}
    
    return render_to_response(html, context)
