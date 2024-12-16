class Decoder:
    def __init__(self, data):
        self.data = data
        self.index = 0
    def decode(self):
        try:
            decoded_value = self._decode_next()
            return decoded_value
        except KeyError as e:
            print(f"KeyError: {e} - Issue with index {self.index}.")
            return None
    def _decode_next(self):
        if self.index >= len(self.data):
            raise IndexError("No more data to decode.")

        try:
            current_byte = list(self.data.items())[self.index]
            self.index += 1
            return current_byte
        except KeyError:
            print(f"KeyError at index {self.index}. Check the data structure.")
            return None
