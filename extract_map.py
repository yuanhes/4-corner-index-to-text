from bs4 import BeautifulSoup
import html
import re


# Read the HTML file with the appropriate encoding
htm_filepath = "./4CI_HTM/four_corner_index_of_chinese_characters-revised_version.htm"
with open(htm_filepath, 'r', encoding='gb18030') as file:
    soup = BeautifulSoup(file, 'html.parser')

# Find all <p> elements with the class "MsoNormal"
paragraphs = soup.find_all('p', class_='MsoNormal')

pattern = re.compile(r'^\*(\d{5})：(.*)')

# Loop through each paragraph to extract and decode content
count = 0 
for p in paragraphs:
    spans = p.find_all('span')  # Find all <span> elements within the <p> tag
    
    # Combine the text content of each <span>, decoding any numeric references
    combined_text = ''.join([html.unescape(span.get_text()) for span in spans])
    
    # Search for the pattern in the combined text
    match = pattern.search(combined_text)
    if match:
        count += 1
        number = match.group(1)
        characters = match.group(2).encode('utf-8', errors='ignore').decode('utf-8')
        char_list = list(characters)
        print(f"{count} : {number} {char_list}")
 

