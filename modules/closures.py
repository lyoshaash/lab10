import requests
import time

def create_api_request_closure(api_url):
    def api_request():
        response = requests.get(api_url)
        if response.status_code == 200:
            return response.json()
        else:
            return f"Error: {response.status_code}"

    return api_request

api_url = "https://dogapi.dog/api/v2/facts"
get_dog_fact = create_api_request_closure(api_url)
dog_fact = get_dog_fact()
print("Dog Fact:", dog_fact)

def throttle(limit_per_second):
    def decorator(func):
        last_invocation = 0

        def wrapper(*args, **kwargs):
            nonlocal last_invocation
            current_time = time.time()

            if current_time - last_invocation >= 1 / limit_per_second:
                result = func(*args, **kwargs)
                last_invocation = current_time
                return result
            else:
                return f"Пожалуйста подождите перед тем как делать новый запрос"

        return wrapper

    return decorator

@throttle(limit_per_second=7)
def limited_function():
    return "частота вызовов этой функции ограничена"

for _ in range(5):
    print(limited_function())
    time.sleep(2)
