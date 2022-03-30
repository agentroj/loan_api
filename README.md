**Loan Calculator API**

**Description:**


**Running the Loan Calculator API on dev:**

1. Clone the repository using the git command:
git clone <SSH or HTTP address>

2. Build and start the Docker image:
docker compose build && docker compose up
Note: you may use the extension "-d" if you want to access the docker console only via CLI

3. Migrate databases:
docker-compose  run --rm app sh -c "python manage.py makemigrations" 
docker-compose  run --rm app sh -c "python manage.py migrate" 

4. Create ad admin account:
    Open the Docker CLI and type the command below:
        docker-compose  run --rm app sh -c "python manage.py createsuperuser" 

5. You may download Postman and set the parameters below:
    Request Type: POST
    URL: http://0.0.0.0:8080/loan_calculator/
    Reqeust Body: { 
        "first_name":"Rick", 
        "middle_name":"Harold", 
        "last_name":"Grimes:", 
        "loan_amount":10000, 
        "loan_term":12
    }
 
6. You may confirm if the data has beena added on the Database by accessing the Django admin ORM dashboard 
Open the Web app with the URL below:
    localhost:8080/admin/
