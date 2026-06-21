def format_username(first_name: str, last_name: str) -> str:
    return f"{first_name.lower()}.{last_name.lower()}"


def is_valid_email(email: str) -> bool:
    return "@" in email and "." in email


def get_user_role(is_admin: bool) -> str:
    if is_admin:
        return "Admin"
    return "User"
