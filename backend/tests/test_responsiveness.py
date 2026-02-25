# Epic Title: Test Portal Usability on Various Screen Sizes

import requests

class TestPortalUsability:
    
    BASE_URL = "http://localhost:8000"

    def test_usability_on_desktop(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        response = requests.get(self.BASE_URL, headers=headers)
        assert response.status_code == 200
        # Add assertions to check that all major elements are present
        # and accessible, according to your application's requirements.

    def test_usability_on_tablet(self):
        headers = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X)'}
        response = requests.get(self.BASE_URL, headers=headers)
        assert response.status_code == 200
        # Add assertions to check that all major elements are present
        # and accessible, according to your application's requirements.

    def test_usability_on_mobile(self):
        headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2 like Mac OS X)'}
        response = requests.get(self.BASE_URL, headers=headers)
        assert response.status_code == 200
        # Add assertions to check that all major elements are present
        # and accessible, according to your application's requirements.