from __future__ import unicode_literals

from django.db import models
import bcrypt

class UserManager(models.Manager):
	def validate_registration(self, form_data):
		errors = {}

		#first name
		if len(form_data['first_name']) ==0:
			errors.append("First name is required")

		if len(form_data['last_name']) ==0:
			errors.append("Last name is required")

		if len(form_data['email']) ==0:
			errors.append("Email is required")

		if len(form_data['password']) ==0:
			errors.append("Password is required")

		if len(form_data['credit_card']) ==0:
			errors.append("credit card is not required")

		if len(form_data['address']) ==0:
			errors.append("Address is required")

		if form_data['password'] != form_data['password_confirmation']:
			errors.append("Passwords must match.")

		print 'in models'
		return errors

	def create_user(self, form_data):
		hashpw = bcrypt.hashpw(form_data['password'].encode(), bcrypt.gensalt())
		


		User.objects.create(
			first_name= form_data['first_name'],
			last_name= form_data['last_name'],
			email= form_data['email'],
			password = hashpw,
			address = form_data['address'],
			credit_card = hashpw,			
			)
		return redirect('/success')

# Create your models here.
class User(models.Model):
	first_name = models.CharField(max_length=45, blank= False)
	last_name = models.CharField(max_length=45, blank= False)
	email = models.CharField(max_length=45, blank= False)
	password = models.CharField(max_length=45, blank= False)
	address = models.CharField(max_length=45, blank= False)
	credit_card = models.CharField(max_length=16) 
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = UserManager()

	def __unicode__(self):
		return 'first_name: {}, last_name: {}, email: {}, password:{} id: {}, credit_card: {}, address: {}'. format(self.first_name, self.last_name, self.email, self.password, self.credit_card, self.address, self.id)

