#!/usr/bin/env python3
""" Unittests for the client module. """
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test case for GithubOrgClient.org"""

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value"""
        expected_payload = {"login": org_name}
        mock_get_json.return_value = expected_payload

        client = GithubOrgClient(org_name)
        result = client.org

        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")
        self.assertEqual(result, expected_payload)
        
    def test_public_repos_url(self):
        """Test that GithubOrgClient._public_repos_url returns the correct URL"""
        org_name = "google"
        client = GithubOrgClient(org_name)
        expected_url = f"https://api.github.com/orgs/{org_name}/repos"
        
        self.assertEqual(client._public_repos_url, expected_url)
    
    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test that GithubOrgClient.public_repos returns the correct repos"""
        mock_get_json.return_value = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"}
        ]
        test_url = "https://fake.url/orgs/test/repos"

        with patch('client.GithubOrgClient._public_repos_url', new_callable=PropertyMock) as mock_repos_url:
            mock_repos_url.return_value = test_url

            client = GithubOrgClient("test")
            result = client.public_repos()

            self.assertEqual(result, ["repo1", "repo2", "repo3"])
            mock_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with(test_url)
    
    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test that has_license returns correct boolean for license match"""
        client = GithubOrgClient("test")
        result = client.has_license(repo, license_key)
        self.assertEqual(result, expected)
