import requests
import environ
from .models import Users
from django.core.exceptions import ObjectDoesNotExist

env = environ.Env()
environ.Env.read_env()

def get_user_data(token):
    user_data_url = env('USER_DATA_URL')
    user_data_headers = {'Authorization' : token}

    try:
        response_user_data = requests.get(url=user_data_url, headers=user_data_headers)
    # except exceptions.HTTPError as e:
    #     print("Invalid response when requesting for user_data:")
    #     print(e)
    # except exceptions.ConnectionError as e:
    #     print("Connection error when requesting for user_data:")
    #     print(e)
    # except exceptions.Timeout as e:
    #     print("Timeout when requesting for user_data:")
    #     print(e)
    # except response_user_data.raise_for_status() as e:
    #     print("Invalid url when requesting for user_data")
    #     print(e)
    except Exception as e:
        print("Exception occured when requesting for USER DATA:")
        print(e)
    else:
        if response_user_data.status_code==200:
            # TO-DO : InvildJSONError handling
            user_data = response_user_data.json()
            is_maintainer = False

            user_roles = user_data['person']['roles']
            for role in user_roles:
                if role['role']=='Maintainer':
                    is_maintainer=True
                    break

            if is_maintainer:
                required_user_data = {
                    'is_maintainer' : is_maintainer,
                    'username' : user_data['person']['fullName'],
                    'email' : user_data['contactInformation']['instituteWebmailAddress'],
                    'password' : token,
                    'year' : user_data['student']['currentYear'],
                    'image' : user_data['person']['displayPicture']
                }
            else:
                required_user_data = {
                    'is_maintainer' : is_maintainer,
                }
            return required_user_data

    return None

def check_and_create_user(user_data):
    user_dict={
        'created' : False,
        'user' : ''
    }
    try:
        user=Users.objects.get(username=user_data['username'])
    except ObjectDoesNotExist:
        user = Users(
            username=user_data['username'],
            email=user_data['email'],
            password=user_data['password'],
            is_superuser=False,
            is_staff=True,
            is_active=True,
            year=user_data['year'],
            image=user_data['image'],
        )
        user_dict['created']=True
    user_dict['user']=user
    user.save()
    return user_dict

# TO-DO : Exception handling : InvildJSONError handling in get_user_data function