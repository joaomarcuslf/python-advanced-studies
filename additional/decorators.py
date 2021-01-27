import functools

user = {"access_level": "user"}


def make_secure(access_level):
    def decorator(func):
        @functools.wraps(func)
        def secure_function(*args, **kwargs):
            if user["access_level"] == access_level:
                return func(*args, **kwargs)
            else:
                return f"No {access_level} permissions for this role."

        return secure_function

    return decorator


@make_secure("user")
def get_dashboard_password():
    return "user: user_password"


@make_secure("admin")
def get_admin_password():
    return "admin: 1234"
