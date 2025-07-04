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
  <ul>
    <li>Authentication flows</li>
    <li>CRUD operations</li>
    <li>Tax calculations</li>
    <li>Permission checks</li>
  </ul>
  <p>
    Run tests with: <code>python manage.py test</code>
  </p><br>
  
  <strong>For detailed implementation, check all project files and their corresponding documentation.</strong>
</div>