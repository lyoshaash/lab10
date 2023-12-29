import typer
import time
import math
import gens
import closures
import recursions

app = typer.Typer()

@app.command()
def task1_recursive():
    nested_list = [1, [2, [3, 4, [5]]]]
    result_recursive = sum_nested_recursive(nested_list)
    print(result_recursive)

@app.command()
def task1_iterative():
    nested_list = [1, [2, [3, 4, [5]]]]
    result_iterative = sum_nested_iterative(nested_list)
    print(result_iterative)

@app.command()
def task2_closures(api_url: str):
    get_dog_fact = create_api_request_closure(api_url)
    dog_fact = get_dog_fact()
    print("Dog Fact:", dog_fact)

@app.command()
def task2_throttle():
    for _ in range(5):
        print(limited_function())
        time.sleep(2)

@app.command()
def task3(file_path: str, max_line_length: int):
    for truncated_line in read_file_line_by_line(file_path, max_line_length):
        print(truncated_line, end='')


if __name__ == "__main__":
    app()
