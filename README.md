# WorkOS_SSO_DirectorySync_Application
An SSO and directory sync application setup with Okta and synced with WorkOS

**WorkOS Django SSO and Directory Sync Example**

**Prerequisites**

Before setting up and running this Django application for Single Sign-On (SSO) authentication with WorkOS, ensure you have the following prerequisites:

- Python 3.6+
- Access to the WorkOS Admin Portal

**Getting Started**

1. Clone the main git repository for these Python example applications using your preferred method (HTTPS or SSH):

   ```bash
   # HTTPS
   $ git clone https://github.com/alanjdbuckley/WorkOS_SSO_DirectorySync_Application.git
   ```

2. Navigate to the "python-django-sso-example" directory within the cloned repository:

   ```bash
   $ cd python-django-example-applications/python-django-sso-example
   ```

3. Create and activate a Python virtual environment:

   ```bash
   $ python3 -m venv env
   $ source env/bin/activate
   ```

   You should see "(env)" at the beginning of your command-line prompt when the virtual environment is activated.

4. Install the application's dependencies:

   ```bash
   (env) $ pip install -r requirements.txt
   ```

5. Obtain and make note of the following values, as they will be set as environment variables in the next steps:

   - Your [WorkOS API key](https://dashboard.workos.com/signin?redirect=/api-keys)
   - Your [SSO-specific WorkOS Client ID](https://dashboard.workos.com/signin?redirect=/sso/configuration)
   - The redirect URI (for this example, we'll use http://localhost:8000/auth/callback)

6. Create a `.env` file in the root directory of the example app to securely store the environment variables:

   ```bash
   (env) $ touch .env
   ```

7. Open the `.env` file using a text editor like Nano:

   ```bash
   (env) $ nano .env
   ```

8. Add the environment variables to the `.env` file:

   ```bash
   export WORKOS_API_KEY=<your WorkOS API key>
   export WORKOS_CLIENT_ID=<your WorkOS Client ID>
   export REDIRECT_URI='http://localhost:8000/auth/callback'
   ```

   To exit Nano, press `CTRL + X`, confirm the save with `Y`, and press `Enter`.

9. Source the environment variables to make them accessible to the operating system:

   ```bash
   (env) $ source .env
   ```

10. Verify that the environment variables were set correctly:

    ```bash
    (env) $ echo $WORKOS_API_KEY
    (env) $ echo $WORKOS_CLIENT_ID
    (env) $ echo $REDIRECT_URI
    ```

**Running the Application**

11. Run Django migrations from the "python-django-sso-example/" directory, where the `manage.py` file is located:

    ```bash
    (env) $ python3 manage.py migrate
    ```

    You should see migration operations being applied without any errors.

12. In the "python-django-sso-example/sso/views.py" file:

    *  Update the `ORGANIZATION_ID` string value to match the organization ID you are targeting on line 20.  You can find this ID in the WorkOS Dashboard under Organization Settings.
    *  You will also need to update (on line 53 and 55) both your `API Key`  (which should contain your `Directory_ID` ) and `Bearer Token`  so an API call can be made to retrieve Active Directory Users. These values can be found in your WorkOS dashboard under your Organisation -> Diretcory Sync connection. 

14. Start the server:

    ```bash
    (env) $ python3 manage.py runserver --insecure
    ```

    You'll know the server is running when you see no warnings or errors in the CLI, and it displays output similar to the following:

    ```
    Watching for file changes with StatReloader
    Performing system checks...
    
    System check identified no issues (0 silenced).
    March 18, 2021 - 04:54:50
    Django version 3.1.7, using settings 'workos_django.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.
    ```

15. Open your web browser and navigate to "http://localhost:8000." You should see a "Login" link. Note that clicking this link will currently redirect you to an HTTP 404 page since SSO hasn't been set up yet.

16. To stop the local Django server, press `CTRL + C` in the command line.

**Setting up SSO and Directory Sync with WorkOS**

16. SSO : Follow the [SSO authentication flow instructions](https://workos.com/docs/sso/introduction)  provided to set up an SSO connection. When you reach the step where you need to provide the `REDIRECT_URI` value, use "http://localhost:8000/auth/callback."
17. Directory Sync: Follow the [Directory Sync Instructions](https://workos.com/docs/integrations/okta-scim) to create a Directory Sync connections. Feel free to set up a few user accounts for demo purposes. 

18. If you encounter any issues during the SSO setup, don't hesitate to reach out to us at support@workos.com for assistance.

**Testing the Integration**

19. Navigate to the "python-django-sso-example" directory that contains the `manage.py` file.

20. Source the virtual environment you created earlier (if it isn't still activated):

    ```bash
    $ cd ~/Desktop/python-django-sso-example/
    $ source env/bin/activate
    ```

21. Start the Django server locally:

    ```bash
    (env) $ python3 manage.py runserver
    ```

22. Once the server is running, visit "http://localhost:8000" in your web browser to test the SSO workflow.

------------------------------------------------------------------------------------------------------------------
**ScreenShots of what to expect once the application is running:**

1. Navigate to "http://localhost:8000" and select Enterprise SAML 

<img width="1724" alt="Login" src="https://github.com/alanjdbuckley/WorkOS_SSO_DirectorySync_Application/assets/146522264/145c5145-e6af-4fcf-af09-ce80c1282165">


2. Okta Verification 

<img width="588" alt="Okta Sign In " src="https://github.com/alanjdbuckley/WorkOS_SSO_DirectorySync_Application/assets/146522264/713c6fed-9e99-42bf-9f98-b4b3d044e90b">


3. Welcome Screen showing your details from the IDP. Then click on the "Directory Sync Data" button

<img width="1709" alt="Welcome Page with Name" src="https://github.com/alanjdbuckley/WorkOS_SSO_DirectorySync_Application/assets/146522264/42d09353-df80-40ab-8a99-a64ccd3a0fbc">

4. Directory Sync Data 

<img width="1715" alt="Directoey Sync Data" src="https://github.com/alanjdbuckley/WorkOS_SSO_DirectorySync_Application/assets/146522264/1d3f6143-75b4-455f-a6c0-62c298de6685">

Congratulations! You've successfully set up and tested the SSO and Directory Sync applicatiopn using the WorkOS Python SDK with this Django example application.
