import os
import workos
import json
from django.conf import settings
from django.shortcuts import redirect, render
from django.urls import reverse
import requests

# Set the WorkOS API key and client ID from environment variables
workos.api_key = os.getenv("WORKOS_API_KEY")
workos.client_id = os.getenv("WORKOS_CLIENT_ID")

# Set the base API URL for WorkOS based on whether DEBUG is True or False in Django settings
workos.base_api_url = (
    "http://localhost:8000/" if settings.DEBUG else workos.base_api_url
)

# Constants
# Required: Fill in CUSTOMER_ORGANIZATION_ID for the desired organization from the WorkOS Dashboard
CUSTOMER_ORGANIZATION_ID = "org_01HB3XGX19T4PWXWEGN4W11B7A"
REDIRECT_URI = os.getenv("REDIRECT_URI")

# Render the login page
def login(request):
    # Check if the session is not active
    if request.session.get("session_active") is None:
        return render(request, "sso/login.html")

    # Check if the session is active and user is logged in
    if request.session.get("session_active"):
        return render(
            request,
            "sso/login_successful.html",
            {
                "p_profile": request.session.get("p_profile"),
                "first_name": request.session.get("first_name"),
                "last_name": request.session.get("last_name"),
                "raw_profile": json.dumps(request.session.get("raw_profile"), indent=2),
                "raw_attributes": json.dumps(request.session.get("raw_attributes"), indent=2),
            },
        )

    # If none of the above conditions are met, render a default login page
    return render(request, "sso/login.html")

# Set the WorkOS API key and client ID from Django settings
workos.api_key = settings.WORKOS_API_KEY
workos.client_id = settings.WORKOS_CLIENT_ID

# Retrieve directory sync data from the WorkOS API
def directory_sync_data(request):
    # Make the API call
    api_url = "https://api.workos.com/directory_users?directory=directory_01HB8S53EHXD314XA7XAGYMF65"
    headers = {
        "Authorization": "Bearer sk_test_a2V5XzAxSEIzWEQwM0hBUU5WRFBTN1paS1I1SjQwLDhxalFhVlZxVFExdVptMVpBNnNDU1dqSHE"
    }
    
    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()  # Raise an exception if the API request fails
        data = response.json()  # Parse the JSON response
    except requests.exceptions.RequestException as e:
        # Handle API request errors here, e.g., log the error
        print(f"API Request Error: {e}")
        data = {}  # Set data to an empty dictionary or handle error gracefully
    
    # Add the retrieved data to the context
    context = {
        "data": data,
    }

    # Print the data for debugging purposes
    print(data)

    # Render the template with the context
    return render(request, "sso/directory_sync_data.html", context)

# Handle user authentication
def auth(request):
    login_type = request.POST["login_method"]
    params = {"redirect_uri": REDIRECT_URI, "state": {}}

    if login_type == "saml":
        params["organization"] = CUSTOMER_ORGANIZATION_ID
    else:
        params["provider"] = login_type

    # Get the authorization URL for the selected login method
    authorization_url = workos.client.sso.get_authorization_url(**params)

    # Redirect the user to the authorization URL
    return redirect(authorization_url)

# Handle the callback after authentication
def auth_callback(request):
    code = request.GET["code"]
    profile = workos.client.sso.get_profile_and_token(code)
    p_profile = profile.to_dict()

    # Store user profile and session information
    request.session["p_profile"] = p_profile
    request.session["last_name"] = p_profile.get("last_name", "")
    request.session["first_name"] = p_profile["profile"]["first_name"]
    request.session["raw_attributes"] = p_profile["profile"]["raw_attributes"]
    request.session["raw_profile"] = p_profile["profile"]
    request.session["session_active"] = True

    # Redirect to the login page
    return redirect("login")

# Log out the user and clear the session
def logout(request):
    request.session.clear()
    return redirect("login")

