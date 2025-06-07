"""
3. Retry Decorator

Write a @retry decorator that retries a function if it raises an exception, up to N times with delay.

@retry(max_attempts=3, delay=2)
def flaky_api_call():
    ...
"""
import requests
import time

def retry(max_attempts, delay):
    def retry_func(func):
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts+1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt} failed. Error is {e}")
                    if attempt < max_attempts:
                        time.sleep(delay)
                    else:
                        raise
        return wrapper
    return retry_func

@retry(max_attempts=3, delay=2)
def flaky_api_call():
    print("call API")
    response = requests.get("https://httpstat.us/403")
    response.raise_for_status()
    return response.status_code

flaky_api_call()
