from django.shortcuts import render

# Create your views here.
# request > returns response
# its a request handler
# Action


from django.http import HttpResponse

def say_hello(request):
    # return HttpResponse('Hello World')
    # to return template file
    # return render(request, 'hello.html')
    
    # dynamically render values by passing  dictionary
    return render(request, 'hello.html', {'name': 'copy charming'})



# now we need to map this URL to call this function