# AdminInterface

# App structure

There are 2 django apps 
- adminapp - App designed to render into templates
- adminApiapp - This gives API endpoints based on the requirements

## How to run the app
- Go to the terminal navigate to the django project directory to manage.py file position
- pip install -r requirements.txt
- Since there is no register interface the db used is sqlite which is attached to the project. So no db setup is required.
- to run the app run the command : 
    - python manage.py runserver
    - python manage.py runserver 0.0.0.0:<port_num> (to run in a specific port)

# Users added

username - TESTUSER 1
password - Testuser1

username - TESTUSER 2
password - Testuser2

username - TESTUSER 3
password - Testuser3

For adding a new user -

Go to the terminal navigate to the django project directory to manage.py file position
run the following commands
- python manage.py shell

```
from adminapp.models import User

add_user = User.objects.create_user('<username>','','<password>',is_active=1,is_superuser=1)
add_user.save()
exit()

```
## Things to note

- The api endpoint structure - api/<endpoint>
- template render app structure - /<endpoint>
- pass the access token from the response to each endpoint for authentication - adminApiapp
- format to add a new customer/invoice through api call - adminAPIapp

CUSTOMER

```
{   "user":"<logged_user_id>",
    "name":"<customer_nm>",
    "phone":"<phone>",
    "email":"<email>",
    "Address":"<address>"

}

```
INVOICE

```
{
    "user":"<logged_user_id>",
    "customer":<available_cust_id_of_logged_userlist>,
    "date":"<date>",
    "amount":200000,
    "Status":"Unpaid"
}

```