import json
class Encoder:
    @staticmethod
    def encode(data):

        if isinstance(data, dict):
            return Encoder.encode_dictionary(data)
        elif isinstance(data, str):
            return Encoder.encode_string(data)
        elif isinstance(data, list):
            return Encoder.encode_list(data)
        elif isinstance(data, int):
            return Encoder.encode_int(data)
        elif isinstance(data, float):
            return Encoder.encode_float(data)
        elif isinstance(data, bool):
            return Encoder.encode_bool(data)
        else:
            raise ValueError(f"Unsupported data type: {type(data)}")

    @staticmethod
    def encode_dictionary(data):
        encoded_data = {}
        for key, value in data.items():
            encoded_key = Encoder.encode(key)  # Recursively encode the key
            encoded_value = Encoder.encode(value)  # Recursively encode the value
            encoded_data[encoded_key] = encoded_value
        return encoded_data

    @staticmethod
    def encode_string(data):
        return data.encode('utf-8')

    @staticmethod
    def encode_list(data):
        return [Encoder.encode(item) for item in data]

    @staticmethod
    def encode_int(data):
        return data

    @staticmethod
    def encode_float(data):
        return data

    @staticmethod
    def encode_bool(data):
        return data

if __name__ == "__main__":
    with open('test_data.json') as f:
        input_data = json.load(f)

    encoded_data = Encoder.encode(input_data)

    with open('result.json', 'w') as output_file:
        json.dump(encoded_data, output_file, ensure_ascii=False, indent=4)
