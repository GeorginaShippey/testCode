from django import forms
from .models import Client, Site, Group
from django.contrib.admin import widgets

#--------------------------------------------------------------------

class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = ('name',)
        
#--------------------------------------------------------------------

class NewSiteForm(forms.ModelForm):

    class Meta:
        model = Site
        fields = ('client','name',)

class EditSiteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EditSiteForm, self).__init__(*args,**kwargs)
        if hasattr(self.instance, 'client'):
            self.fields['groups'].queryset = Group.objects.filter(client=self.instance.client)
        else:
            self.fields['groups'].queryset = Group.objects.all()
        
    groups = forms.ModelMultipleChoiceField(required=False, widget=widgets.FilteredSelectMultiple(verbose_name='Groups',is_stacked=False), queryset=Group.objects.all())
    #attrs={'disabled':'disabled'}, BEFORE verbose_name

    class Meta:
        model = Site
        fields = ('name', 'groups')

"""
In the instance where the client is not null (not adding a new client),
the group select boxes only show the groups associated with the client id
"""
class SiteAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SiteAdminForm, self).__init__(*args,**kwargs)
        if hasattr(self.instance, 'client'):
            self.fields['groups'].queryset = Group.objects.filter(client=self.instance.client).exclude(group=self.instance.group)
            #self.fields['client'].widget.attrs['disabled'] = 'disabled'
        else:
            self.fields['groups'].queryset = Group.objects.all()
            
#--------------------------------------------------------------------
class NewGroupForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = ('name','client')
        
class EditGroupForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(EditGroupForm, self).__init__(*args,**kwargs)
        if hasattr(self.instance, 'client'):
            '''
            g is used to store the object of the group that we are
            editing. We need to use g.id in the queryset below.
            This excludes being able to set a group as a subgroup of
            itself.
            '''
            g = Group.objects.filter(id=self.instance.id)
            self.fields['subgroups'].queryset = Group.objects.filter(client=self.instance.client).exclude(id__in=g)
        else:
            self.fields['subgroups'].queryset = Group.objects.all()
     
    #creates the linked select boxes generally used in the admin area   
    subgroups = forms.ModelMultipleChoiceField(required=False, widget=widgets.FilteredSelectMultiple(verbose_name='Subgroups',is_stacked=False), queryset=Group.objects.all())

    class Meta:
        model = Group
        fields = ('name','subgroups')
        


