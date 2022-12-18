from django.shortcuts import render, redirect
from .forms import InputForm
from .models import Parameter
# from forms.py import InputForm
# Create your views here.
def frontpage(request):
    form = InputForm()
    if request.method == "POST":
        form = InputForm(request.POST)
        if form.is_valid():
            input = form.save(commit=False)
            input.post = form
            input.save()
            return redirect("evaluation")

    else:
        form = InputForm()
    return render(request, "recommend_app/frontpage.html", {'form':form})

def evaluationpage(request):
    result = Parameter.objects.all().last()
    # result.price_score = round(result.product_price/(result.max_price - result.min_price)*100)
    # result.size_score = round(result.product_size/(result.max_size - result.min_size)*100)
    # result.memory_score = round(result.product_memory/(result.max_memory - result.min_memory)*100)
    result.save()
    return render(request, "recommend_app/evaluationpage.html", {"result":result})

def comparepage(request):
    historys = Parameter.objects.all()
    return render(request, "recommend_app/comparepage.html", {"historys":historys})