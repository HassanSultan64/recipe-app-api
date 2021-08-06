from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status


CREATE_USER_URL = reverse('user:create')

def create_user(**params):
    return get_user_model().objects.create_user(**params)


class PublicUserApiTests(TestCase):
    """Test the Users API"""

    def setUp(self):
        self.client = APIClient 

    def create_valid_user_success(self):
            """TEST CREATING USER WITH VALID PAYLOAD SUCCESFULL"""

            payload = {
                'email':'hassansahi6464@gmail.com',
                'password':'admin',
                'name':'Test name'
            }
            res = self.client.post(CREATE_USER_URL, payload)

            self.assertEqual(res.status_code, status.HTTP_201_CREATED)
            self.assertTrue(user.check_password(payload['password']))    
            self.assertNotIn('password', res.data)
             
    def test_user_exists(self):
        """TEST CREATING DUPLICATE USER FAILS"""
        payload = {
            'email':'hassansahi6464@gmail.com',
            'password':'admin'
        }
        create_user(**payload) 
        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)


    def test_password_too_short(self):
        """Test that password must be more than 5 characters"""
        payload = {'email': 'hassansahi6464@gmail.com', 'password': 'pw'}
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        user_exists = get_user_model().objects.filter(
            email=payload['email']
        ).exists()
        self.assertFalse(user_exists)    