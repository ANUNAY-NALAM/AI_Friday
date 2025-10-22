import re

def scrub_line(line):
    # Replace the Groq API key with a placeholder
    # Example: if the key looks like "GROQ-123456-XYZ", remove it
    return re.sub(r'GROQ-[A-Za-z0-9-]+', '<REDACTED>', line)

def scrub_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    with open(path, 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(scrub_line(line))