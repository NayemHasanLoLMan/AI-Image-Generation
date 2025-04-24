import time
import requests
import json

# API key
api_key = 'API KEY'

def process_image_and_save():
    # Step 1: Send the initial request to get the order ID
    outfit_url = 'https://api.lightxeditor.com/external/api/v1/outfit'
    headers = {
        'Content-Type': 'application/json',
        'x-api-key': api_key
    }
    data = {
        "imageUrl": "https://wwd.com/wp-content/uploads/2023/07/GettyImages-1459019694.jpg",
        "textPrompt": "a person wearing a colorful shorts and T-shirts "
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

                if status == "completed" or status == "active":
                    output_url = status_data['body']['output']
                    print(f"Output URL: {output_url}")

                    # Download the image
                    img_response = requests.get(output_url)
                    if img_response.status_code == 200:
                        with open("output_image.jpg", "wb") as f:
                            f.write(img_response.content)
                        print("Output image saved as 'output_image.jpg'")
                    else:
                        print("Failed to download the image.")
                    return  # Exit the loop and function after successful generation

                elif status == "failed":
                    print("Processing failed!")
                    return
                else:
                    print(f"Current Status: {status}. Retrying in 5 seconds...")
                    time.sleep(5)
            else:
                print(f"Failed to retrieve order status. Status code: {status_response.status_code}, Response: {status_response.text}")
                return

    except requests.exceptions.RequestException as e:
        print("An error occurred while checking the order status:", e)
        return


# Call the function
process_image_and_save()
