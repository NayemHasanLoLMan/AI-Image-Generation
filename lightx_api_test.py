import requests

# # API endpoint and headers
# url = 'https://api.lightxeditor.com/external/api/v1/outfit'
# headers = {
#     'Content-Type': 'application/json',
#     'x-api-key': '4d2b892c537049d590ebd57afd9e5e63_c8b49c32d0f04da69d450dcedae2dd87_andoraitools'  # Replace with your actual API key
# }

# # Payload (replace with your specific input)
# data = {
#     #"imageUrl": "https://as1.ftcdn.net/v2/jpg/02/50/84/98/1000_F_250849890_qxH2MudfMq5AFSqHrOp5oA9NqykT14Ti.jpg",  # Replace with the URL of your input image
#     # "imageUrl": "C:/Users/hasan/Pictures/Screenshots/test.png",
#     "imageUrl": "https://wwd.com/wp-content/uploads/2023/07/GettyImages-1459019694.jpg",
#     "textPrompt": "a person wearing a modern black suit"  # Replace with your input prompt
# }

# try:
#     # Send POST request
#     response = requests.post(url, headers=headers, json=data)

#     # Check response status
#     if response.status_code == 200:
#         print("Request was successful!")
#         print("Response Data:", response.json())
#     else:
#         print(f"Request failed with status code: {response.status_code}")
#         print("Error Response:", response.text)

# except requests.exceptions.RequestException as e:
#     print("An error occurred:", e)







##############################################################################################################
'''New version'''
#############################################################################################################

import time
import requests

# # API endpoint and headers
# base_url = 'https://api.lightxeditor.com/external/api/v1/outfit'
# # https://api.lightxeditor.com/external/api/v1/outfit
# headers = {
#     'Content-Type': 'application/json',
#     'x-api-key': '4d2b892c537049d590ebd57afd9e5e63_c8b49c32d0f04da69d450dcedae2dd87_andoraitools'  # Replace with your actual API key
# }

# # Initial payload
# data = {
#     "imageUrl": "https://wwd.com/wp-content/uploads/2023/07/GettyImages-1459019694.jpg",
#     "textPrompt": "a person wearing a modern pink suit"  # Replace with your input prompt
# }

# try:
#     # Send initial POST request
#     response = requests.post(base_url, headers=headers, json=data)
#     if response.status_code == 200:
#         print("Request was successful!")
#         response_data = response.json()
#         order_id = response_data["body"]["orderId"]
#         print(f"Order ID: {order_id}")

#         # Poll the status endpoint
#         status_url = f'{base_url}/{order_id}'
#         while True:
#             status_response = requests.get(status_url, headers=headers)
#             if status_response.status_code == 200:
#                 status_data = status_response.json()
#                 status = status_data["body"]["status"]
#                 print(f"Current Status: {status}")

#                 if status == "completed":
#                     output_url = status_data["body"]["outputUrl"]
#                     print(f"Output Image URL: {output_url}")
#                     break
#                 elif status == "failed":
#                     print("The job failed to process.")
#                     break
#                 else:
#                     print("Processing... Retrying in 5 seconds.")
#                     time.sleep(5)
#             else:
#                 print(f"Failed to fetch status. Status code: {status_response.status_code}")
#                 print(status_response.text)
#                 break
#     else:
#         print(f"Request failed with status code: {response.status_code}")
#         print("Error Response:", response.text)

# except requests.exceptions.RequestException as e:
#     print("An error occurred:", e)


#########################
'''New version 3 with slight changese.'''
########################
import requests

url = 'https://api.lightxeditor.com/external/api/v1/outfit'
# headers = {
#     'Content-Type': 'application/json',
#     'x-api-key': '4d2b892c537049d590ebd57afd9e5e63_c8b49c32d0f04da69d450dcedae2dd87_andoraitools'  # Replace with your actual API key
# }

# # Initial payload
# data = {
#     "imageUrl": "https://wwd.com/wp-content/uploads/2023/07/GettyImages-1459019694.jpg",
#     "textPrompt": "a person wearing a modern pink suit"  # Replace with your input prompt
# }
# response = requests.post(url, headers=headers, json=data)

# # Check if the request was successful
# if response.status_code == 200:
#     print("Request was successful!")
#     print(response.json())
# else:
#     print(f"Request failed with status code: {response.status_code}")
#     print(response.text)



import requests
import json

# Define the URL and API key
url = 'https://api.lightxeditor.com/external/api/v1/order-status'
api_key = '4d2b892c537049d590ebd57afd9e5e63_c8b49c32d0f04da69d450dcedae2dd87_andoraitools'  # Replace with your actual API key

# Define the request body
payload = {
"orderId": "438b3615340b4d9ca652f645043663e2"  # Replace with your actual Order ID
}

# Set headers
headers = {
'Content-Type': 'application/json',
'x-api-key': api_key
}

# Make the POST request
response = requests.post(url, headers=headers, data=json.dumps(payload))

# Check for successful request
if response.status_code == 200:
# Print the response
    print("Response:", response.json())
else:
    print(f"Failed to retrieve order status. Status code: {response.status_code}, Response: {response.text}")