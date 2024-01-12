import csv
from itertools import permutations
import string
def bits_to_ascii(bits, bit_order):
    order = list(map(int, bit_order))
    bits = [bits[i] for i in order]

    bits[0] = 0
    bits = [str(bit) for bit in bits]

    # Convert the bits to a string
    bit_string = ''.join(bits)

    # Convert binary string to decimal
    decimal_value = int(bit_string, 2)

    # Convert decimal to ASCII
    ascii_char = chr(decimal_value)

    return ascii_char

def process_csv(csv_file, bit_orders):
    results = []

    for i,bit_order in enumerate(bit_orders):
        attempt=[]
        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                ascii_char = bits_to_ascii(row, bit_order)
                attempt.append(ascii_char)
            results.append("".join(attempt))
            print(f"attempt: {i} of order{bit_order}")
            print("".join(attempt),"\n")
        
            

    return results
def contains_special_characters(s):
    # Check if the string contains any characters other than letters (both upper and lower case), numbers, basic English punctuation, and spaces
    allowed_characters = set(string.ascii_letters + string.digits + string.punctuation + ' ')
    return any(char not in allowed_characters for char in s)

def main():
    # Specify the CSV file
    csv_file = 'result.csv'

    # Generate all possible bit orders
    bit_orders = [''.join(p) for p in permutations('01234567')]

    # Process the CSV file for each bit order
    results = process_csv(csv_file, bit_orders)


    with open("translations.csv", 'a', newline='') as csv_file:
            # Create a CSV writer
            csv_writer = csv.writer(csv_file,escapechar='\\')
            # Append the list to the CSV file
            count=0
            for row in results:
                if not contains_special_characters(row):
                    csv_writer.writerow([row])
                    count+=1
            print(count,"lines were valid")
    # # Join the result into a phrase with spaces every 5 letters
    # final_phrase = ' '.join(results[i:i + 5] for i in range(0, len(results), 5))

    # print(final_phrase)

if __name__ == "__main__":
    main()
