# from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import HttpResponse


def home_page(request):
    # if request.method == 'POST':
    #     return HttpResponse(request.POST['item_text'])
    return render(request, 'home.html', {
        # get with 2 parameters sends a default value.
        'new_item_text': request.POST.get('item_text', ''),
    })
