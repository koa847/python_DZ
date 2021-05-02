from functools import wraps

def logger(verbosity):
   def _logger(func):
       def wrapper(*args):
           result = func(*args)
           if verbosity(*args):
               return result
           else: print(f'ValueError: wrong val {args}')
       return wrapper
   return _logger


@logger(lambda x: x > 0)
def render_input(x):
   return x ** 3

print(render_input(-5))