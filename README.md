# FlaskJWTBackend. Flask + MongoDB backend with JWT support.

This package contains a basic Flask based API with JWT support. As for the data storage, by default, the API exects that MongoDB is running locally at port 27017.

## Data format:

This API stores a collection of Users in the following format:

User
    {
      _id:        "type: string",
      "username": "type: string",
      "password": "type: string",
      "items":    "type: Item[ ]"
    }

Item
    {
      _id:       "type: string",
      item_name: "type: string"
    }
    
User objects are gathered in a collection called "users".

## Usage and endpoints

### <server_address>/registration
This endpoint allows adding a new user to the database. 
#### Expected Request: 
Request Type: POST

Payload: 

JSON: {
       "username": "type: string",
       "password": "type: string"
     }
              
#### Response: 
Status: 200;
JSON: {
       "msg": "User registration successful."
     }
          
#### Error Statuses:
400, 405

### <server_address>/login
This endpoint allows to login to the server and receive an access token for further use. 
#### Expected Request: 
Request Type: POST

Payload: 

JSON: {
       "username": "type: string",
       "password": "type: string"
     }
              
#### Response: 

Status: 200; 
JSON: {
       "msg": "Login successful. Logged as [username, type: string].", 
       "access_token": "[JWT access token, type: string]"
    } 
          
#### Error Statuses: 
400, 405

### <server_address>/items/new
This endpoint allows adding an item using the token obtained after a login.
#### Expected Request: 
Request Type: POST

Payload: 
Header: {"Autorization": "Bearer [JWT access token, type: string]"}
JSON: {
       "item_name": "type: string"
     }
              
#### Response: 

Status: 200; 
JSON: {
    "msg": "An item was added to user: [username, type: string].",
    "item": {
        "_id": "[item id, type: string]",
        "item_name": "[item content, type: string]"
    }
}
          
#### Error Statuses: 
400, 401, 405

### <server_address>/items/:id
This endpoint allows deleting an item using the item id and the token obtained after a login.
#### Expected Request: 
Request Type: DELETE

Payload: 
Header: {"Autorization": "Bearer [JWT access token, type: string]"}
Query string: id
              
#### Response: 

Status: 200; 
JSON: {
    'msg': 'Item successfully deleted: [item id, type: string]'
}
          
#### Error Statuses: 
400, 401, 404, 405

### <server_address>/items
This endpoint allows listing all items that belong to a user.
#### Expected Request: 
Request Type: GET

Payload: 
Header: {"Autorization": "Bearer [JWT access token, type: string]"}
              
#### Response: 

Status: 200; 
JSON: {"msg": "List of all items. User: [username, type: string].",
    "data": {
        "items": [
                    {
                      "_id": "[item id, type: string]",
                      "item_name": "[item content, type: string]"
                    },
                    ...
                 ]
        }
    }  
#### Error Statuses: 
400, 405

### <server_address>/users DEBUG ENDPOINT.
This endpoint allows listing all users and their items.
#### Expected Request: 
Request Type: GET

Payload: 
Header: None
              
#### Response: 

Status: 200; 
JSON: {"msg": "List of users.",
    "data": {
            "users": [
                        {
                          "_id": "[user id, type: string]", 
                          "username": "[username, type: string]",
                          "password": "[password, type: string]",
                          "items": [
                                    {
                                      "_id": "[item id, type: string]",
                                      "item_name": "[item content, type: string]"
                                    },
                                  ...
                                  ]
                        },
                        ...
                     ]
          }
      }
      
#### Error Statuses: 
400, 405

### <server_address>/ DEBUG ENDPOINT.
This endpoint allows checking the connection to the server.
#### Expected Request: 
Request Type: GET

Payload: 
Header: None
              
#### Response: 

Status: 200; 
JSON: {"msg": "Connection is OK"}
      
#### Error Statuses: 
405

## Codebase

The backend is written using the Flask framework which is linked with the MongoDB database.

The app folder contains all the files required to run the backend. Those include app/views.py that define the endpoints, app/resources.py which holds the functionality to
process the requests coming to those endpoints, app/config.py holds the app and database configurations, finally app/__init__.py initialises the required services. 

The "database" folder contains the file that defines data structures used in the database (app/database/models.py) and the service that processes all communications with MongoDB
(app/database/mongo_service.py)

The MongoDB database is supposed to be running locally and can be configured in app/config.py file.

app/requirements.txt contains the required dependencies.

To test the API is functioning correctly one may run tests_run.py which should test the server's state. Note that at the moment, not all the tests are ready.
However, the test principles were outlined in the corresponding file alongside the list that contains the layout of the work to be completed next (see tests_run.py and the next section
for further details).

## Further work

Although the core of the API has been implemented, there are still unimplemented parts such as described later. The idea behind this version is to show my logic of building code architectures and working with different aspects of programming such as code design, error handling, testing and more.

As for the parts that were not implemented those include: task 4 which was not completed due to the lack of time. Similarly, not all tests were finalised (TODO list can be found in the test_run.py), however this does not imply that the API was not fully tested, tests were completed using the Postman software.

## How to run. Suggested method.

1. Create a Flask project in PyCharm
2. Install the required dependencies
3. Run server_run.py
4. Test the server with tests_run.p
