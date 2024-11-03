from bs4 import BeautifulSoup
import html
import re
import json

# Read the HTML file with the appropriate encoding

htm_filepath = "./4CI_HTM/four_corner_index_of_chinese_characters-revised_version.htm"
with open(htm_filepath, 'r', encoding='gb18030') as file:
    soup = BeautifulSoup(file, 'html.parser')

# Find all <p> elements with the class "MsoNormal"
paragraphs = soup.find_all('p', class_='MsoNormal')

# Regular expression pattern to match a five-digit number followed by Chinese characters
pattern = re.compile(r'^\*(\d{5})：(.*)')

# Initialize a dictionary to store the mappings
mapping = {}

#count = 0 
# Loop through each paragraph to extract and decode content
for p in paragraphs:
    spans = p.find_all('span')  # Find all <span> elements within the <p> tag
    
    # Combine the text content of each <span>, decoding any numeric references
    combined_text = ''.join([html.unescape(span.get_text()) for span in spans])
    
    # Search for the pattern in the combined text
    match = pattern.search(combined_text)
    if match:
        #count += 1
        number = match.group(1)
        characters = match.group(2).encode('utf-8', errors='ignore').decode('utf-8')
        char_list = list(characters)
        #print(f"{count} : {number} {char_list}")
        # Add the mapping to the dictionary
        mapping[number] = char_list


# Save the mapping to a JSON file
json_filepath = './results/4CornerIndex_mapping.json'
with open(json_filepath, 'w', encoding='utf-8') as file:
    json.dump(mapping, file, ensure_ascii=False, indent=4)

print(f"Mapping data has been stored into \'{json_filepath}\' .")

