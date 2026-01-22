class Plant:
    """
    A secure plant class that protects data integrity using encapsulation.
    """

    def __init__(self, name: str, height: int, age: int):
        """
        Initialize the secure plant with protected attributes.
        """
        self.name = name
        self._height = height
        self._age = age

    # setter & getter (Age)
    def get_height(self) -> int:
        """Return the current height."""
        return self._height

    def set_height(self, value: int):
        """
        Update height safely. Rejects negative values.
        """
        if value < 0:
            print(f"\nInvalid operation attempted:"
                  f" height {value}cm [REJECTED]")

            print("Security: Negative height rejected")
        else:
            self._height = value
            print(f"Height updated: {self._height}cm [OK]")

    # setter & getter (Age)
    def get_age(self) -> int:
        """Return the current age."""
        return f"{self._age}"

    def set_age(self, value: int):
        """
        Update age safely. Rejects negative values.
        """
        if value < 0:
            print(f"\nInvalid operation attempted:"
                  f" age {value} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self._age = value
            print(f"Age updated: {self._age} days [OK]")


print("=== Garden Security System ===")
rose = Plant("Rose", 0, 0)
print(f"Plant created: {rose.name}")
rose.set_height(25)
rose.set_age(30)
rose.set_height(-5)
print(f"\nCurrent plant: {rose.name}"
      f" ({rose.get_height()}cm, {rose.get_age()} days)")
