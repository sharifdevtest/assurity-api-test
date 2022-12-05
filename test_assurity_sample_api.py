# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #    
#                                                                                       #
#   Test script to verify the below acceptance criteria                                 #
#                                                                                       #
#   -   Name = "Carbon credits"                                                         #    
#   -   CanRelist = true                                                                #
#   -   The Promotions element with Name = "Gallery" has a                              #                                  
#       Description that contains the text "Good position in category"                  #
#                                                                                       #
#   Sample API -                                                                        #
#   URL = https://api.tmsandbox.co.nz/v1/Categories/6327/Details.json?catalogue=false   #
#                                                                                       #                                           
#   Author - Mohammad Sharif                                                            #
#                                                                                       #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import requests
import json

URL = "https://api.tmsandbox.co.nz/v1/Categories/6327/Details.json?catalogue=false"
response = requests.get(URL)
response_body = response.json()

# Additional check to verify the API end point 
def test_status_code(): 
    assert response.status_code == 200, "Response status code is not 200, {}".format(response.status_code) 

# Acceptancce Test 1    
def test_name():
    assert response_body['Name'] == "Carbon credits", "Name is invalid, got {}".format(response_body['Name']) 

# Acceptancce Test 2
def test_can_relist():
    assert response_body['CanRelist'] == True, "CanRelist is not True" 

# Acceptancce Test 3
def test_promotion_gallery_description():    
    element_found = False
    for element in response_body['Promotions']:
        if element['Name'] == "Gallery":
            assert element['Description'] == "Good position in category"
            element_found = True
            break

    assert element_found, "The Promotions element with Name = 'Gallery' not found"

# if __name__ == "__main__":
#     test_status_code()
#     test_name()
#     test_can_relist()
#     test_promotion_gallery_description()
