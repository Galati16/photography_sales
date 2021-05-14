# photography_sales
Backend server and database for managing online sales of photographies on dreamstime.
## For Reviewer:
Heroku: https://photography-sales.herokuapp.com/

#For the reviewer, who graced me with the unnecessary work of recreating the tokens:
#NOONE ASKED FOR A UNITTEST TEST SUIT FOR THE ENDPOINTS!!
#I had ADDED A POSTMAN COLLECTION CONTAINING ALL TESTSSCENARIOS as stated below!!

Two roles have been established:
Visitor only with get:data permission
NoeFerfi with all permissions: get:data, patch:data, post:data, delete:data
Test for different users have been set up in the postman collection within the application folder.

In case of need:
NoeFerfi token:
(all access rights:)
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjB5SnU5T3lseXBZVVBjTWg4bVhaRSJ9.eyJpc3MiOiJodHRwczovL2ZlcmZpLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDk2NzNiNThhNDcwMzAwNjk4YmQzNmIiLCJhdWQiOiJwaG90b2dyYXBoeSIsImlhdCI6MTYyMDk5ODM5NCwiZXhwIjoxNjIxMDg0Nzk0LCJhenAiOiIxY3hMU01xbGxCdG83d0hrbFBOV1FtVWdIeUxyb3BDVyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmRhdGEiLCJnZXQ6ZGF0YSIsInBhdGNoOmRhdGEiLCJwb3N0OmRhdGEiXX0.m5WbKR76XaFbQ9cfbPsrqDDaWoN2muRPWgKs6DzPnmCSqNaxk1LCyQcJXzANGNerMdYtbHg1w5gYs6MO4IF6k0L5QgUgtbCFTRwvHWYQziMVOhhcWPcADYg9dFb8rNibf0Z6oZ9GaYfSBuH95GOPp0QX2Eh2IRjB6b0OZ1bj-7QIxy0lKRn3Y6TgeDozu75PVyeHG4aTAG2V8VBddOiSUraqAR72_ArfXkRMV8xYjq18mAGAk897d5DjzfbcRDeJRxAniZtiwuIa2W8_oZGMKgmOKoMsZO64Cir5Xc40fF-TMo4f8Ep7Xut_3li_E89jLyWCpfkm_pD-WsDVTrrNRw

Visitor: (only read data: get:data)
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjB5SnU5T3lseXBZVVBjTWg4bVhaRSJ9.eyJpc3MiOiJodHRwczovL2ZlcmZpLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDhkYzE0YWQ0OTI5ZDAwNmE4ZDYxOTQiLCJhdWQiOiJwaG90b2dyYXBoeSIsImlhdCI6MTYyMDk5Nzg1MCwiZXhwIjoxNjIxMDg0MjUwLCJhenAiOiIxY3hMU01xbGxCdG83d0hrbFBOV1FtVWdIeUxyb3BDVyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmRhdGEiXX0.abvdjfwQp4ihSHgTyxUAbqCUjfg_JR1dN3DrhjyrjKJ_fVvdq3WgAeF9JXDwY6R98-b6iSLeAHGWxUptWfrxwG-es9QpmMrAxl5kpKjFLU4VC1D6DJ4HZo2HKkrw2ZAgE69BkCXAikPGvA1_BA9ON038isKLxMsTtoZmfjbVXvvKpXIYe9xmQteMDYw6PpbHH1IZbWT3R1tMCxT_z7-UidI_r8PVuDvQxiFB0Z-l9sOYz-uhlbv42rV8EY7L9EB6qfh1OGPk29L7Kqq_Nx8vjDdSAYiFQOFeiIW8Wi4u3tP71__CX05duChtSxIM-tNtKNg6sG8EDkp1dn-ZJvPsaA

Heroku DATABASE_URL: postgres://lfigvzfrjqtiit:488ea0cb4c40f1fef6787a0f49bf3f174a1f43de328616d278584467f1e3c2e2@ec2-54-74-35-87.eu-west-1.compute.amazonaws.com:5432/d54ml76mm6330

## Endpoints:
- GET /sales 
show data in  sales table
requires the 'get:data' permission
returns status code 200 and json {"success": True, "image_sales": all_sales} 
-GET  /images:
show data in image table
requires the 'get:data' permission
returns status code 200 and json {"success": True, " all_images":  all_images} 
-POST /data, add jsonfile:
'''{   
    "create": "sale",
    "image_id": 2,
    "sales_date": "2020-05-08 09:52:30",
    "income": 0.9,
    "platform": "AdobeStock"
}'''
create a new row in the Sale or Image table
requires the 'post:data' permission
returns status code 200 and json {"success": True, "data": data} where data is an array containing only the newly created data
- DELETE /delete/<type>/<id>
<type>: image or sale
<id>: id to be deleted
removes image or sale from table
requires the 'delete:data' permission
returns status code 200 and json {"success": True, 'type': type, 'id': id } 
- POST /data/<id> 
add jsonfile containing data:
'''{   
    "patch": "sale",
    "image_id": 2,
    "sales_date": "2020-05-08 09:52:30",
    "income": 0.9,
    "platform": "AdobeStock"
}'''
<id>: id to be changed
changes image data or sales in table
requires the 'patch:data' permission
returns status code 200 and json {"success": True, 'data': data }

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Environment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virtual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

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
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```