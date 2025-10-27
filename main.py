# main.py
import json
import inspect
import time
import importlib


def run_local(method_name: str = None):
    # Dynamically import your code.py
    code_module = importlib.import_module("code")
    if not hasattr(code_module, "Solution"):
        raise ValueError("Your code.py must contain a class named 'Solution'.")

    Solution = getattr(code_module, "Solution")
    sol = Solution()

    with open("input.txt", "r") as infile:
        lines = [line.strip() for line in infile.readlines() if line.strip()]

    t = int(lines[0])
    results = []

    # Auto-detect the method
    methods = [
        name for name, obj in inspect.getmembers(Solution, predicate=inspect.isfunction)
        if not name.startswith("__")
    ]

    if method_name is None:
        if len(methods) == 0:
            raise ValueError("No method found inside Solution class.")
        elif len(methods) > 1:
            print(f"Multiple methods found: {methods}. Using '{methods[0]}' by default.")
        method_name = methods[0]

    method = getattr(sol, method_name)
    sig = inspect.signature(method)
    num_params = len(sig.parameters)

    print(f"Running {method_name} for {t} test case(s)...")

    for i in range(1, t + 1):
        line = lines[i]

        try:
            data = json.loads(line)
        except json.JSONDecodeError:
            data = line

        if num_params == 1:
            args = (data,)
        elif isinstance(data, list) and len(data) == num_params:
            args = tuple(data)
        else:
            args = (data,)

        start = time.time()
        result = method(*args)
        end = time.time()
        elapsed = (end - start) * 1000  # ms

        print(f"Test {i}: {elapsed:.2f} ms")
        results.append(f"{result}  ({elapsed:.2f} ms)")

    with open("output.txt", "w") as outfile:
        outfile.write("\n".join(map(str, results)))


if __name__ == "__main__":
    run_local()
