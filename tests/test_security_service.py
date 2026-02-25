# File: tests/test_security_service.py

import unittest
from unittest.mock import MagicMock, patch
from cryptography.fernet import Fernet, InvalidToken
from security_service import SecurityService

class TestSecurityService(unittest.TestCase):
    def setUp(self):
        self.db_mock = MagicMock()
        self.security_repository_mock = MagicMock()
        self.cipher_suite_mock = MagicMock()
        self.service = SecurityService(self.db_mock)
        self.service.security_repository = self.security_repository_mock
        self.service.cipher_suite = self.cipher_suite_mock

    @patch('security_service.os')
    def test_init(self, mock_os):
        mock_os.environ.get.return_value = 'testkey123'
        security_service = SecurityService(self.db_mock)
        self.assertEqual(security_service.security_repository, self.security_repository_mock)
        self.assertIsInstance(security_service.cipher_suite, Fernet)
        self.assertEqual(security_service.cipher_suite.key, b'testkey123')

    def test_validate_token_success(self):
        token = 'valid_token'
        self.security_repository_mock.verify_token.return_value = True
        self.service.validate_token(token)
        self.security_repository_mock.verify_token.assert_called_once_with(token)

    def test_validate_token_missing_token(self):
        with self.assertRaises(ValueError) as context:
            self.service.validate_token('')
        self.assertEqual(str(context.exception), 'Missing token')

    def test_validate_token_invalid_token(self):
        token = 'invalid_token'
        self.security_repository_mock.verify_token.return_value = False
        with self.assertRaises(ValueError) as context:
            self.service.validate_token(token)
        self.assertEqual(str(context.exception), 'Invalid or expired token')

    def test_encrypt_sensitive_data_with_banking_data(self):
        data = {'banking_data': 'sensitive_info'}
        encrypted_data = 'encrypted_info'
        self.cipher_suite_mock.encrypt.return_value = encrypted_data.encode()
        result = self.service.encrypt_sensitive_data(data)
        self.assertEqual(result, {'banking_data': encrypted_data})
        self.cipher_suite_mock.encrypt.assert_called_once_with(b'sensitive_info')

    def test_encrypt_sensitive_data_without_banking_data(self):
        data = {'other_data': 'value'}
        result = self.service.encrypt_sensitive_data(data)
        self.assertEqual(result, data)

if __name__ == '__main__':
    unittest.main()
