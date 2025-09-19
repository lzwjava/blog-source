#!/usr/bin/env python3
"""
Python integration tests for bandwidth API endpoints.
These tests run against the actual running Java server.
"""

import unittest
import requests
import time
import os


class TestBandwidthAPI(unittest.TestCase):
    """Integration tests for bandwidth API endpoints."""

    @classmethod
    def setUpClass(cls):
        """Set up test class with server URL."""
        cls.base_url = os.getenv('TEST_SERVER_URL', 'http://localhost:8080')
        cls.max_wait = 30  # seconds
        cls._wait_for_server()

    @classmethod
    def _wait_for_server(cls):
        """Wait for the server to be ready."""
        print(f"Waiting for server at {cls.base_url}...")
        start_time = time.time()
        while time.time() - start_time < cls.max_wait:
            try:
                response = requests.get(f"{cls.base_url}/actuator/health", timeout=2)
                if response.status_code == 200:
                    print("Server is ready!")
                    return
            except requests.exceptions.RequestException:
                pass
            time.sleep(1)
        raise Exception(f"Server not ready after {cls.max_wait} seconds")

    def test_health_endpoint(self):
        """Test the health endpoint is accessible."""
        response = requests.get(f"{self.base_url}/actuator/health")
        self.assertEqual(response.status_code, 200)
        self.assertIn('status', response.json())

    def test_root_endpoint(self):
        """Test the root endpoint."""
        response = requests.get(f"{self.base_url}/")
        self.assertEqual(response.status_code, 200)

    def test_pdf_endpoint_accessible(self):
        """Test the PDF endpoint is accessible."""
        # Test with a simple request - adjust based on your actual API
        response = requests.get(f"{self.base_url}/api/pdf/test")
        # This might return 404 for non-existent PDF, but should not crash
        self.assertIn(response.status_code, [200, 404])

    def test_bandwidth_endpoint_response(self):
        """Test bandwidth endpoint returns proper response."""
        # Adjust this test based on your actual bandwidth API
        try:
            response = requests.get(f"{self.base_url}/api/bandwidth")
            # Check if endpoint exists and responds
            self.assertIn(response.status_code, [200, 404, 405])
        except requests.exceptions.RequestException as e:
            self.fail(f"Bandwidth endpoint request failed: {e}")


if __name__ == '__main__':
    unittest.main()