from django.shortcuts import render_to_response

def register(req):
    if req.method == 'POST':
        # Do register action.
        pass
    else:
        html = "templates/user_register.html"
        context = {}
    
    return render_to_response(html, context)

