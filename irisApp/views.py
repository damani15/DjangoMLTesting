from django.shortcuts import render
from joblib import load

model = load("./models/model.joblib")

# Create your views here.
def start(request):
    if request.method == "POST":
        sepal_length = request.POST["sepal_length"]
        sepal_width = request.POST["sepal_width"]
        petal_length = request.POST["petal_length"]
        petal_width = request.POST["petal_width"]
        result = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
        if result[0] == 0:
            result = 'Setosa'
        elif result[0] == 1:
            result = 'Versicolor'
        else:
            result = 'Virginica'
        return render(request, "index.html", {'result': result})
    return render(request, "index.html")