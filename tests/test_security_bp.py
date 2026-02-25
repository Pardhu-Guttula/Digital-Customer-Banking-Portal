# File: tests/test_security_bp.py

import unittest
from unittest.mock import MagicMock, patch
from flask import Flask
from flask.testing import FlaskClient
from backend.access_control.services.security_service import SecurityService
from backend.database.config import get_db
from security import security_bp

class SecurityBPTest(unittest.TestCase):
    def setUp(self):
        app = Flask(__name__)
        app.register_blueprint(security_bp)
        self.client: FlaskClient = app.test_client()

    @patch('security.SecurityService')
    @patch('security.get_db')
    def test_secure_api_call_valid_token_and_data(self, mock_get_db, mock_security_service):
        mock_db = MagicMock()
        mock_get_db.return_value = iter([mock_db])
        mock_security_service_instance = mock_security_service.return_value
        response = self.client.post('/secure-api', headers={'Authorization': 'valid-token'}, json={'key': 'value'})
        mock_security_service_instance.validate_token.assert_called_once_with('valid-token')
        mock_security_service_instance.encrypt_sensitive_data.assert_called_once_with({'key': 'value'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': 'Interaction authorized and data encrypted'})

    @patch('security.SecurityService')
    @patch('security.get_db')
    def test_secure_api_call_invalid_token(self, mock_get_db, mock_security_service):
        mock_db = MagicMock()
        mock_get_db.return_value = iter([mock_db])
        mock_security_service_instance = mock_security_service.return_value
        mock_security_service_instance.validate_token.side_effect = Exception('Invalid token')
        response = self.client.post('/secure-api', headers={'Authorization': 'invalid-token'}, json={'key': 'value'})
        mock_security_service_instance.validate_token.assert_called_once_with('invalid-token')
        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.json, {'error': 'Invalid token'})

    @patch('security.SecurityService')
    @patch('security.get_db')
    def test_secure_api_call_missing_token(self, mock_get_db, mock_security_service):
        mock_db = MagicMock()
        mock_get_db.return_value = iter([mock_db])
        response = self.client.post('/secure-api', json={'key': 'value'})
        self.assertEqual(response.status_code, 403)
        self.assertIn('error', response.json)

    @patch('security.SecurityService')
    @patch('security.get_db')
    def test_secure_api_call_encryption_failure(self, mock_get_db, mock_security_service):
        mock_db = MagicMock()
        mock_get_db.return_value = iter([mock_db])
        mock_security_service_instance = mock_security_service.return_value
        mock_security_service_instance.encrypt_sensitive_data.side_effect = Exception('Encryption failed')
        response = self.client.post('/secure-api', headers={'Authorization': 'valid-token'}, json={'key': 'value'})
        mock_security_service_instance.validate_token.assert_called_once_with('valid-token')
        mock_security_service_instance.encrypt_sensitive_data.assert_called_once_with({'key': 'value'})
        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.json, {'error': 'Encryption failed'})

    @patch('security.SecurityService')
    @patch('security.get_db')
    def test_secure_api_call_no_payload(self, mock_get_db, mock_security_service):
        mock_db = MagicMock()
        mock_get_db.return_value = iter([mock_db])
        mock_security_service_instance = mock_security_service.return_value
        response = self.client.post('/secure-api', headers={'Authorization': 'valid-token'})
        mock_security_service_instance.validate_token.assert_called_once_with('valid-token')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': 'Interaction authorized and data encrypted'})

def suite():
    suite = unittest.TestLoader().loadTestsFromTestCase(SecurityBPTest)
    return suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())
