from django.shortcuts import render

def index(request):
    answers = ["Aa", "Bb", "Cc"]
    questions = ["What color are apples? \nA) Red \nB) Yellow \nC) Blue \n", 
    "What color are bananas? \nA) Green \nB) Purple \nC) Yellow \n",
    "What color is Darth Vader? \nA) Yellow \nB) Black \nC) Green \n"]
    return render(request, "index.html")

def process_answer(request):
    return render(request, "image.html")
# Create your views here.
