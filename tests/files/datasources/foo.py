from src.docker_jinja3 import global_function


@global_function
def bar(name):
    return f" - {name} - "
