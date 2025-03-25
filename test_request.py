import requests

# Replace with your actual API key
api_key = "SG_776dee56a8261fcd"
url = "https://api.segmind.com/v1/fashion-ai"

# Prepare data and files
data = {
    'prompt': "a person wearing a black tux",
    'clothing': "topwear"
}

# Add the path to the image file
files = {
    'image': open(r"C:\Users\hasan\Pictures\Screenshots\Screenshot 2025-01-11 112759.png", 'rb')
}
# Add the API key in the headers
headers = {'x-api-key': api_key}

# Make the POST request
response = requests.post(url, data=data, files=files, headers=headers)

# Print the response
print(response.status_code)
print(response.content)  # Response will likely include the generated image or details
