import functools
user = {"username": "Jose", "access_level":"guest"}

def make_secure(access_level):
    def decorator(func):  #func->get_admin_pwd
        @functools.wraps(func)
        def secure_function(*args, **kwargs):
            if user["access_level"]==access_level:
                return func(*args, **kwargs)
            else:
                return f"No {access_level} permissions for {user['username']}."
    
        return secure_function   

    return decorator


@make_secure("admin")
def get_admin_pwd():
    return "admin: 1234"

@make_secure("user")
def get_dashboard_pwd():
    return "user : user_password"
 
print(get_admin_pwd())
print(get_dashboard_pwd())

user = {"username": "Jose", "access_level":"admin"}


print(get_admin_pwd())
print(get_dashboard_pwd())