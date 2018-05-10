from django.shortcuts import render, HttpResponse, redirect

# the index function is called when root is visited
def index(request):
    return render(request, "survey_form_templates/index.html")

def result(request):
    if 'count' not in request.session:
        request.session["count"] = 1
    else:
        request.session["count"] += 1
    if request.method == "POST":
        context = {
            "name": request.POST['name'],
            "dojo_location": request.POST['dojo_location'],
            "favorite_language": request.POST['favorite_language'],
            "comment": request.POST['comment']
        }
    return render(request, "survey_form_templates/results.html", context)

def clear(request):
    return redirect('/')
