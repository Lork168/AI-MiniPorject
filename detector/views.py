from django.shortcuts import render
from .forms import EmailForm
import pickle
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), "spam_model.pkl")

def home(request):
    result = None

    if request.method == "POST":
        form = EmailForm(request.POST)

        if form.is_valid():
            message = form.cleaned_data["message"]

            with open(MODEL_PATH, "rb") as file:
                model = pickle.load(file)

            prediction = model.predict([message])[0]

            if prediction == 1:
                result = "Spam"
            else:
                result = "Not Spam"

    else:
        form = EmailForm()

    return render(request, "detector/home.html", {
        "form": form,
        "result": result
    })