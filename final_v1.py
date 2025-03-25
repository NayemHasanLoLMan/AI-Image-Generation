'''Last try for before after noon'''

import requests
import json
import time

# API key
api_key = '4d2b892c537049d590ebd57afd9e5e63_c8b49c32d0f04da69d450dcedae2dd87_andoraitools'

def get_order_status():
    # Step 1: Send the initial request to get the order ID
    outfit_url = 'https://api.lightxeditor.com/external/api/v1/outfit'
    headers = {
        'Content-Type': 'application/json',
        'x-api-key': api_key
    }
    data = {
        "imageUrl": "https://wwd.com/wp-content/uploads/2023/07/GettyImages-1459019694.jpg",
        "textPrompt": "a person wearing a modern pink-white longa suit"
    }

    try:
        # Send POST request
        response = requests.post(outfit_url, headers=headers, json=data)

        if response.status_code == 200:
            print("Request was successful!")
            response_data = response.json()
            order_id = response_data['body']['orderId']
            print(f"Order ID: {order_id}")
        else:
            print(f"Request failed with status code: {response.status_code}")
            print("Error Response:", response.text)
            return None
    except requests.exceptions.RequestException as e:
        print("An error occurred while creating the order:", e)
        return None

    # Step 2: Poll the order status
    status_url = 'https://api.lightxeditor.com/external/api/v1/order-status'
    payload = {"orderId": order_id}

    try:
        while True:
            # Send POST request to check status
            status_response = requests.post(status_url, headers=headers, data=json.dumps(payload))

            if status_response.status_code == 200:
                status_data = status_response.json()
                print("Order Status Response:", status_data)
                status = status_data['body']['status']

                if status == "completed":
                    print("Processing completed!")
                    print("Output URL:", status_data['body']['outputUrl'])
                    return status_data
                elif status == "failed":
                    print("Processing failed!")
                    return status_data
                else:
                    print(f"Current Status: {status}. Retrying in 5 seconds...")
                    time.sleep(5)
            else:
                print(f"Failed to retrieve order status. Status code: {status_response.status_code}, Response: {status_response.text}")
                return None

    except requests.exceptions.RequestException as e:
        print("An error occurred while checking the order status:", e)
        return None


# Call the merged function
result = get_order_status()
print("Final Result:", result)
