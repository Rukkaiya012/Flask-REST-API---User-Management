This is a simple RESTful API built with Flask that allows you to manage user data. 
It demonstrates the basic CRUD operations using in-memory storage (Python dictionary), without the use of a database.

🚀 Features
✅ Get all users
🔍 Get a specific user by ID
➕ Add a new user
✏️ Update an existing user
❌ Delete a user

🛠️ Technologies Used
Python 3
Flask
CURL or PowerShell (for testing API requests)

▶️ How to Run the Project
Make sure Python is installed.
Install Flask:
pip install flask
Save the following code as app.py.
Run the Flask server:
python app.py
The server will start at:
http://localhost:5000

📮 API Endpoints
Method	 Endpoint     	Description
GET	     /users    	    Get all users
GET	     /users/<id>  	Get user by ID
POST   	 /users	        Add new user
PUT    	 /users/<id>	  Update user by ID
DELETE 	 /users/<id>	  Delete user by ID

🧪 Testing the API with curl
✅ Get all users
curl http://127.0.0.1:5000/users

➕ Add a new user
Invoke-RestMethod -Uri "http://127.0.0.1:5000/users" `
  -Method POST `
  -Body '{"name":"Rani","email":"rani@example.com"}' `
  -ContentType "application/json"
OR
curl -X POST http://127.0.0.1:5000/users \
-H "Content-Type: application/json" \
-d "{\"name\":\"Rani\",\"email\":\"rani@example.com\"}"

🔍 Get user by ID
curl http://127.0.0.1:5000/users/1

✏️ Update user by ID
Invoke-RestMethod -Uri "http://127.0.0.1:5000/users/1" `
  -Method PUT `
  -Body '{"name":"Updated Name"}' `
  -ContentType "application/json"
  OR
  curl -X PUT http://127.0.0.1:5000/users/1 \
  -H "Content-Type: application/json" \
  -d "{\"name\":\"Updated Name\"}"

❌ Delete user by ID
Invoke-RestMethod -Uri "http://127.0.0.1:5000/users/1" -Method DELETE
OR
curl -X DELETE http://127.0.0.1:5000/users/1


📁 Folder Structure
.
├── app.py
└── README.md
