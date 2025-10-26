def greet(name: str) -> str:
    if not name:
        return "Hello, World!"
    return f"Hello, {name}!"

def main() -> None:
    print(greet("World"))

if __name__ == "__main__":
    main()
