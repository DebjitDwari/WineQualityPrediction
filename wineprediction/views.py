

from django.http import HttpResponse
from django.shortcuts import render 
from django.conf import settings
import os
import pickle
import sklearn


# render(rqst,html_file) is used to render HTML templates
model_path = os.path.join(settings.BASE_DIR , "Wine.pkl")
with open(model_path, "rb") as file:
    model = pickle.load(file)

def home(request):
    pred = None
    if request.method == "POST":
        fixed_acidity = float(request.POST["fixed acidity"])
        volatile_acidity = float(request.POST["volatile acidity"])
        citric_acid = float(request.POST["citric acid"])
        residual_sugar = float(request.POST["residual sugar"])
        chlorides = float(request.POST["chlorides"])
        free_sulfur_dioxide = float(request.POST["free sulfur dioxide"])
        total_sulfur_dioxide = float(request.POST["total sulfur dioxide"])
        density = float(request.POST["density"])
        pH = float(request.POST["pH"])
        sulphates = float(request.POST["sulphates"])
        alcohol = float(request.POST["alcohol"])

        pred = model.predict([[fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol]])
        
    context = {
        "prediction" : pred
    }
    return render(request, "index.html", context)

def about(request):
    return HttpResponse("this is a About Page")

def contact(request):
    return HttpResponse("this is a Contact Page")