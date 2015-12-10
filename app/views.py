from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from app.models import *

from .forms import NewSiteForm, EditSiteForm, ClientForm, NewGroupForm
from .forms import EditGroupForm

import json
from django.core import serializers

def index(request):
    #return HttpResponse("index")
    return render(request, 'app/index.html')
    
#--------------------------------------------------------    
    
def clients(request):
    #return HttpResponse("clients")
    c = Client.objects.all()
    return render(request, 'app/clients.html', {'clients':c})
    
def client(request, pk):
    c = get_object_or_404(Client, pk=pk)
    return render(request, 'app/client.html', {'client':c})
    
def client_new(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save() #use commit=False if need to add
            return HttpResponseRedirect(reverse('app:client', args=(client.id,)))
    else:
        form = ClientForm()
    return render(request, 'app/client_new.html', {'form':form})

def client_edit(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == "POST":
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            client = form.save()
            return HttpResponseRedirect(reverse('app:client', args=(client.id,)))
    else:
        form = ClientForm(instance=client)
    return render(request, 'app/client_edit.html', {'form': form})
    
def client_delete(request, pk):
    client = get_object_or_404(Client, pk=pk)
    client.delete()
    return HttpResponseRedirect(reverse('app:clients', args=()))
    
#--------------------------------------------------------

def sites(request):
    s = Site.objects.all()
    return render(request, 'app/sites.html', {'sites':s})

def site(request, pk):
    s = get_object_or_404(Site, pk=pk)
    return render(request, 'app/site.html', {'site':s})

def site_new(request):
    #get_object_or_404(Client, id=client_id)
    if request.method == "POST":
        form = NewSiteForm(request.POST)
        if form.is_valid():
            site = form.save() #use commit=False if need to add
            return HttpResponseRedirect(reverse('app:site', args=(site.id,)))
    else:
        form = NewSiteForm()
    return render(request, 'app/site_new.html', {'form':form})
    
def site_edit(request, pk):
    site = get_object_or_404(Site, pk=pk)
    if request.method == "POST":
        form = EditSiteForm(request.POST, instance=site)
        if form.is_valid():
            post_client_id = request.POST.get('id_client')
            site = form.save()
            return HttpResponseRedirect(reverse('app:site', args=(site.id,)))
    else:
        form = EditSiteForm(instance=site)
    return render(request, 'app/site_edit.html', {'form': form})

def site_delete(request, pk):
    site = get_object_or_404(Site, pk=pk)
    site.delete()
    return HttpResponseRedirect(reverse('app:sites', args=()))
    
#--------------------------------------------------------

def groups(request):
    g = Group.objects.all()
    return render(request, 'app/groups.html', {'groups':g})

def group(request, pk):
    g = get_object_or_404(Group, pk=pk)
    return render(request, 'app/group.html', {'group':g})
      
def group_new(request):
    if request.method == "POST":
        form = NewGroupForm(request.POST)
        if form.is_valid():
            group = form.save()
            return HttpResponseRedirect(reverse('app:group', args=(group.id,)))
    else:
        form = NewGroupForm()
    return render(request, 'app/group_new.html', {'form':form})
    
def group_edit(request, pk):
    group = get_object_or_404(Group, pk=pk)
    if request.method == "POST":
        form = EditGroupForm(request.POST, instance=group)
        if form.is_valid():
            group = form.save()
            return HttpResponseRedirect(reverse('app:group', args=(group.id,)))
    else:
        form = EditGroupForm(instance=group)
    return render(request, 'app/group_edit.html', {'form': form})
    
def group_delete(request, pk):
    group = get_object_or_404(Group, pk=pk)
    group.delete()
    return HttpResponseRedirect(reverse('app:groups', args=()))  
#--------------------------------------------------------
#JS, JQ & AJAX VIEWS

#linked to in the javascript folder from site
#for example:
"""
def test_admin(request):
    print("in test_admin")
    if request.is_ajax() and request.POST:
        client_id = request.POST.get('client_id')
        print(client_id)
        g = Group.objects.filter(client=int(client_id))
        for group in g:
            print(group.name)
        data = serializers.serialize("json",g)
        return HttpResponse(data, content_type='application/json')
    else:
        raise Http404
"""
