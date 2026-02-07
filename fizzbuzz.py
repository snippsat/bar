def fizzbuzz(n):
    """Return list of FizzBuzz values from 1..n."""
    if not isinstance(n, int):
        raise TypeError("n must be int")
    if n < 1:
        return []

    result = []
    for i in range(1, n + 1):
        value = ""
        if i % 3 == 0:
            value += "Fizz"
        if i % 5 == 0:
            value += "Buzz"
        if not value:
            value = str(i)
        result.append(value)
    return result


def print_fizzbuzz(n):
    """Print FizzBuzz values from 1..n, one per line."""
    for item in fizzbuzz(n):
        print(item)


if __name__ == "__main__":
    import sys

    try:
        count = int(sys.argv[1]) if len(sys.argv) > 1 else 100
    except ValueError:
        raise SystemExit("Usage: python fizzbuzz.py [positive_integer]")
    print_fizzbuzz(count)
