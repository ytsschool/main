from django.db import models
from django import forms

import random

texts = {
	1: "Not to know is bad, not to wish to know is worse.",
	2: "Success doesn't come to you... you go to it.",
	3: "Formal education will make you a living. Self-education will make you a fortune.",
	4: "Those who cannot change their minds cannot change anything.",
	5: "If anything is worth trying at all, it's worth trying at least 10 times.",
	6: "Two things are infinite: the universe and human stupidity; and I'm not sure about the universe.",
	7: "Being entirely honest with oneself is a good exercise.",
	8: "The possession of unlimited power will make a despot of almost any man. There is a possible Nero in the gentlest human creature that walks.",
	9: "Every English poet should master the rules of grammar before he attempts to bend or break them.",
	10: "To limit the press is to insult a nation; to prohibit reading of certain books is to declare the inhabitants to be either fools or slaves.",
}

# Create your models here.
class Cryptotext(models.Model):
	text1 = "let it be let it be speaking words of wisdom let it be"


	@staticmethod
	def encrypt(text):
		encrypted = ""
		for i in text:
			encrypted += chr(ord(i) + 3)
		return encrypted

	@staticmethod
	def random_text():
		return texts[random.randint(1,10)]

class ContactForm(forms.Form):
	decrypted = forms.CharField(max_length=200)