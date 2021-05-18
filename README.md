# photography_sales
Backend server and database for managing online sales of photography rights on dreamstime.
# For Reviewer:
Heroku: https://photography-sales.herokuapp.com/

## Test suite
  there is a postman collection AND 
  two unittest files:
  test_app_admin_authentificatio.py
  test_app_visitor_authentificatio.py
  (configured to test on local database in models_test.py)

## Authentification
Two roles have been established:
- Visitor only with get:data permission
- Admin with all permissions: get:data, patch:data, post:data, delete:data


### In case of need:
- Admin token:(all access rights:)
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjB5SnU5T3lseXBZVVBjTWg4bVhaRSJ9.eyJpc3MiOiJodHRwczovL2ZlcmZpLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDk2NzNiNThhNDcwMzAwNjk4YmQzNmIiLCJhdWQiOiJwaG90b2dyYXBoeSIsImlhdCI6MTYyMTMzODA1NCwiZXhwIjoxNjIxNDI0NDU0LCJhenAiOiIxY3hMU01xbGxCdG83d0hrbFBOV1FtVWdIeUxyb3BDVyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmRhdGEiLCJnZXQ6ZGF0YSIsInBhdGNoOmRhdGEiLCJwb3N0OmRhdGEiXX0.R6bDMLvhk8s6t7rvIzXU8AEDf11Bx-6vw0ev8gz85VeUp8Xum1XHkOuzJGhNzQ1GOb2BvCx49UEQhIiOfakl0cLYZydonTlkChlUKnShlDsyotSyt6vrIRtes9p-rAh5Fjh3FW_tPA0GNLKD3sq-2h-XBb3_76X9Ceqx8wMbTsrXMgF4diIGp-iSlYBxHnvzDkj8GlOnrDzovxoQ8bTr6hoYW1tyuSKpUNgZE5HA0T5caxh9vIaGGh7DYLE_-K0PysAhqdtBGb4iEHnqjzBwcKm_Q2T4RCM6uiD8M-8QGqRlJFihHa5-Pdg5pju82Scm0KFaOO--2yR72bjN8nMKTA

- Visitor: (only read data: get:data)
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjB5SnU5T3lseXBZVVBjTWg4bVhaRSJ9.eyJpc3MiOiJodHRwczovL2ZlcmZpLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDhkYzE0YWQ0OTI5ZDAwNmE4ZDYxOTQiLCJhdWQiOiJwaG90b2dyYXBoeSIsImlhdCI6MTYyMTMzNTQ4MCwiZXhwIjoxNjIxNDIxODgwLCJhenAiOiIxY3hMU01xbGxCdG83d0hrbFBOV1FtVWdIeUxyb3BDVyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmRhdGEiXX0.f0UAOgPEmmNxRVvO69tPwv70BP_sPgtWl12MVZpdSYgedHcteSH8aptMvqTv1fTTn7aQgwDpZOfx9SE0qsEQuv0kxUlHkpzlJr2ueIXUcJn7rIrTgvAKBL9by9P6i5Kgk4Mx5THc0RtUSGsqClCnLIzsLQ4j3Nka8Ym2M76LISQsyJhGNP-r9SzgRehhZETIDEi9RexrDOCameQjaUFa4FZ4nalNb3tmq5ckuaEVe2LbDpz5jmaP7dMQICnHgK_4Lus88hgh5rAx_b5_4Uc3_OwZkBkx8LA_27E3VFmUMAxmMszRmGhJh5cQSZnQBB6DBqTsX-p9wTfs8cgwGqsQDQ

- Heroku DATABASE_URL: 
postgres://lfigvzfrjqtiit:488ea0cb4c40f1fef6787a0f49bf3f174a1f43de328616d278584467f1e3c2e2@ec2-54-74-35-87.eu-west-1.compute.amazonaws.com:5432/d54ml76mm6330

## Endpoints:
- GET ```/sales```

show data in  sales table

requires the 'get:data' permission

returns status code 200 and json 
```
{"success": True, "image_sales": all_sales}
```

- GET  ```/images```:

show data in image table

requires the 'get:data' permission

returns status code 200 and json

```
{"success": True, 
" all_images":  all_images}
```

- POST ```/data``` 

create a new row in the Sale or Image table

requires the 'post:data' permission

add jsonfile:
```
{   
    "create": "sale",
    "image_id": 2,
    "sales_date": "2020-05-08 09:52:30",
    "income": 0.9,
    "platform": "AdobeStock"
}
```


returns status code 200 and json

 ```
 {"success": True, "data": data}
 ```
  where data is an array containing only the newly created data

- DELETE ```/delete/<type>/<id>```

```
<type>: image or sale

<id>: id to be deleted
````
removes image or sale from table

requires the 'delete:data' permission

returns status code 200 and json 
```
{"success": True, 'type': type, 'id': id } 
```

- Patch  ```/data/<id>```
```
<id>: id to be changed
```
add jsonfile containing data:

```{   
    "patch": "sale",
    "image_id": 2,
    "sales_date": "2020-05-08 09:52:30",
    "income": 0.9,
    "platform": "AdobeStock"
}
```

changes image data or sales in table

requires the 'patch:data' permission

returns status code 200 and json
 ```
 {"success": True, 'data': data }
 ```

# Getting Started

## Installing Dependencies

### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by navigating to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=app
export FLASK_ENV=development
flask run
```