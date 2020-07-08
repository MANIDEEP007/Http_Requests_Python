'''
Module to Get the Public Information of a GitHub Exisiting User
'''
import requests #To make Http Requests
#To Save Image data of response - pip install pillow
from PIL import Image
#Read Image as Raw bytes and save it
from io import BytesIO

#Take UserName as Input
USERNAME = input("Enter GitHub UserName to get your public information:")

URL = "https://api.github.com/users/" + USERNAME

#GET Http Request - Returns requests.Reponse Object
response = requests.get(
    url = URL,
    )

#Needed Keys as Per API Response
KEYS_USER_INFO =(
    "name",
    "company",
    "location",
    "followers",
    "following",
    )

#Parse Response if request is succesful
if response.status_code == 200:
    print("User %s Exists" %(USERNAME,))
    print("Data of User %s" %(USERNAME,))
    '''Check Response Content is Json or Not
    If Response is Json, Get Necessary Details'''
    if "json" in response.headers.get("content-type"):
        print('*' * 60)
        for each_key in KEYS_USER_INFO:
            if response.json().get(each_key):
                print(
                        each_key.capitalize(),
                        ":",
                        response.json().get(each_key)
                      )
        print('*' * 60)
        #Download the Profile Picture if exists publicly
        avatar_url = response.json()["avatar_url"]
        if avatar_url:
            avatar_response = requests.get(
                url = avatar_url,
                )
            #Check Response Content is Image
            if "image" in avatar_response.headers.get("content-type"):
                image_data = Image.open(BytesIO(avatar_response.content))
                image_data.save(response.json().get("name","Default") + ".jpeg")
else:
    print("User %s Not Found" %(USERNAME,))
