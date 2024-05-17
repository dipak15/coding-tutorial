import sys

# Check if there are enough command-line arguments
if len(sys.argv) < 3:
    print("Usage: python concatenate_strings.py <string1> <string2> [<string3> ...]")
    sys.exit(1)

# Get the input strings from command-line arguments
strings = sys.argv[1:]

# Concatenate the strings
result = ' '.join(strings)

# Print the result
print(result)

