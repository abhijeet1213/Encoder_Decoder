import json
from decoder import Decoder

def run_error_tests():

    test_data = {
        "key1": "value1",
        "key2": "value2"
    }

    decoder = Decoder(data=test_data)

    try:
        decoded_data = decoder.decode()
        print("Decoded data:", decoded_data)
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    run_error_tests()
