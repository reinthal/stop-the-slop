import os


def get_env_var(var_name, default=None):
    return os.getenv(var_name, default)
