Overview
This project is a Django REST Framework based People Discovery application. It supports authentication, profile management, interactions, and discovering people using secured APIs.
Tech Stack
- Django
- Django REST Framework
- MySQL
- JWT Authentication
- Postman (API Testing)
  
👉Step 1: User register and login 
Endpoint: POST /auth/account/register/
![user register](https://github.com/Maraganimadhu/people-discovery-backend/blob/main/output%20ss/register_png.png)
![re-register](https://github.com/Maraganimadhu/people-discovery-backend/blob/main/output%20ss/re-register_png.png)
Endpoint: POST /auth/login/
![user login](https://github.com/Maraganimadhu/people-discovery-backend/blob/main/output%20ss/login_png.png)
Use Postman to login with valid credentials.
Response returns JWT access token.
Screenshot: login_success.png

👉Step 2: Authorization Setup
![Authorization Setup](https://github.com/Maraganimadhu/people-discovery-backend/blob/main/output%20ss/Authorization_Setup.png)
In Postman → Authorization tab:
Type: Bearer Token
Token: <JWT access token>
This token is required for all protected APIs.

👉Step 3: Get / Create Profile
Endpoint: POST /profile/me/
![create profile](https://github.com/Maraganimadhu/people-discovery-backend/blob/main/output%20ss/register_png.png)
If profile does not exist, it will be created.
Error Faced: age cannot be null.
Fix: Provide default age or make age nullable in model.
Screenshot: profile_500_error.png

👉Step 4: View Profile
Endpoint: GET /profile/me/
![get profile ](https://github.com/Maraganimadhu/people-discovery-backend/blob/main/output%20ss/get_profile.png)
Returns logged-in user profile data.
Screenshot: profile_get_success.png

👉Step 5: Discover People
Endpoint: GET /discover/people/
![empty reponse](https://github.com/Maraganimadhu/people-discovery-backend/blob/main/output%20ss/discover_empty.png.png)
![multiple respones](https://github.com/Maraganimadhu/people-discovery-backend/blob/main/output%20ss/multiple_users_existed_data.png)
Returns list of users excluding self.
Empty response [] means no other profiles exist.
Screenshot: discover_people_empty.png
Common Issues
401 Authentication credentials not provided:
- Missing Authorization header

500 Internal Server Error:
- Database constraint issues (age null)
Conclusion
All APIs work correctly after profile model fix and valid authentication. Screenshots above show each step execution order.

👉Step 6: Interaction API

The Interaction module allows users to express interest or skip other users.
All interaction APIs are JWT protected.
Endpoint: POST /interactions/
![intraction](https://github.com/Maraganimadhu/people-discovery-backend/blob/main/output%20ss/intraction_saved.png)
![re-intraction](https://github.com/Maraganimadhu/people-discovery-backend/blob/main/output%20ss/re-intraction.png)

Business Rules Enforced
- A user cannot interact with themselves
- A user cannot interact with the same person twice
- Every interaction is stored in the database
- Only authenticated users can perform interactions
