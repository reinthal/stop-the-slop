from unittest.mock import Mock, patch

import pytest

from src.utils.integrations import get_env_var
from src.utils.io_functions import get_ip
from src.utils.my_math import some_function


class TestSomeFunction:
    """Test cases for the some_function in my_math module."""

    def test_some_function_positive_integer(self):
        """Test some_function with positive integers."""
        assert some_function(5) == 6
        assert some_function(10) == 11
        assert some_function(100) == 101

    def test_some_function_negative_integer(self):
        """Test some_function with negative integers."""
        assert some_function(-5) == -4
        assert some_function(-10) == -9
        assert some_function(-1) == 0

    def test_some_function_zero(self):
        """Test some_function with zero."""
        assert some_function(0) == 1

    def test_some_function_large_numbers(self):
        """Test some_function with large numbers."""
        assert some_function(999999) == 1000000
        assert some_function(-999999) == -999998

    def test_some_function_return_type(self):
        """Test that some_function returns an integer."""
        result = some_function(5)
        assert isinstance(result, int)

    @pytest.mark.parametrize(
        "input_val,expected",
        [
            (1, 2),
            (2, 3),
            (3, 4),
            (-1, 0),
            (-2, -1),
            (0, 1),
            (42, 43),
        ],
    )
    def test_some_function_parametrized(self, input_val, expected):
        """Parametrized test for some_function with various inputs."""
        assert some_function(input_val) == expected

    def test_some_function_type_error(self):
        """Test that some_function raises TypeError for non-numeric inputs."""
        with pytest.raises(TypeError):
            some_function("string")

        with pytest.raises(TypeError):
            some_function(None)

        with pytest.raises(TypeError):
            some_function([1, 2, 3])


class TestGetIp:
    """Test cases for the get_ip function in io_functions module."""

    @patch("src.utils.io_functions.rq.get")
    def test_get_ip_success(self, mock_get):
        """Test get_ip returns IP address on successful request.
        These tests doesnt do anything really but shows how to patch functions."""
        # Mock the response
        mock_response = Mock()
        mock_response.text = "192.168.1.1"
        mock_get.return_value = mock_response

        result = get_ip()

        assert result == "192.168.1.1"
        mock_get.assert_called_once_with("https://api.ipify.org")

    @patch("src.utils.io_functions.rq.get")
    def test_get_ip_different_ips(self, mock_get):
        """Test get_ip with different IP addresses."""
        test_ips = ["203.0.113.1", "198.51.100.42", "10.0.0.1"]

        for test_ip in test_ips:
            mock_response = Mock()
            mock_response.text = test_ip
            mock_get.return_value = mock_response

            result = get_ip()
            assert result == test_ip

    @patch("src.utils.io_functions.rq.get")
    def test_get_ip_return_type(self, mock_get):
        """Test that get_ip returns a string."""
        mock_response = Mock()
        mock_response.text = "127.0.0.1"
        mock_get.return_value = mock_response

        result = get_ip()
        assert isinstance(result, str)

    @patch("src.utils.io_functions.rq.get")
    def test_get_ip_empty_response(self, mock_get):
        """Test get_ip with empty response."""
        mock_response = Mock()
        mock_response.text = ""
        mock_get.return_value = mock_response

        result = get_ip()
        assert result == ""

    @patch("src.utils.io_functions.rq.get")
    def test_get_ip_request_exception(self, mock_get):
        """Test get_ip when requests raises an exception."""
        mock_get.side_effect = Exception("Network error")

        with pytest.raises(Exception) as exc_info:
            get_ip()

        assert str(exc_info.value) == "Network error"
        mock_get.assert_called_once_with("https://api.ipify.org")

    @patch("src.utils.io_functions.rq.get")
    def test_get_ip_request_timeout(self, mock_get):
        """Test get_ip when requests times out."""
        import requests

        mock_get.side_effect = requests.exceptions.Timeout("Request timed out")

        with pytest.raises(requests.exceptions.Timeout):
            get_ip()

    @patch("src.utils.io_functions.rq.get")
    def test_get_ip_connection_error(self, mock_get):
        """Test get_ip when connection fails."""
        import requests

        mock_get.side_effect = requests.exceptions.ConnectionError("Connection failed")

        with pytest.raises(requests.exceptions.ConnectionError):
            get_ip()


class TestGetEnvVar:
    """Test cases for the get_env_var function in integrations module."""

    @patch("src.utils.integrations.os.getenv")
    def test_get_env_var_secret_password_exists(self, mock_getenv):
        """Test get_env_var returns SECRET_PASSWORD when it exists."""
        mock_getenv.return_value = "my_secret_password_123"

        result = get_env_var("SECRET_PASSWORD")

        assert result == "my_secret_password_123"
        mock_getenv.assert_called_once_with("SECRET_PASSWORD", None)

    @patch("src.utils.integrations.os.getenv")
    def test_get_env_var_secret_password_with_default(self, mock_getenv):
        """Test get_env_var returns default when SECRET_PASSWORD doesn't exist."""
        mock_getenv.return_value = "default_password"

        result = get_env_var("SECRET_PASSWORD", "default_password")

        assert result == "default_password"
        mock_getenv.assert_called_once_with("SECRET_PASSWORD", "default_password")

    @patch("src.utils.integrations.os.getenv")
    def test_get_env_var_some_other_config_exists(self, mock_getenv):
        """Test get_env_var returns SOME_OTHER_CONFIG when it exists."""
        mock_getenv.return_value = "production"

        result = get_env_var("SOME_OTHER_CONFIG")

        assert result == "production"
        mock_getenv.assert_called_once_with("SOME_OTHER_CONFIG", None)

    @patch("src.utils.integrations.os.getenv")
    def test_get_env_var_some_other_config_with_default(self, mock_getenv):
        """Test get_env_var returns default when SOME_OTHER_CONFIG doesn't exist."""
        mock_getenv.return_value = "development"

        result = get_env_var("SOME_OTHER_CONFIG", "development")

        assert result == "development"
        mock_getenv.assert_called_once_with("SOME_OTHER_CONFIG", "development")

    @patch("src.utils.integrations.os.getenv")
    def test_get_env_var_none_when_not_exists(self, mock_getenv):
        """Test get_env_var returns None when variable doesn't exist and no default."""
        mock_getenv.return_value = None

        result = get_env_var("SECRET_PASSWORD")

        assert result is None
        mock_getenv.assert_called_once_with("SECRET_PASSWORD", None)

    @pytest.mark.parametrize(
        "var_name,env_value,default,expected",
        [
            ("SECRET_PASSWORD", "secret123", None, "secret123"),
            ("SECRET_PASSWORD", None, "default_secret", "default_secret"),
            ("SOME_OTHER_CONFIG", "config_value", None, "config_value"),
            ("SOME_OTHER_CONFIG", None, "default_config", "default_config"),
            ("SECRET_PASSWORD", "", "fallback", ""),  # Empty string is valid
            ("SOME_OTHER_CONFIG", "0", None, "0"),  # String "0" is valid
        ],
    )
    @patch("src.utils.integrations.os.getenv")
    def test_get_env_var_parametrized(
        self, mock_getenv, var_name, env_value, default, expected
    ):
        """Parametrized test for get_env_var with various scenarios."""
        mock_getenv.return_value = env_value if env_value is not None else default

        result = get_env_var(var_name, default)

        assert result == expected
        mock_getenv.assert_called_once_with(var_name, default)
