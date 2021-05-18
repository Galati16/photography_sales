import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import app, create_app
from models_test import db, setup_db, Image, Sale, db_drop_and_create_all
import os


class PhotographySalesTestCase(unittest.TestCase):
    """This class represents the photography sales test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = app
        self.client = self.app.test_client
        self.database_name = "photography_sales_test"
        # use for local testing:
        setup_db(
           self.app,
           "postgresql://postgres:hallo@localhost:5432/photography_sales_test")
        # create dummy image and sale:
        self.new_image = {
            'create': 'image',
            'active_since': '2020-05-07 10:52:40',
            'description': 'Blue moon'
        }
        self.patch_image = {
            'patch': 'image',
            'active_since': '2020-05-07 10:52:40',
            'description': 'Beautiful blue moon'
        }
        self.new_sale = {
            'create': 'sale',
            'image_id': 1,
            'sales_date': '2021-05-08 09:52:30',
            'income': 0.9,
            'platform': 'Shutterstock'
        }
        self.patch_sale = {
            'patch': 'sale',
            'image_id': 1,
            'sales_date': '2021-05-08 09:52:30',
            'income': 0.7,
            'platform': 'Shutterstock'
        }  # changed income

        # authentification token (data:get permission)
        self.token = os.environ['ADMIN_TOKEN']
        self.headers = {'Authorization': 'Bearer ' + self.token,
                        'Content-Type': 'application/json'}

    def tearDown(self):
        """Executed after each test"""
        db_drop_and_create_all()

    def test_GET_sales_success(self):
        ''' Test Get sales '''
        res = self.client().get('/sales',
                                headers=self.headers
                                )
        data = json.loads(res.data)
        nr_image_sales = Sale.query.all()
        self.assertEqual(len(data['image_sales']), len(nr_image_sales))
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_GET_images_success(self):
        ''' Test Get images '''
        res = self.client().get('/images',
                                headers=self.headers
                                )
        data = json.loads(res.data)
        nr_images = Image.query.all()
        self.assertEqual(len(data['all_images']), len(nr_images))
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_GET_images_fail(self):
        '''Try to use wrong method'''
        res = self.client().post('/sales',
                                 headers=self.headers
                                 )
        data = json.loads(res.data)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['error'], 405)
        self.assertEqual(data['message'], 'method not allowed')

    # Test endpoint:post
    # images:

    def test_add_image(self):
        '''Add a new image to the database'''
        nr_images_previous = len(Image.query.all())
        res = self.client().post('/data',
                                 json=self.new_image,
                                 headers=self.headers)
        nr_images_new = len(Image.query.all())
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(nr_images_previous + 1, nr_images_new)

    # sales:
    def test_add_sales(self):
        '''Add a new sale to the database'''
        nr_sales_previous = len(Sale.query.all())
        res = self.client().post('/data',
                                 json=self.new_sale,
                                 headers=self.headers)
        nr_sales_new = len(Sale.query.all())
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(nr_sales_previous + 1, nr_sales_new)
    # fail:

    def test_add_image_fail(self):
        '''Error: try to add a new element without sending json data'''
        # no data added to request
        res = self.client().post('/data', headers=self.headers)
        self.assertEqual(res.status_code, 400)

    # Test endpoint:patch
    # images:
    def test_patch_image(self):
        '''patch an image '''
        nr_images_previous = len(Image.query.all())
        image = Image.query.filter(Image.id == 1).one_or_none()
        res = self.client().patch('/data/1',
                                  json=self.patch_image,
                                  headers=self.headers)
        nr_images_new = len(Image.query.all())
        image_patched = Image.query.filter(Image.id == 1).one_or_none()
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        # check, that number of images remains unchanged
        self.assertEqual(nr_images_previous, nr_images_new)
        # check, that description has been changed:
        self.assertNotEqual(image_patched.description, image.description)

    # sales:
    def test_patch_sales(self):
        '''patch sale'''
        sale = Sale.query.filter(Sale.id == 1).one_or_none()
        nr_sales_previous = len(Sale.query.all())
        res = self.client().patch('/data/1',
                                  json=self.patch_sale,
                                  headers=self.headers)
        nr_sales_new = len(Sale.query.all())
        sale_patched = Sale.query.filter(Sale.id == 1).one_or_none()
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        # check, that number of sales remains unchanged
        self.assertEqual(nr_sales_previous, nr_sales_new)
        # check, that income has been changed:
        self.assertNotEqual(sale_patched.income, sale.income)

    # fail:
    def test_patch_sales_fail(self):
        '''error test: try to patch a nonexisten sale id'''
        nr_sales_previous = len(Sale.query.all())
        res = self.client().patch('/data/100',
                                  json=self.patch_sale,
                                  headers=self.headers)
        nr_sales_new = len(Sale.query.all())
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    # Test endpoint:delete

    def test_delete_image(self):
        '''Remove image 1 from Database'''
        res = self.client().delete('/delete/image/1', headers=self.headers)
        data = json.loads(res.data)
        image = Image.query.filter(Image.id == 1).one_or_none()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['id'], '1')
        self.assertEqual(data['type'], 'image')
        self.assertEqual(image, None)

    def test_delete_sale(self):
        '''Remove sale 1 from Database'''
        res = self.client().delete('/delete/sale/1', headers=self.headers)
        data = json.loads(res.data)
        sale = Sale.query.filter(Sale.id == 1).one_or_none()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['id'], '1')
        self.assertEqual(data['type'], 'sale')
        self.assertEqual(sale, None)

    def test_delete_fail(self):
        '''Error test: try to delete nonexisten id from Database'''
        res = self.client().delete('/delete/image/200', headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
