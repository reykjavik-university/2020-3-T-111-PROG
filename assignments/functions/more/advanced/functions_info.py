def get_function_info(function: callable) -> str:
    divider = "-" * 40
    return f"Name: {function.__name__}\n{divider}\n{function.__doc__}"
