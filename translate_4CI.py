import json
import random
import argparse

# Load the mapping from the JSON file
json_filepath = './results/4CornerIndex_mapping.json'
with open(json_filepath, 'r', encoding='utf-8') as file:
    mapping = json.load(file)

# Function to translate long number to Chinese characters
def translate_number_to_chinese(long_number):
    i = 0
    translated_text = []

    while i < len(long_number):
        chunk = long_number[i:i + 5]  # Take the next 5 digits
        movement_steps = 0
        
        while movement_steps < 5 and (i + 5 <= len(long_number)):
            if chunk in mapping:
                # Match found; select a random character from the list
                if mapping[chunk]:
                    selected_character = random.choice(mapping[chunk])
                    if not selected_character:
                        selected_character = "\n\n"
                else:
                    selected_character = "\n\n"

                translated_text.append(selected_character)
                
                # Add the separator if we moved
                if movement_steps > 0:
                    if movement_steps == 3:
                        separator = ','
                    elif movement_steps > 3:
                        separator = '.'
                    else:
                        separator = ' '

                    #translated_text.insert(-1, str(movement_steps))  # Insert separator before the last added character
                    translated_text.insert(-1, separator)  # Insert separator before the last added character
                break
            
            # If no match, move one digit forward
            movement_steps += 1
            i += 1
            chunk = long_number[i:i + 5]  # Update the chunk for the new position
            
        # If we've moved the full range and still no match, just move to the next position
        if movement_steps == 5:
            i += 1  # Move one position forward to try the next character
        else:
            i += 5  # Move forward by 5 if we found a match

    # Join the list into a single string and return
    return ''.join(translated_text)


# Main function to parse CLI arguments
def main():
    parser = argparse.ArgumentParser(description='Translate a number into Chinese text.')
    parser.add_argument('-file', type=str, help='The path to the input file containing the number.')

    args = parser.parse_args()

    if args.file:
        # Read the input number from the file specified with the -file argument
        with open(args.file, 'r', encoding='utf-8') as file:
            long_number_input = file.read().strip()  # Read and strip any extra spaces/newlines
    else:
        # Prompt the user for input if no file is specified
        long_number_input = input("Enter a long number: ")

    # Translate the number and print the output
    translated_text = translate_number_to_chinese(long_number_input)
    print(f"{translated_text}")

if __name__ == '__main__':
    main()


