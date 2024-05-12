This is a backend application with CRUD APIs for managing assistants using Python Django framework.
The project includes defining database models, implementing API endpoints, testing with Postman.

●More Details-

● Implementing CRUD APIs (POST, GET, PUT, DELETE) for managing Assistants.
● Defining database model(s) for the Assistant, including applicable fields such as id, name, mobile, email, salary, city, country, department, role, etc.

● Implemented the following API endpoints:

● POST /assistant: Creates a new record in the database and returns
the id of the assistant.
● GET /assistant/<assistant_id>: Retrieves the details of the assistant
with the specified id.
● PUT /assistant/<assistant_id>: Updates the details of the assistant
with the specified id.
● DELETE /assistant/<assistant_id>: Deletes the record of the
assistant with the specified id.

●Postman Collection and Testing:

●Get- http://127.0.0.1:8000/assistant/id/
●Put- http://127.0.0.1:8000/assistant/id/
●Delete- http://127.0.0.1:8000/assistant/id/
●Post- http://127.0.0.1:8000/assistant/

●Project Screenshots-


![image](https://github.com/KaustubhBhavsar20/Assistant-Manager-Django/assets/114724744/6f10b80b-666e-4ba4-b13a-98ea5c7827f1)

![image](https://github.com/KaustubhBhavsar20/Assistant-Manager-Django/assets/114724744/3524a755-f70d-46d9-9f71-45ec7f79f9a6)

