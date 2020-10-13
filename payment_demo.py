from instamojo_wrapper import Instamojo
API_KEY = "YOUR_KEY"
AUTH_TOKEN = 'YOUR_TOKEN'

api = Instamojo(api_key=API_KEY, auth_token=AUTH_TOKEN, endpoint='https://test.instamojo.com/api/1.1/');
response = api.payment_request_create(
    amount='11',
    purpose='Testing',
    send_email=True,
    email="patelvirendra62@gmail.com",
    redirect_url="http://localhost:8000/handle_redirect"
    )

print( response['payment_request']['longurl'])