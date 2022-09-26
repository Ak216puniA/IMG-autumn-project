import requests
import environ

env = environ.Env()
environ.Env.read_env()

def get_auth_code():
    auth_code_url=env('AUTH_CODE_URL')
    request_data = {
        'response_type' : 'code',
        'client_id' : env('CLIENT_ID'),
        'redirect_url' : 'http://localhost:8000/auth/auth-token/'
    }
    response = requests.get(url=auth_code_url, params=request_data)

    if response.status_code==200:
        return True
    
    return False