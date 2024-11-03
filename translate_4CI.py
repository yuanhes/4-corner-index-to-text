import json
import random

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
                selected_character = random.choice(mapping[chunk])
                translated_text.append(selected_character)
                
                # Add the separator if we moved
                if movement_steps > 0:
                    separator = ',' if movement_steps < 5 else '.'
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

# Example usage
long_number_input = input("Enter a long number: ")  # Receive input as a string
translated_text = translate_number_to_chinese(long_number_input)
print(f"Translated Chinese text: {translated_text}")

