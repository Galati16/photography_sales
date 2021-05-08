# photography_sales
Backend server and database for managing online sales of photographies on dreamstime.
## For Reviewer:
Two roles have been established:
Visitor only with get:data permission
NoeFerfi with all permissions: get:data, patch:data, post:data, delete:data
Test for different users have been set up in the postman collection within the application folder.

In case of need:
NoeFerfi token:
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjB5SnU5T3lseXBZVVBjTWg4bVhaRSJ9.eyJpc3MiOiJodHRwczovL2ZlcmZpLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDk2NzNiNThhNDcwMzAwNjk4YmQzNmIiLCJhdWQiOiJwaG90b2dyYXBoeSIsImlhdCI6MTYyMDQ3MjkxMiwiZXhwIjoxNjIwNTU5MzEyLCJhenAiOiIxY3hMU01xbGxCdG83d0hrbFBOV1FtVWdIeUxyb3BDVyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmRhdGEiLCJnZXQ6ZGF0YSIsInBhdGNoOmRhdGEiLCJwb3N0OmRhdGEiXX0.EvJpBgn8CtYJ_h3pysNb7x6VxVOEmBWtU1jmJdmLN73qS3NFdhyfeVsWsPJRfZdlzw8drIZbdOS_zwS1EzxUadPNyiaIGu36eMa3raGu0bApwWQL0uzMbN99_x_HbtRe0BghB38twiTxT0o8DCly6Mp4Py9ugvNuKuISyYmjErBzYSzXyrIya0mHe_k2L7WJR2_YYHWN6yczhmyp0E4ErSsomKEr_53O0dJbqy7DmBqgLhvVZvu1sxu275DOhMhsmdblwOI1ZEEHEahXKwneuP0NwB6YbzUaTUC9tBaxN0KYI0qiDXGDLj8glBoW8ZkihbQaw7Q2UAp-0OylsXp3Cg

Visitor:
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjB5SnU5T3lseXBZVVBjTWg4bVhaRSJ9.eyJpc3MiOiJodHRwczovL2ZlcmZpLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDhkYzE0YWQ0OTI5ZDAwNmE4ZDYxOTQiLCJhdWQiOiJwaG90b2dyYXBoeSIsImlhdCI6MTYyMDQ3MzE5MCwiZXhwIjoxNjIwNTU5NTkwLCJhenAiOiIxY3hMU01xbGxCdG83d0hrbFBOV1FtVWdIeUxyb3BDVyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmRhdGEiXX0.WBDMfVzIjKVqsIjDduFujUD-Yd-5QoxMP0PLVIirHOjP2_6MxaOIvhUHx5FMV1fLQNNS2jHxFCx7vPlg9S8LQnv4_ndLkXnasRnkGaLb2qRkLNTgwCFMUV8fggOaIkqC2W-a48v_5Ndqr8viR-8zDpXAGDVvYGwiqgkvIq4wOlUUN9QPvS7i69mpRd5IT0lZxteHjBzsHHnWX861rn06f5Z3DS4FDd2tbe3fn5wSSEoFPbW0d1DajEsXMVnmGcp2mGXMRvxenDjUOps80lb6OIvA1gipyF1CyLhztphU8NMLENcd4CjXrCuliizH2vuGVGj-GYi7e4HAx3P9Nzs1sQ

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