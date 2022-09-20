from django.shortcuts import redirect

def if_logedin(func):
    def check(request,*args,**kwargs):
        if request.session.get('id'):
            return redirect('home')
        else:
            return func(request,*args,**kwargs)
    return check
    
def if_not_logedin(func):
    def check(request,*args,**kwargs):
        if not request.session.get('id'):
            return redirect('login')
        else:
            return func(request,*args,**kwargs)
    return check
    
    
    