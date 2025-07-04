<div>

    <h1>Django Expense Tracker API</h1>

    
    <h2>Project Overview</h2>
    <p>A REST API for tracking personal expenses and incomes with JWT authentication.</p>
    
    <div class="image-placeholder">
        <img src="" alt="Folder Architecture" />
    </div>
    
    <h2>Core Features</h2>

        <li><strong>User Authentication</strong>: JWT token-based security</li>
        <li><strong>Expense/Income Tracking</strong>: Full CRUD operations</li>
        <li><strong>Tax Calculations</strong>: Support for both flat and percentage taxes</li>
        <li><strong>Data Isolation</strong>: Users only see their own records</li>
        <li><strong>Admin Access</strong>: Superusers can view all records</li>
    
    <h2>Database Models</h2>
    <h3>ExpenseIncome Model</h3>
    <p>
user → ForeignKey to User <br>
title → CharField (max 200 chars) <br>
description → TextField (optional) <br>
amount → DecimalField (10 digits, 2 decimal places) <br>
transaction_type → CharField (choices: 'credit', 'debit') <br>
tax → DecimalField (default 0)<br>
tax_type → CharField (choices: 'flat', 'percentage', default 'flat') <br>
created_at → DateTimeField (auto)<br>
updated_at → DateTimeField (auto)<br>
    </p>
    
    <h2>API Endpoints</h2>
    
    <h3>Authentication</h3>
    <table>
        <tr>
            <th>Endpoint</th>
            <th>Method</th>
            <th>Description</th>
        </tr>
        <tr>
            <td><code>/api/auth/register/</code></td>
            <td>POST</td>
            <td>User registration</td>
        </tr>
        <tr>
            <td><code>/api/auth/login/</code></td>
            <td>POST</td>
            <td>User login (returns JWT tokens)</td>
        </tr>
        <tr>
            <td><code>/api/auth/refresh/</code></td>
            <td>POST</td>
            <td>Refresh JWT token</td>
        </tr>
    </table>
    
    <h3>Expense/Income</h3>
    <table>
        <tr>
            <th>Endpoint</th>
            <th>Method</th>
            <th>Description</th>
        </tr>
        <tr>
            <td><code>/api/expenses/</code></td>
            <td>GET</td>
            <td>List records (paginated)</td>
        </tr>
        <tr>
            <td><code>/api/expenses/</code></td>
            <td>POST</td>
            <td>Create new record</td>
        </tr>
        <tr>
            <td><code>/api/expenses/{id}/</code></td>
            <td>GET</td>
            <td>Get specific record</td>
        </tr>
        <tr>
            <td><code>/api/expenses/{id}/</code></td>
            <td>PUT</td>
            <td>Update record</td>
        </tr>
        <tr>
            <td><code>/api/expenses/{id}/</code></td>
            <td>DELETE</td>
            <td>Delete record</td>
        </tr>
    </table>
    
    <div class="image-placeholder">
        [SCREENSHOT: Postman Collection Example]
    </div>
    
    <h2>Response Formats</h2>
    
    <h3>Single Record</h3>
    <pre>
{
    "id": 1,
    "title": "Grocery Shopping",
    "description": "Weekly groceries",
    "amount": 100.00,
    "transaction_type": "debit",
    "tax": 10.00,
    "tax_type": "flat",
    "total": 110.00,
    "created_at": "2025-01-01T10:00:00Z",
    "updated_at": "2025-01-01T10:00:00Z"
}
    </pre>
    
    <h3>Paginated List</h3>
    <pre>
{
    "count": 25,
    "next": "http://api/expenses/?page=2",
    "previous": null,
    "results": [
        {
            "id": 1,
            "title": "Grocery Shopping",
            "amount": 100.00,
            "transaction_type": "debit",
            "total": 110.00,
            "created_at": "2025-01-01T10:00:00Z"
        }
    ]
}
    </pre>
    
    <h2>Setup Instructions (Windows)</h2>
    
    <ol>
        <li>Download and install Python 3.8+, I have installed 5.2.4</li>
        <li>Install a code editor (recommend VS Code)</li>
        <li>Download and install Git</li>
        <li>Create a project folder and open in Git Bash</li>
        <li>Clone the repository: <code>git clone git_repository</code></li>
        <li>Install virtualenv globally: <code>pip install virtualenv</code></li>
        <li>Create virtual environment: <code>python -m venv myvenv</code></li>
        <li>Activate environment: <code>myvenv/Scripts/activate</code></li>
        <li>Navigate to project folder (where manage.py exists)</li>
        <li>Install requirements: <code>pip install -r requirements.txt</code></li>
        <li>Run the server: <code>python manage.py runserver</code></li>
    </ol>
    
    <div class="image-placeholder">
        [SCREENSHOT: Terminal Setup Process]
    </div>
    
    <h2>Testing with Postman</h2>
    <ol>
        <li>Download and install Postman</li>
        <li>Create a new collection</li>
        <li>Add requests for all endpoints</li>
        <li>Test authentication first (register → login → refresh)</li>
        <li>Then test CRUD operations with the received token</li>
    </ol>
    
    <h2>Success Criteria</h2>
    <ul>
        <li>✅ All CRUD operations work correctly</li>
        <li>✅ Proper user data isolation</li>
        <li>✅ JWT authentication implemented</li>
        <li>✅ Accurate tax calculations</li>
        <li>✅ Proper HTTP status codes</li>
        <li>✅ All test cases pass</li>
    </ul>
    
    <div class="image-placeholder">
        [SCREENSHOT: Test Results]
    </div>
    
    <h2>Technical Stack</h2>
    <ul>
        <li>Backend: Django + Django REST Framework</li>
        <li>Authentication: djangorestframework-simplejwt</li>
        <li>Database: SQLite (development)</li>
        <li>Python: 3.8+</li>
    </ul>
    
    <h2>HTTP Status Codes</h2>
    <ul>
        <li><code>200</code> OK - Successful GET/PUT</li>
        <li><code>201</code> Created - Successful POST</li>
        <li><code>204</code> No Content - Successful DELETE</li>
        <li><code>400</code> Bad Request - Invalid data</li>
        <li><code>401</code> Unauthorized - Authentication required</li>
        <li><code>403</code> Forbidden - Permission denied</li>
        <li><code>404</code> Not Found - Resource not found</li>
    </ul>

</div>