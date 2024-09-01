# Created by me - Anumoy Nandy

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "index.html")
    # return HttpResponse(
    #     """<h1>Home Page ...</h1>
    #                        <a href="/about"><button>About</button></a>
    #                        <button onclick="window.history.back()">Back</button>"""
    # )


def about(request):
    params = {"college": "Jadavpur University", "company": "oracle"}
    return render(request, "about.html", params)
    # return HttpResponse(
    #     """<h1>About Page ...</h1>
    #                        <a href="/contact"><button>Contact</button></a>
    #                        <button onclick="window.history.back()">Back</button>"""
    # )


def contact(request):
    return HttpResponse(
        """<h1>Contact Me Page ...</h1>
                         <button onclick="window.history.back()">Back</button>"""
    )


def analyze(request):
    text = request.POST.get("text", "default")

    removepunc = request.POST.get("removepunc", "off")
    fullcaps = request.POST.get("fullcaps", "off")
    newlineremover = request.POST.get("newlineremover", "off")
    extraspaceremover = request.POST.get("extraspaceremover", "off")

    punctuations = """!()-[]{};:'"\,<>./?@#$%^&*_~"""
    operations = []
    analyzed_text = ""

    if removepunc == "on":
        for character in text:
            if character not in punctuations:
                analyzed_text += character
        operations.append("Remove Punctuations")
        text = analyzed_text
    if fullcaps == "on":
        print(text)
        analyzed_text = text.upper()
        print(analyzed_text)
        operations.append("Capitalize Text")
        text = analyzed_text
    if newlineremover == "on":
        for character in text:
            if (character != "\n" and character != '\r'):
                analyzed_text += character
            else:
                analyzed_text += " "
        operations.append("New Line Remover")
        text = analyzed_text
    if extraspaceremover == "on":
        for index in range(len(text) - 1):
            if not (text[index] == " " and text[index + 1] == " "):
                analyzed_text += text[index]
        operations.append("Extra Space Remover")
        text = analyzed_text
    if (removepunc == "on" or fullcaps == "on" or newlineremover == "on" or extraspaceremover == "on"):
        params = {"operations": operations, "analyzed_text": analyzed_text}
        return render(request, "analyze.html", params)
    else:
        return HttpResponse("<h1>Error ....</h1>")
