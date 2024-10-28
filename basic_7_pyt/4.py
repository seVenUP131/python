import time

def is_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        
        print("Время выполнения", end_time - start_time, "секунд")

        return result 
    return wrapper


@is_decorator
def example_function(n):
    total = 0
    for i in range (n):
        total += i
    return total 

example_function(1000000)        