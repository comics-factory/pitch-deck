from flask import Flask, jsonify, send_file, request, redirect
import os
from datetime import datetime

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account or Application Default Credentials
# When running on Firebase App Hosting/Cloud Run, use Application Default Credentials
if os.path.exists('serviceAccountKey.json'):
    cred = credentials.Certificate('serviceAccountKey.json')
else:
    # Use Application Default Credentials (automatically provided by App Hosting)
    cred = credentials.ApplicationDefault()

# Initialize Firebase
firebase_app = firebase_admin.initialize_app(cred)
db = firestore.client()

app = Flask(__name__)

# In-memory storage for email subscriptions (for demo purposes)
waitlist_ref = db.collection("waitlist-email")

@app.route("/")
def index():
    return send_file('src/index.html')

@app.route("/result")
def result():
    """Serves the result page that displays the PDF."""
    return send_file('src/result.html')

@app.route('/public/favicon.svg')
def favicon():
    return send_file('public/favicon.svg', mimetype='image/svg+xml')

@app.route('/public/hesdi.jpg')
def sample_photo():
    return send_file('public/hesdi.jpg', mimetype='image/jpeg')

@app.route('/public/qr_code.png')
def qr_code():
    return send_file('public/qr_code.png', mimetype='image/png')

@app.route('/subscribe', methods=['POST'])
def subscribe():
    """Handle email subscription to the waiting list"""
    try:
        data = request.get_json()
        email = data.get('email', '').strip()
        
        if not email:
            return jsonify({"error": "Email is required"}), 400
        
        # Basic email validation
        if '@' not in email or '.' not in email:
            return jsonify({"error": "Please enter a valid email address"}), 400
                
        # Add email to the list
        email_ref = waitlist_ref.document()
        email_ref.set({"email": email})

        # Log the subscription
        print(f"New subscription: {email} at {datetime.now()}")
        
        return jsonify({
            "message": "Successfully subscribed to the waiting list!",
            "email": email
        }), 200
        
    except Exception as e:
        print(f"Error in subscribe: {str(e)}")
        return jsonify({"error": "An error occurred. Please try again."}), 500

def main():
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 80)))

if __name__ == "__main__":
    main()
