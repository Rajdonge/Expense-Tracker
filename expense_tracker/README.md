<div>
  <h1 align="center">Django Expense Tracker API</h1>
  <br /><br />
  <h1>1. Introduction</h1>
  <p>
    The Django Expense Tracker API is a robust RESTful service built with Django REST Framework. 
    It provides secure user authentication and comprehensive expense/income tracking capabilities 
    with automatic tax calculations. The API follows REST principles and uses JWT tokens for 
    authentication, ensuring data security and proper access control.
  </p> <br>
  
  <h1>2. Key Features</h1><br>
  
  <h2>2.1 Secure Authentication</h2><br>
  <p>
    The API implements JWT (JSON Web Tokens) authentication with token refresh functionality. 
    Users can register, login, and maintain secure sessions. All protected endpoints require 
    valid JWT tokens in the Authorization header.
  </p><br>
  
  <h2>2.2 Data Isolation</h2><br>
  <p>
    Regular users can only access their own expense/income records, while superusers have 
    administrative access to all data. This is enforced at both the view and database query levels 
    for maximum security.
  </p><br>
  
  <h2>2.3 Automatic Tax Calculations</h2><br>
  <p>
    The API automatically calculates totals based on tax type (flat amount or percentage). 
    Business logic ensures accurate calculations: Flat Tax (Amount + Tax) or Percentage Tax 
    (Amount + (Amount × Tax ÷ 100)).
  </p><br>
  
  <h2>2.4 RESTful Design</h2><br>
  <p>
    Following REST conventions, the API provides proper HTTP status codes and consistent JSON 
    response formats. All CRUD operations are supported with pagination for list endpoints.
  </p><br>
  
  <h1>3. Technical Implementation</h1><br>
  
  <h2>3.1 Database Models</h2><br>
  <pre>
  ExpenseIncome Model:
  - user → ForeignKey to User
  - title → CharField (max 200 chars)
  - description → TextField (optional)
  - amount → DecimalField (10 digits, 2 decimal places)
  - transaction_type → CharField (choices: 'credit', 'debit')
  - tax → DecimalField (default 0)
  - tax_type → CharField (choices: 'flat', 'percentage', default 'flat')
  - created_at → DateTimeField (auto)
  - updated_at → DateTimeField (auto)
  </pre><br>
  
  <h2>3.2 API Endpoints</h2><br>
  <h3>Authentication</h3>
  <pre>
  POST /api/auth/register/ → User registration
  POST /api/auth/login/ → User login (returns JWT tokens)
  POST /api/auth/refresh/ → Refresh JWT token
  </pre>
  
  <h3>Expense/Income</h3>
  <pre>
  GET    /api/expenses/ → List records (paginated)
  POST   /api/expenses/ → Create new record
  GET    /api/expenses/{id}/ → Get specific record
  PUT    /api/expenses/{id}/ → Update record
  DELETE /api/expenses/{id}/ → Delete record
  </pre><br>
  
  <h1>4. Setup Instructions</h1><br>
  <ol>
    <li>Clone repository: <code>git clone [repository-url]</code></li>
    <li>Create virtual environment: <code>python -m venv venv</code></li>
    <li>Activate environment: <code>source venv/bin/activate</code> (Linux/Mac) or <code>venv\Scripts\activate</code> (Windows)</li>
    <li>Install dependencies: <code>pip install -r requirements.txt</code></li>
    <li>Run migrations: <code>python manage.py migrate</code></li>
    <li>Start server: <code>python manage.py runserver</code></li>
  </ol><br>
  
  <h1>5. Testing</h1><br>
  <p>
    The API includes comprehensive test coverage for:
  </p>
  ### Authentication Tests  
• User registration with valid data  
<img src="https://github.com/Rajdonge/Expense-Tracker/blob/main/expense_tracker/Testing%20Screenshots/Authentication%20Test/User%20Registration.jpg"/>

• User registration with duplicate email/username  
<img src="https://drive.google.com/file/d/1TqO2w8xIUz_2NduYQhwfvS0eoAa--1_Y/view?usp=sharing"/>

• User login with valid credentials  
<img src="https://drive.google.com/file/d/1d2cyjeilx2nzCn-8MV1Owe-ny9fa1PDu/view?usp=sharing"/>

• User login with invalid credentials  
<img src="https://drive.google.com/file/d/1cSruHcvrgJenxkkfD23dXtVmLC-QDdao/view?usp=sharing"/>

• Token refresh functionality  
<img src="https://drive.google.com/file/d/17rwATA6Fyg19bFtDUdHQx8jT3ihQ65Xr/view?usp=sharing"/>

• Access protected endpoint with valid token  
<img src="https://drive.google.com/file/d/1GaQdTy0sYrRtnPpPgnn06SjrD3iUAcoE/view?usp=sharing"/>

• Access protected endpoint without token  
<img src="https://drive.google.com/file/d/1JvITZCQYy6t5nFUSON4g-rGZm5h0ZN5E/view?usp=sharing"/>

### CRUD Operations Tests  
• Create expense/income record  
<img src="https://drive.google.com/file/d/1RYi5pHVXxTgMOiNF4qolAMjQ4L-VzJRc/view?usp=sharing"/>

• List user's own records only  
<img src="https://drive.google.com/file/d/1jJmOptoODE0YJAIyviH4on2hEuuBzBCu/view?usp=sharing"/>

• Retrieve specific record (own only)  
<img src="https://drive.google.com/file/d/1nPtBnhRYP8Zpvu3x1Ahuuy7gNgNaxbaP/view?usp=sharing"/>

• Update existing record (own only)  
<img src="https://drive.google.com/file/d/1KoB4zKVCfRh0TFdCYRRF_i3DjZhQhcbG/view?usp=sharing"/>

• Delete record (own only)  
<img src="https://drive.google.com/file/d/126cmGb7stpe2_YS9ikB37HoWzPDaU7EH/view?usp=sharing"/>

• Verify superuser can access all records  
<img src="https://drive.google.com/file/d/1RM97hUvnDiwsOQiUiu5UoTU1Q3OA40U8/view?usp=sharing"/>

### Business Logic Tests  
• Flat tax: Amount = 100, Tax = 10 → Total = 110  
<img src="https://drive.google.com/file/d/1CbKJkMq-XI3ic8MaN80oXON4xbSCiFPR/view?usp=sharing"/>

• Percentage tax: Amount = 100, Tax = 10% → Total = 110  
<img src="https://drive.google.com/file/d/1uXWE7JA-jZjHvWtxyEdteHNymCJIDtx7/view?usp=sharing"/>

• Zero tax: Amount = 100, Tax = 0 → Total = 100  
<img src="https://drive.google.com/file/d/1m4f0PGWuDSpLk6kVflGnwjk0938zULod/view?usp=sharing"/>

### Permission Tests  
• Regular user cannot access other users' records  
<img src="https://drive.google.com/file/d/1SlApY5n6PbKW9OaIgFNV20Bil3k_Q41H/view?usp=sharing"/>

• Superuser can access all records  
<img src="https://drive.google.com/file/d/1Ki_yNAhNvTVWAiSQu37H6F5im-o-erVP/view?usp=sharing"/>

• Unauthenticated requests are rejected  
<img src="https://drive.google.com/file/d/13kAdUFetAJavqAzu9xPUBHfqhQNYLRgv/view?usp=sharing"/>

  <p>
    Run tests with: <code>python manage.py test</code>
  </p><br>
  
  <strong>For detailed implementation, check all project files and their corresponding documentation.</strong>
</div>