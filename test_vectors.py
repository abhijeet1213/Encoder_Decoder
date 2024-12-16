import json
from decoder import Decoder

def run_test_vectors():

    with open('test_data.json', 'r') as file:
        test_data = json.load(file)

    decoder = Decoder(test_data)

    decoded_data = decoder.decode()

    with open('result.json', 'w') as file:
        json.dump(decoded_data, file, indent=4)

if __name__ == "__main__":
    run_test_vectors()
