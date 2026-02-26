# File: tests/test_account_opening.py

import unittest
from unittest.mock import patch, MagicMock
from flask import Flask
from backend.account_management.routes import account_bp

class TestOpenAccount(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(account_bp)
        self.client = self.app.test_client()

    @patch('backend.account_management.routes.AccountService.process_opening_request')
    @patch('backend.database.config.get_db')
    def test_open_account_successful(self, mock_get_db, mock_process_opening_request):
        mock_get_db.return_value.__next__.return_value = MagicMock()
        mock_process_opening_request.return_value = {'success': True}

        response = self.client.post('/account/open', json={'sample_key': 'sample_value'})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': 'Account opening request successfully submitted'})

    @patch('backend.account_management.routes.AccountService.process_opening_request')
    @patch('backend.database.config.get_db')
    def test_open_account_failure(self, mock_get_db, mock_process_opening_request):
        mock_get_db.return_value.__next__.return_value = MagicMock()
        mock_process_opening_request.return_value = {'success': False, 'message': 'Failed to open account'}

        response = self.client.post('/account/open', json={'sample_key': 'sample_value'})

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Failed to open account'})

    @patch('backend.account_management.routes.AccountService.process_opening_request')
    @patch('backend.database.config.get_db')
    def test_open_account_processing_error(self, mock_get_db, mock_process_opening_request):
        mock_get_db.return_value.__next__.return_value = MagicMock()
        mock_process_opening_request.side_effect = SQLAlchemyError()

        response = self.client.post('/account/open', json={'sample_key': 'sample_value'})

        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {'error': 'Backend processing error'})

    @patch('backend.account_management.routes.AccountService.process_opening_request')
    @patch('backend.database.config.get_db')
    def test_open_account_invalid_input(self, mock_get_db, mock_process_opening_request):
        mock_get_db.return_value.__next__.return_value = MagicMock()
        mock_process_opening_request.return_value = {'success': False, 'message': 'Invalid data'}
        
        response = self.client.post('/account/open', json=None)
        
        # Ensure the request was parsed as None
        self.assertIsNone(request.get_json())
        
        # Ensure it handles the case correctly
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

if __name__ == '__main__':
    unittest.main()
