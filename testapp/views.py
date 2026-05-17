from django.shortcuts import render

# Create your business logic / views here.

def page_count_view(request):
    print('='*30)
    print('COOKIE from the Client : ', request.COOKIES)  # Display all the COOKIES  on Terminal / console
    print('='*30)
    
    count = int(request.COOKIES.get('count', 0))  # initaly count 0
    count += 1  # Increment count
    response = render(request, 'testapp/counter.html',{'count':count})
    response.set_cookie('count',count)  # Send the COOKIES
    # response.set_cookie('count', count, max_age=60*60*24)  # Expiry set Ye cookie 1 day tak rahegi.
    return response


