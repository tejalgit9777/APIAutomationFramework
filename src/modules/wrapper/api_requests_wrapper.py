import  requests
import json

# requests.get()
# requests.post()
# requests.put()
# requests.delete()
# requests.patch()

def get_request(url,auth):
    response_data = requests.get(url= url,auth=auth)
    return response_data.json()

def get_booking_request2(url):
    response_data = requests.get(url= url)
    return response_data.status_code

def post_request(url,auth,headers,payload,in_json):
    post_response = requests.post(url= url,auth=auth,headers=headers,data=json.dumps(payload))
    if in_json is True:
        return post_response.json()
    return  post_response

def put_request(url,auth,headers,payload,in_json):
    put_response = requests.post(url= url,auth=auth,headers=headers,data=json.dumps(payload))
    if in_json is True:
        return put_response.json()
    return  put_response

def patch_request(url,auth,headers,payload,in_json):
    patch_response = requests.post(url= url,auth=auth,headers=headers,data=json.dumps(payload))
    if in_json is True:
        return patch_response.json()
    return  patch_response

def delete_request(url,auth,headers,payload,in_json):
    delete_response = requests.post(url= url,auth=auth,headers=headers,data=json.dumps(payload))
    if in_json is True:
        return delete_response.json()
    return  delete_response

