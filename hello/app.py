def greet(name: str) -> str:
    if not name or not name.strip():
        return "Hello, World!"
    clean = name.strip()
    return f"Hello, {clean}!"


def main() -> None:
    print(greet("World"))

if __name__ == "__main__":
    main()
