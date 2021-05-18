import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime
from models import db, Image, Sale, db_drop_and_create_all, setup_db
from auth import AuthError, requires_auth


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    CORS(app)

    return app


app = create_app()
setup_db(app)

# set Access-Control-Allow cors headers:


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add(
        'Access-Control-Allow-Methods',
        'GET,POST,PATCH,DELETE')
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

#
# Variables and functions dealing with time and time formatting:
#


current_time = datetime.now().strftime('%Y-%m-%d %H:%S:%M')

# create new database with one entry for Image and Sale Module each
# db_drop_and_create_all()
'''
GET /sales
show data in  sales table
requires the 'get:data' permission
returns status code 200 and json {"success": True, "image_sales": all_sales}
'''


@app.route('/sales', methods=['GET'])
@requires_auth('get:data')
def get_list_sales(payload):
    try:
        sales = Sale.query
        all_sales = [sale.format() for sale in sales]
        return jsonify({
            'success': True,
            'image_sales': all_sales
        })

    except Exception:
        abort(405)


'''GET  /images:
show data in image table
requires the 'get:data' permission
returns status code 200 and json {"success": True, " all_images":  all_images}
'''


@app.route('/images', methods=['GET'])
@requires_auth('get:data')
def get_list_images(payload):
    try:
        images = Image.query
        all_images = [image.format() for image in images]
        return jsonify({
            'success': True,
            'all_images': all_images
        })

    except Exception:
        abort(405)


'''
POST /data
create a new row in the Sale or Image table
requires the 'post:data' permission
returns status code 200 and json
{"success": True, "data": data} where data is an array
containing only the newly created data
'''


@app.route('/data', methods=['POST'])
@requires_auth('post:data')
def post_data(payload):
    body = request.get_json()
    if body.get('create') is None:
        abort(404)
    elif body.get('create') == 'image':
        # create a new row in Image Table
        description = body.get('description')
        active_since = body.get('active_since')
        image = Image(
            description=description,
            active_since=active_since
        )
        in_database = Image.query.filter(
            Image.description == description).one_or_none()
        if in_database is None:
            image.insert()
            data = image
        else:
            data = in_database
    elif body.get('create') == 'sale':
        # create a new row in Sale Table
        sale = Sale(
            image_id=body.get('image_id'),
            sales_date=body.get('sales_date'),
            income=body.get('income'),
            platform=body.get('platform'),
        )
        in_database = Sale.query.filter(
            Sale.sales_date == body.get('sales_date')).one_or_none()
        if in_database is None:
            sale.insert()
            data = sale
        else:
            data = in_database
    return jsonify({
        'success': True,
        'data': data.format()
    })


'''
DELETE /delete/<type>/<id>
<type>: image or sale
<id>: id to be deleted
removes image or sale from table
requires the 'delete:data' permission
returns status code 200 and json {"success": True, 'type': type, 'id': id }
'''


@app.route('/delete/<type>/<id>', methods=['DELETE'])
@requires_auth('delete:data')
def delete_data(payload, id, type):
    if type is None:
        abort(404)
    elif type == 'image':
        image = Image.query.filter(Image.id == id).one_or_none()
        if image is None:
            abort(404)
        image.delete()
    elif type == 'sale':
        sale = Sale.query.filter(Sale.id == id).one_or_none()
        if sale is None:
            abort(404)
        sale.delete()
    else:
        abort(500)

    return jsonify({
        'success': True,
        'type': type,
        'id': id
    }), 200


'''
PATCH /data/<id>
<id>: id to be changed
changes image data or sales in table
requires the 'patch:data' permission
returns status code 200 and json {"success": True, 'data': data }
'''


@app.route('/data/<id>', methods=['PATCH'])
@requires_auth('patch:data')
def patch_data(payload, id):

    # try:
    body = request.get_json()
    if body.get('patch') is None:
        abort(404)
    elif body.get('patch') == 'image':
        image = Image.query.filter(Image.id == id).one_or_none()
        if image is None:
            abort(404)
        if 'active_since' in body:
            image.active_since = body.get('active_since')
        if 'description' in body:
            image.description = body.get('description')
        image.update()
        data = image
    elif body.get('patch') == 'sale':
        sale = Sale.query.filter(Sale.id == id).one_or_none()
        if sale is None:
            abort(404)
        if 'image_id' in body:
            sale.image_id = body.get('image_id')
        if 'income' in body:
            sale.income = body.get('income')
        if 'platform' in body:
            sale.platform = body.get('platform')
        if 'sales_date' in body:
            sale.sales_date = body.get('sales_date')
        sale.update()
        data = sale
    else:
        abort(500)
    return jsonify({
        'success': True,
        'data': [data.format()]
    })
    # except:
    # abort(405)


@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello, World!'

# Error Handling


@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422


@app.errorhandler(400)
def bad_request(error):
    return jsonify({
        "success": False,
        "error": 400,
        "message": "bad request"
    }), 400


@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'success': False,
        'error': 404,
        'message': 'resource not found'
    }), 404


@app.errorhandler(405)
def bad_request(error):
    return jsonify({
        'success': False,
        'error': 405,
        'message': 'method not allowed'
    }), 405


@app.errorhandler(401)
def unauthorized(error):
    return jsonify({
        'success': False,
        'error': 401,
        'message': 'unauthorized'
    }), 401


@app.errorhandler(403)
def forbidden(error):
    return jsonify({
        'success': False,
        'error': 403,
        'message': 'forbidden'
    }), 403


@app.errorhandler(500)
def unprocessable(error):
    return jsonify({
        'success': False,
        'error': 500,
        'message': 'internal sever error'
    }), 500


'''
error handler for AuthErrorerror handler
'''


@app.errorhandler(AuthError)
# 401 status code
def auth_error(message):
    return jsonify({
        "success": False,
        "error": message.status_code,
        "code": message.error['code'],
        "message": message.error['description']
    }), message.status_code


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
