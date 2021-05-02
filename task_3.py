from functools import wraps

def profile_decorator(callback):
   @wraps(callback)
   def wrapper(*args):
       res_type = {}
       result = callback(*args)
       for i in result:
          res_type[i] = type(i)

       print(res_type)
       return result
   return wrapper


@profile_decorator
def cal_cub(x, y):
    return x ** 3, y ** 3


print(cal_cub(4, 5))