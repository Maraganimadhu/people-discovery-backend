Overview
This project is a Django REST Framework based People Discovery application. It supports authentication, profile management, interactions, and discovering people using secured APIs.
Tech Stack
- Django
- Django REST Framework
- MySQL
- JWT Authentication
- Postman (API Testing)
Step 1: User Login
![user login](C:\Users\Lenovo\OneDrive\Desktop\tech assign on djnago\output ss\login_png.png)
Endpoint: POST /auth/login/
Use Postman to login with valid credentials.
Response returns JWT access token.
Screenshot: login_success.png
Step 2: Authorization Setup
In Postman → Authorization tab:
Type: Bearer Token
Token: <JWT access token>
This token is required for all protected APIs.
Screenshot: bearer_token_setup.png
Step 3: Get / Create Profile
Endpoint: POST /profile/me/
If profile does not exist, it will be created.
Error Faced: age cannot be null.
Fix: Provide default age or make age nullable in model.
Screenshot: profile_500_error.png
Step 4: Profile Fix
Model Fix:
age = models.IntegerField(default=18)
Run makemigrations & migrate.
Screenshot: profile_fixed.png
Step 5: View Profile
Endpoint: GET /profile/me/
Returns logged-in user profile data.
Screenshot: profile_get_success.png
Step 6: Discover People
Endpoint: GET /discover/people/
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
