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
   <h2>### Authentication Tests</h2>  
<strong>• User registration with valid data </strong> <br>
<img src="https://github.com/Rajdonge/Expense-Tracker/blob/main/expense_tracker/Testing%20Screenshots/Authentication%20Test/User%20Registration.jpg" width="700px"/><br><br><hr>

<strong>• User registration with duplicate email/username  </strong><br>
<img src="https://github.com/Rajdonge/Expense-Tracker/blob/main/expense_tracker/Testing%20Screenshots/Authentication%20Test/Duplicate%20User%20Registration.jpg" width="700px"/><br><br><hr>

<strong>• User login with valid credentials  </strong><br>
<img src="https://github.com/Rajdonge/Expense-Tracker/blob/main/expense_tracker/Testing%20Screenshots/Authentication%20Test/Login%20with%20valid%20user%20credentials.jpg" width="700px"/><br><br><hr>

<strong>• User login with invalid credentials </strong> <br>
<img src="https://github.com/Rajdonge/Expense-Tracker/blob/main/expense_tracker/Testing%20Screenshots/Authentication%20Test/Login%20with%20invalid%20login%20credential.jpg" width="700px"/><br><br><hr>
<strong>• Token refresh functionality </strong> <br>
<img src="https://github.com/Rajdonge/Expense-Tracker/blob/main/expense_tracker/Testing%20Screenshots/Authentication%20Test/Refresh%20JWT%20Token.jpg" width="700px"/><br><br><hr>

<strong>• Access protected endpoint with valid token </strong> <br>
<img src="https://github.com/Rajdonge/Expense-Tracker/blob/main/expense_tracker/Testing%20Screenshots/Authentication%20Test/Access%20protected%20endpoint%20with%20valid%20token.jpg" width="700px"/><br><br><hr>

<strong>• Access protected endpoint without token  </strong><br>
<img src="https://github.com/Rajdonge/Expense-Tracker/blob/main/expense_tracker/Testing%20Screenshots/Authentication%20Test/Access%20protected%20endpoint%20without%20token.jpg" width="700px"/><br><br><hr>

<h2>### CRUD Operations Tests </h2> 
<strong>• Create expense/income record </strong> <br>
<img src="https://github.com/Rajdonge/Expense-Tracker/blob/main/expense_tracker/Testing%20Screenshots/Crud%20Operation%20Test/Create%20expense%20or%20income%20record.jpg" width="700px"/><br><br><hr>

<strong>• List user's own records only </strong> <br>
<img src="https://github.com/Rajdonge/Expense-Tracker/blob/main/expense_tracker/Testing%20Screenshots/Crud%20Operation%20Test/List%20user's%20own%20records%20only.jpg" width="700px"/><br><br><hr>

<strong>• Retrieve specific record (own only)  </strong><br>
<img src="https://github.com/Rajdonge/Expense-Tracker/blob/main/expense_tracker/Testing%20Screenshots/Crud%20Operation%20Test/Retrieve%20specific%20record%20(own%20only).jpg" width="700px"/><br><br><hr>

<strong>• Update existing record (own only)  </strong><br>
<img src="https://github.com/Rajdonge/Expense-Tracker/blob/main/expense_tracker/Testing%20Screenshots/Crud%20Operation%20Test/Update%20existing%20record%20(own%20only).jpg" width="700px"/><br><br><hr>

<strong>• Delete record (own only)  </strong><br>
<img src="https://github.com/Rajdonge/Expense-Tracker/blob/main/expense_tracker/Testing%20Screenshots/Crud%20Operation%20Test/Delete%20record%20(own%20only).jpg" width="700px"/><br><br><hr>

<strong>• Verify superuser can access all records </strong> <br>
<img src="https://github.com/Rajdonge/Expense-Tracker/blob/main/expense_tracker/Testing%20Screenshots/Crud%20Operation%20Test/Superuser%20login.jpg"/><br>
<img src="https://github.com/Rajdonge/Expense-Tracker/blob/main/expense_tracker/Testing%20Screenshots/Crud%20Operation%20Test/Verify%20superuser%20can%20access%20all%20records.jpg" width="700px"/><br><br><hr>

<h2>### Business Logic Tests </h2>
<strong>• Flat tax: Amount = 100, Tax = 10 → Total = 110 </strong> <br>
<img src="https://github.com/Rajdonge/Expense-Tracker/blob/main/expense_tracker/Testing%20Screenshots/Business%20Logic%20Test/q-1.jpg" width="700px"/><br><br><hr>

<strong>• Percentage tax: Amount = 100, Tax = 10% → Total = 110 </strong> <br>
<img src="https://github.com/Rajdonge/Expense-Tracker/blob/main/expense_tracker/Testing%20Screenshots/Business%20Logic%20Test/q-2.jpg" width="700px"/><br><br><hr>

<strong>• Zero tax: Amount = 100, Tax = 0 → Total = 100 </strong> <br>
<img src="https://github.com/Rajdonge/Expense-Tracker/blob/main/expense_tracker/Testing%20Screenshots/Business%20Logic%20Test/q-3.jpg" width="700px"/><br><br><hr>

<h2>### Permission Tests </h2>
<strong>• Regular user cannot access other users' records  </strong><br>
<img src="https://github.com/Rajdonge/Expense-Tracker/blob/main/expense_tracker/Testing%20Screenshots/Permission%20Test/Regular%20user%20cannot%20access%20other%20users'%20records.jpg" width="700px"/><br><br><hr>

<strong>• Superuser can access all records </strong> <br>
<img src="https://github.com/Rajdonge/Expense-Tracker/blob/main/expense_tracker/Testing%20Screenshots/Permission%20Test/Superuser%20can%20access%20all%20records.jpg" width="700px"/><br><br><hr>

<strong>• Unauthenticated requests are rejected  </strong><br>
<img src="https://github.com/Rajdonge/Expense-Tracker/blob/main/expense_tracker/Testing%20Screenshots/Permission%20Test/Unauthenticated%20requests%20are%20rejected.jpg" width="700px"/><br><br><hr>

  <p>
    Run tests with: <code>python manage.py test</code>
  </p><br>
  
  <strong>For detailed implementation, check all project files and their corresponding documentation.</strong>
</div>