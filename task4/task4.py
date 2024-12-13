import sys

def read_numbers(file_path):
    with open(file_path, 'r') as file:
        return [int(line.strip()) for line in file]

def min_moves_to_equal(nums):
    nums.sort()
    median = nums[len(nums) // 2]
    return sum(abs(num - median) for num in nums)

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]

    try:
        nums = read_numbers(input_file)
        result = min_moves_to_equal(nums)
        print(result)
    except Exception as e:
        print(f"Error processing file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
