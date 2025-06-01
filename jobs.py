from chancy import job
import time

@job()
async def fibonacci(n: int):
    """Calculate fibonacci number (for testing longer running jobs)"""
    print("Start: ", n)
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    

    print("Result is: ", b)
    return b

@job()
def hello_world(*, name: str):
    print("Start")
    # exit(1)
    time.sleep(20)
    print("End")
    print(f"another, {name}!")