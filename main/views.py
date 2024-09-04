from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306201621',
        'name': 'Anders Willard Leo',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)