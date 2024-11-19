from django import forms
from .models import Event,Member

class EventForm(forms.ModelForm):
    attendees = forms.ModelMultipleChoiceField(
        queryset=Member.objects.all(),  # Get all the members
        widget=forms.CheckboxSelectMultiple,  # This can be a multi-select dropdown, or checkboxes
        required=False,  # Attendees are optional, depending on your needs
        label="Attendees"
    )
    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'location','attendees']
