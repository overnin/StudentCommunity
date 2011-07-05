from django.http import HttpResponse, Http404
from community.models import GoogleGroup, Post
from django.shortcuts import render_to_response, get_list_or_404

def index(request):
    googlegroup_list = GoogleGroup.objects.all()
    return render_to_response('community/index.html', {'googlegroup_list': googlegroup_list})

def detail(request, googlegroup_id):
    try:
        googlegroup_object = GoogleGroup.objects.get(pk=googlegroup_id)
        post_list = get_list_or_404(Post, googlegroup=googlegroup_object)
    except GoogleGroup.DoesNotExist:
        raise Http404
    return render_to_response('community/detail.html', 
                              {'googlegoup_objecct':googlegroup_object, 
                               'post_list':post_list})