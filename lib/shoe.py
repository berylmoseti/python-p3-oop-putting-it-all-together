class Shoe:
    def __init__(self, brand, size):
        # brand is a string (like "Adidas")
        self.brand = brand

        # size uses the property setter (validates input)
        self._size = None
        self.size = size

        # start with no condition by default
        self.condition = None

    # property for size (getter)
    @property
    def size(self):
        return self._size

    # property setter for size (validation happens here)
    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self._size = value
        else:
            # IMPORTANT: must match exactly what the test expects
            print("size must be an integer")

    # method for repairing the shoe
    def cobble(self):
        # set condition to "New" as required by test
        self.condition = "New"
        print("Your shoe is as good as new!")
