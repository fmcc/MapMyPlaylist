# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404

def mainpage(request):
   return render_to_response('mainpage.html') 
