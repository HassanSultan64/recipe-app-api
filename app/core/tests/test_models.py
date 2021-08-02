from django.test import TestCase
from django.db import models
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """Test creating a new user with email"""
        email = 'hassansahi6464@gmail.com'
        password = 'admin'
        user = get_user_model().objects.create_user(
            email=email, 
            password=password
        )
        

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for user is normalized"""
        email = 'hassansahi6464@GMAIL.COM'
        user = get_user_model().objects.create_user(email,'admin')
        
        self.assertEqual(user.email,email.lower())

