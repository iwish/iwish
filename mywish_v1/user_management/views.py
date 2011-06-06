from django.shortcuts import render_to_response

def CheckPostUserInfo(req):
    if "user_name" not in req.POST.keys():
        return "User Name should be specified"
    if "email" not in req.POST.keys():
        return "Email should be specified"
    if "passwd" not in req.POST.keys():
        return "Password should be specified"
    if "passwd_verify" not in req.POST.keys():
        return "Password for verification should be specified"
    return "OK"

def register(req):
    if req.method == 'POST':
        # Do register action.
        ret = CheckPostUserInfo(req)
        if ret != "OK":
            html = "templates/user_register.html"
            context = {"error_message" : ret}
        else:
            html = "templates/user_register.html"
            context = {"error_message" : "NO ERROR"}
        # TODO
    else:
        html = "templates/user_register.html"
        context = {}
    
    return render_to_response(html, context)

