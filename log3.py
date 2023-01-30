import datetime


def logger(old_function):
    def new_function(*args, **kwargs):
        with open('homework.log', 'a') as f:
            result = old_function(*args, **kwargs)
            f.write(
                f'{datetime.datetime.now()} - Function "{old_function.__name__}" was called with arguments {args}'
                f'and keyword arguments {kwargs}. Returned value: {result}\n'
            )
        return result
    return new_function
