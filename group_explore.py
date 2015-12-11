#!/usr/bin/env python

"""
This explores relations in groups and subgroups by (bfs?)
Should end up with a list of linked groups and a list of
the reachable groups

Use python, import project setting into this file
Can now access items

run using ./group_explore.py
"""

import os, sys, django
os.environ["DJANGO_SETTINGS_MODULE"] = 'project.settings'
from django.conf import settings
sys.path.append(settings.BASE_DIR)
django.setup()
from app.models import Client, Group, Site


def explore(grp_visited, grpId):
    g = Group.objects.get(id=grpId)
    if not g.id in grp_visited:
        grp_visited.append(g.id)
        for s in Site.objects.filter(groups=g.id):
            if not s.id in site_visited:
                site_visited.append(s.id)
        #optimize this further by checking sg.id in grp_visited?
        for sg in g.subgroups.all():
            explore(grp_visited, sg.id)

def main():
    grp_visited = list()
    site_visited = list()
    g = Group.objects.get(id=2)
    #print(g.name)
    if not g.id in grp_visited:
        grp_visited.append(g.id)
        for s in Site.objects.filter(groups='1'):
            site_visited.append(s.id)
        for sg in g.subgroups.all():
            explore(grp_visited, sg.id)
            
    print(grp_visited)
    print(site_visited)
    del grp_visited
    del site_visited

main()
