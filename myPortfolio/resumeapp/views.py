from django.shortcuts import render

def resume(request):
    return render(request,'resumeapp/resume.html')
