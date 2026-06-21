from main import format_username, is_valid_email, get_user_role


def test_format_username():
    assert format_username("Joe", "Doe") == "joe.doe"


def test_valid_email():
    assert is_valid_email("[ivan@example.com](mailto:ivan@example.com)") is True


def test_invalid_email():
    assert is_valid_email("invalid-email") is False


def test_admin_role():
    assert get_user_role(True) == "Admin"


def test_user_role():
    assert get_user_role(False) == "User"
