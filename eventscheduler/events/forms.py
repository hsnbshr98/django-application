from django import forms
from .models import Event
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, ButtonHolder, Div, HTML
from .ai_service import AIDescriptionGenerator

class EventForm(forms.ModelForm):
    generate_ai_description = forms.BooleanField(
        required=False,
        initial=False,
        label='Generate description with AI'
    )
    
    class Meta:
        model = Event
        fields = ['title', 'description', 'date_time', 'location', 'status']
        widgets = {
            'date_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'description': forms.Textarea(attrs={'rows': 4}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_id = 'event-form'
        
        # Reorder fields to make AI checkbox appear after description
        self.helper.layout = Layout(
            Fieldset(
                'Event Details',
                'title',
                'date_time',
                'location',
                'status',
                'description',
                Div(
                    HTML("""
                    <div class="form-check">
                        <input class="form-check-input" type="checkbox" name="generate_ai_description" id="id_generate_ai_description">
                        <label class="form-check-label" for="id_generate_ai_description">
                            Generate description with AI
                        </label>
                    </div>
                    <small class="form-text text-muted">
                        If you don't want to write a description, check this box and we'll generate one for you.
                    </small>
                    """),
                    css_class='mb-3'
                ),
            ),
            ButtonHolder(
                Submit('submit', 'Save Event', css_class='btn-primary')
            )
        )
    
    def clean(self):
        cleaned_data = super().clean()
        generate_ai = cleaned_data.get('generate_ai_description')
        description = cleaned_data.get('description')
        
        # If AI generation is requested and no description is provided
        if generate_ai and not description:
            title = cleaned_data.get('title')
            location = cleaned_data.get('location')
            date_time = cleaned_data.get('date_time')
            
            if title:
                ai_generator = AIDescriptionGenerator()
                ai_description = ai_generator.generate_description(title, location, date_time)
                cleaned_data['description'] = ai_description
                self.initial['description'] = ai_description  # For redisplay
                
        return cleaned_data