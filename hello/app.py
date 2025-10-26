def greet(name: str) -> str:
    if name is None:
        return "Hello, World!"
    if name == "":
        return "Hello, World!"
    if name.strip() == "":
        return "Hello, !"
    return f"Hello, {name.strip()}!"

def main() -> None:
    print("Hello, World!")

if __name__ == "__main__":
    main()
