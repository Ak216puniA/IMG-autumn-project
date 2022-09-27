from unicodedata import is_normalized
import requests
import environ
from .models import Users

env = environ.Env()
environ.Env.read_env()

def get_auth_code():
    auth_code_url=env('AUTH_CODE_URL')
    request_data = {
        'response_type' : 'code',
        'client_id' : env('CLIENT_ID'),
        'redirect_url' : 'http://localhost:8000/auth/auth-token/'
    }
    response = requests.post(url=auth_code_url, data=request_data)

    if response.status_code==200:
        return True
    return False

def get_user_data(token):
    user_data_url = env('USER_DATA_URL')
    user_data_headers = {'Authentication' : token}

    response_user_data = requests.get(url=user_data_url, headers=user_data_headers)

    if response_user_data.status_code==200:
        user_data = response_user_data.json()
        is_maintainer = False

        for role in user_data['person']['roles']:
            if role=='Maintainer':
                is_maintainer=True
                break

        if is_maintainer:
            required_user_data = {
                'is_maintainer' : is_maintainer,
                'username' : user_data['person']['full_name'],
                'email' : user_data['contact_information']['institute_webmail_address'],
                'password' : token,
                'year' : user_data['student']['current_year'],
                'image' : user_data['person']['display_picture']
            }
        else:
            required_user_data = {
                'is_maintainer' : is_maintainer,
            }
        return required_user_data
    return None

def check_and_create_user(user_data):
    user=Users.objects.get(username=user_data['username'])
    if user is None:
        new_user = Users(
            username=user_data['username'],
            email=user_data['email'],
            password=user_data['password'],
            is_superuser=False,
            is_staff=True,
            is_active=True,
            year=user_data['year'],
            image=user_data['image'],
        )
        new_user.save()
        return True
    return False

# TO-DO : Exception handling