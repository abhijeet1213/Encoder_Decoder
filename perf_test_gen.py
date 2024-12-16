import json
import random
import string

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Generate performance test data.")
    parser.add_argument("--size", type=int, required=True, help="Size of the test data in bytes.")
    parser.add_argument("--seed", type=int, required=True, help="Random seed for reproducibility.")
    parser.add_argument("--output", required=True, help="Output JSON file.")

    args = parser.parse_args()

    random.seed(args.seed)

    def random_string(length):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

    data = {random_string(5): random.randint(0, 1000) for _ in range(args.size // 10)}

    with open(args.output, "w") as f:
        json.dump(data, f, indent=4)

    print(f"Test data generated and saved to {args.output}")
