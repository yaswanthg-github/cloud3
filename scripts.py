import os
import re
import socket
from collections import Counter

# Detect if running inside Docker
inside_docker = os.path.exists("/home/data")

# Use correct paths based on the environment
if inside_docker:
    file1 = "IF-1.txt"
    file2 = "AlwaysRememberUsThisWay-1.txt"
    output_dir = "output"
else:
    file1 = "IF-1.txt"
    file2 = "AlwaysRememberUsThisWay-1.txt"
    output_dir = "output"

# Function to read file content
def read_file(file_path):
    if not os.path.exists(file_path):
        print(f"Error: {file_path} is missing!")
        return None
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read().lower()

# Function to count words
def count_words(text):
    words = re.findall(r'\b\w+\b', text)
    return len(words), Counter(words)

# Function to handle contractions
def handle_contractions(text):
    contractions = {
        "can't": "cannot", "won't": "will not", "n't": " not",
        "'re": " are", "'ll": " will", "'ve": " have",
        "'m": " am", "'s": " is", "'d": " had"
    }
    for contraction, replacement in contractions.items():
        text = text.replace(contraction, replacement)
    
    words = re.findall(r'\b\w+\b', text)
    return len(words), Counter(words)

# Read and process files
text1 = read_file(file1)
text2 = read_file(file2)

if text1 is None or text2 is None:
    print("❌ Error: One or both files are missing! Ensure IF-1.txt and AlwaysRememberUsThisWay-1.txt are in the correct directory.")
    exit(1)

word_count1, freq_words1 = count_words(text1)
word_count2, freq_words2 = handle_contractions(text2)

# Grand total of words across both files
total_words = word_count1 + word_count2

# Top 3 most frequent words in each file
top3_file1 = freq_words1.most_common(3)
top3_file2 = freq_words2.most_common(3)

# Get the machine's IP address
ip_address = socket.gethostbyname(socket.gethostname())

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Output file path
output_path = os.path.join(output_dir, "result.txt")

# Write results to result.txt
with open(output_path, 'w', encoding='utf-8') as result_file:
    result_file.write(f"Word count for IF-1.txt: {word_count1}\n")
    result_file.write(f"Word count for AlwaysRememberUsThisWay-1.txt: {word_count2}\n")
    result_file.write(f"Grand total of words: {total_words}\n")
    result_file.write(f"Top 3 words in IF-1.txt: {top3_file1}\n")
    result_file.write(f"Top 3 words in AlwaysRememberUsThisWay-1.txt: {top3_file2}\n")
    result_file.write(f"Machine IP Address for Yaswanth Gangula M16552731: {ip_address}\n")

# Print the contents of result.txt
with open(output_path, 'r', encoding='utf-8') as file:
    print(file.read())
