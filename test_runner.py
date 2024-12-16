import json
from encoder import Encoder
from decoder import Decoder

with open('test_data.json') as f:
    input_data = json.load(f)

encoded_data = Encoder.encode(input_data)

print("Encoded Data:", encoded_data)

decoder = Decoder(encoded_data)
decoded_data = []
while True:
    try:
        decoded_data.append(decoder.decode())
    except (IndexError, ValueError):
        break

print("Decoded Data:", decoded_data)

with open('result.json', 'w') as f:
    json.dump(decoded_data, f, ensure_ascii=False, indent=4)

print("Decoding completed and saved to result.json.")
