import os
import re

def css_hex_color_code_matcher(input_text):
    # Remove CSS comments (non-greedy)
    modified_text = re.sub(r'/\*.*?\*/', '', input_text, flags=re.DOTALL)
    
    # Find valid hex color codes: # followed by exactly 3 or 6 hex digits
    hex_codes = re.findall(r'#[0-9a-fA-F]{6}\b|#[0-9a-fA-F]{3}\b', modified_text)
    
    return modified_text.strip(), hex_codes

# Driver Code
if __name__ == "__main__":
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    text = input()
    modified_text, matched_hex_color_codes = css_hex_color_code_matcher(text)
    fptr.write("Modified Text: " + modified_text)
    fptr.write("\n")
    sorted_array = sorted(matched_hex_color_codes)
    space_separated_values = ' '.join(map(str, sorted_array))
    fptr.write("Matched Hex Color Codes: " + space_separated_values)
    fptr.close()
