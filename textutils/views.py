# i have created this file - Akshit

# index takes an argument 'request' and needs to be specified otherwise index error will occur

# views return an HTTP Response instead of a string

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    # Get the text
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    charcount = request.POST.get('charactercount','off')
    # Analyse the text
    purpose = ""
    analyzed  = ""
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        purpose = purpose + 'Removed Punctuations, '
        djtext = analyzed
    if(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        djtext = analyzed
        purpose = purpose + 'Changed to UpperCase, '
    if(newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if(char != "\n" and char!='\r'):
                analyzed = analyzed + char
        purpose = purpose + 'Removed Newlines, '
        djtext = analyzed
    if(extraspaceremover == "on"):
        analyzed = ""
        for index,char in enumerate(djtext):
            if not(djtext[index] ==" " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        purpose = purpose + 'Removed extra space, '
        djtext = analyzed
    if(charcount == "on"):    
        count = 0
        # analyzed = ""
        for char in djtext:
            count +=1
        if(analyzed != ""):
            analyzed = djtext + "\nNumber of Characters are : " + str(count)
        else:
            analyzed = "Number of Characters are : " + str(count)
        purpose = purpose + 'Count Characters, '
    if(removepunc != 'on' and fullcaps != 'on' and newlineremover != 'on' and extraspaceremover != 'on' and charcount != 'on'):
        return render(request,'error.html')
    else:
        params = {'purpose' : purpose, 'analyzed_text' : analyzed}
        return render(request,'analyze.html',params) 