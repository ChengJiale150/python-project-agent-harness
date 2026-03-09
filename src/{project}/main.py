def hello(name: str = "World") -> str:
    """A simple hello function."""
    return f"Hello, {name}!"

def main() -> None:
    """Entry point for the project."""
    print(hello())

if __name__ == "__main__":
    main()
