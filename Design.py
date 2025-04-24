from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)

# Your Segmind API key
API_KEY = "API KEY"
SEGMENT_API_URL = "https://api.segmind.com/v1/fashion-ai"

@app.route('/')
def home():
    return render_template('index.html')  # HTML frontend for user input

@app.route('/generate', methods=['POST'])
def generate_clothing():
    # Get user inputs from the form
    prompt = request.form.get('prompt')
    clothing_type = request.form.get('clothing_type')
    image = request.files.get('image')  # Get the uploaded image file

    # Prepare the headers
    headers = {'x-api-key': API_KEY}

    # Prepare the data payload
    data = {
        "prompt": prompt,
        "clothing": clothing_type
    }

    # Prepare the files payload
    files = {'image': image} if image else None

    try:
        # Send request to the API
        response = requests.post(
            SEGMENT_API_URL,
            data=data,
            files=files,
            headers=headers
        )

        # Debugging logs
        print("Request Headers:", headers)
        print("Request Data:", data)
        print("Response Status Code:", response.status_code)
        print("Response Text:", response.text)

        # Handle successful response
        if response.status_code == 200:
            image_url = response.json().get('image_url', 'No URL provided')
            return jsonify({"success": True, "image_url": image_url})
        else:
            # Handle API errors
            return jsonify({"success": False, "error": response.text}), response.status_code
    except requests.exceptions.RequestException as e:
        # Handle network errors
        print("Network error:", str(e))
        return jsonify({"success": False, "error": "Network error. Please try again later."}), 500
    except Exception as e:
        # Handle unexpected exceptions
        print("Unexpected error:", str(e))
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
