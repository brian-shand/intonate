import re
import yaml
import os
import argparse

# --- CLI ARGUMENT PARSING ---
parser = argparse.ArgumentParser(description="Intonate: Markdown to SSML processor")
parser.add_argument('--input', required=True, help='Path to input Markdown file')
parser.add_argument('--config', required=True, help='Path to YAML config file')
parser.add_argument('--output', required=True, help='Path to write processed output')
args = parser.parse_args()

# --- LOAD CONFIG ---
with open(args.config, 'r') as config_file:
    config = yaml.safe_load(config_file)

rules = config.get('rules', [])

# --- READ INPUT FILE ---
with open(args.input, 'r') as input_file:
    lines = input_file.readlines()

output_lines = []

# --- APPLY RULES ---
for line in lines:
    for rule in rules:
        pattern = re.compile(rule['match'])
        if pattern.search(line):
            line = pattern.sub(rule['replacement'], line)
    output_lines.append(line)

# --- WRITE OUTPUT FILE ---
os.makedirs(os.path.dirname(args.output), exist_ok=True)

with open(args.output, 'w', encoding='utf-8') as output_file:
    output_file.write('<speak>\n')
    output_file.writelines(output_lines)
    output_file.write('\n</speak>')

print(f"✅ Intonate processing complete.\nInput: {args.input}\nOutput: {args.output}")
