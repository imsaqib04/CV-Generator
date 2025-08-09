from rest_framework import generics

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer
from django.views import View
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template.loader import render_to_string
from xhtml2pdf import pisa
from .models import Profile
import io
from django.views.generic import DetailView
from django.template.loader import render_to_string
from xhtml2pdf import pisa
import io
from django.http import HttpResponse
from django.template.loader import get_template

# Create your views here.

# function based
# @api_view(['GET','POST'])
# def profile_list_create(request):
#     if request.method=="GET":
#         profiles = Profile.objects.all()
#         serializer = ProfileSerializer(profiles,many=True)
#         return Response(serializer.data)
    
#     if request.method=="POST":
#         serializer = ProfileSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=201)
#         return Response(serializer.errors,status=400)

# class based 
class ProfileListCreateView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = io.BytesIO()
    pdf = pisa.pisaDocument(io.BytesIO(html.encode("utf-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

def generate_pdf_view(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    data = {
        'profile': profile
    }
    pdf = render_to_pdf('cv_template.html', data)
    return pdf