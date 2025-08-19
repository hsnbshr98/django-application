# events/ai_service.py
from transformers import pipeline, set_seed
import re

class AIDescriptionGenerator:
    def __init__(self):
        self.generator = pipeline('text-generation', model='distilgpt2')
        set_seed(42) 
    
    def generate_description(self, title, location, date_time=None):
        prompt = f"Event: {title}"
        if location:
            prompt += f" at {location}"
        if date_time:
            prompt += f" on {date_time.strftime('%B %d, %Y')}"
        prompt += ". Description:"
        
        try:
            result = self.generator(
                prompt,
                max_length=100,
                num_return_sequences=1,
                truncation=True,
                pad_token_id=self.generator.tokenizer.eos_token_id
            )
            
            generated_text = result[0]['generated_text']
            
            description = generated_text.replace(prompt, '').strip()
            
            description = re.split(r'[.!?]', description)[0] + '.'
            
            if not description or description == '.':
                description = self._get_fallback_description(title, location)
                
            return description
            
        except Exception as e:
            print(f"AI generation failed: {e}")
            return self._get_fallback_description(title, location)
    
    def _get_fallback_description(self, title, location):
        """Fallback description if AI generation fails"""
        if location:
            return f"Join us for {title} at {location}. This event promises to be engaging and informative for all attendees."
        else:
            return f"Join us for {title}. This event promises to be engaging and informative for all attendees."