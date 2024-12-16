import argparse
import json
import time
from decoder import Decoder

def run_performance_test(input_file, output_file):

    with open(input_file, 'r') as file:
        input_data = json.load(file)

    decoder = Decoder(data=input_data)

    start_time = time.time()

    decoded_data = decoder.decode()

    end_time = time.time()
    elapsed_time = end_time - start_time

    performance_metrics = {
        'decoded_data': decoded_data,
        'elapsed_time_seconds': elapsed_time
    }

    with open(output_file, 'w') as outfile:
        json.dump(performance_metrics, outfile, indent=4)

    print(f"Performance test completed in {elapsed_time:.4f} seconds")
    print(f"Decoded data saved to {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Performance test for decoding")
    parser.add_argument('--input', required=True, help="Input JSON file")
    parser.add_argument('--output', required=True, help="Output JSON file")

    args = parser.parse_args()

    run_performance_test(args.input, args.output)
