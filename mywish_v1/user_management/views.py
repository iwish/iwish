# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
import re

ValidUserNamePattern = re.compile("^[a-zA-Z_]\w+$")
ValidEmailPattern = re.compile("^([_a-z0-9]+([._a-z0-9-]+)*)@([a-z0-9]{2,}(.[a-z0-9-]{2,})*.[a-z]{2,3})$")

def CheckUserName(userName):
    global ValidUserNamePattern
    if ValidUserNamePattern.match(userName) == None:
        return False

    return True

def CheckEmail(email):
    global ValidEmailPattern
    if ValidEmailPattern.match(email) == None:
        return False
    return True

def CheckPostUserInfo(req):
    """
    Check POST Data for registration
    """
    if "user_name" not in req.POST.keys():
        return u"User Name should be specified"
    else:
        userName = req.POST["user_name"]
        if CheckUserName(userName) == False:
            return u"请确认用户名的合法性（大小写英文字母数字或者下划线，必须以字母开头）"
    if "email" not in req.POST.keys():
        email = req.POST["email"]
        if CheckEmail(email) == False:
            return u"确认email地址合法性"
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

