from django.core.exceptions import ValidationError

def validate_content(value):
	content = value
	profanities = ["damn", "shoot", "darn"]
	for each in profanities:
		if content.lower() == each:
			raise ValidationError("Content cannot be profanity. Please enter a different Tweet.")
	return value