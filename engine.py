import argparse
import yaml
import re

# --- PARSE CLI ARGS ---
parser = argparse.ArgumentParser(description="Intonate: Markdown → SSML engine")
parser.add_argument('--input', required=True, help='Path to input Markdown file')
parser.add_argument('--config', required=True, help='Path to YAML config with SSML rules')
parser.add_argument('--output', required=True, help='Path to output SSML file')
parser.add_argument('--profile', default='core', choices=['core', 'extended'],
                    help="Which SSML profile to use: 'core' or 'extended'. Default is 'core'.")
args = parser.parse_args()

# --- READ INPUT FILE ---
with open(args.input, 'r') as f:
    text = f.read()

# --- LOAD YAML RULES ---
with open(args.config, 'r') as f:
    config = yaml.safe_load(f)

rules = config.get('rules', [])
used_rules = [] # Track which rules actually match input

# --- VALIDATE RULES ---
print("🔍 Validating rules...")

for rule in rules:
    name = rule.get('name', '<unnamed>')
    match = rule.get('match')
    tag = rule.get('tag')

    # Validate match exists and compiles
    if not match:
        raise ValueError(f"❌ Rule '{name}' is missing a 'match' pattern.")
    try:
        re.compile(match)
    except re.error as e:
        raise ValueError(f"❌ Rule '{name}' has invalid regex: {e}")

    # Validate tag is a string
    if not isinstance(tag, str) or tag.strip() == '':
        raise ValueError(f"❌ Rule '{name}' has an empty or invalid 'tag'.")

    # Warn if rule uses capture group but tag does not reference \1
    if '(' in match and '\\1' not in tag:
        print(f"⚠️ Warning: Rule '{name}' has a capture group but tag has no '\\1' reference.")

print("✅ Rule validation complete.\n")


# --- APPLY RULES ---
selected_profile = args.profile

for rule in rules:
    rule_profile = rule.get('profile', 'core')
    if selected_profile == 'core' and rule_profile != 'core':
        continue

    print(f"Applying rule: {rule['name']}")
    
    pattern = re.compile(rule['match'], re.MULTILINE)

    def safe_sub(match):
        used_rules.append(rule['name']) # ✅ Log usage, even if content unchanged
        
        # Warn if no capture group and no \1 in tag
        if '\\1' not in rule['tag']:
            snippet = match.group(0).strip()
            print(f"⚠️ Rule '{rule['name']}' matched content but discards it: \"{snippet}\"")
            return snippet  # Output original content unchanged
        return re.sub(pattern, rule['tag'], match.group(0))

    new_text = pattern.sub(safe_sub, text)


    if new_text != text:
        print(f"✅ Rule '{rule['name']}' matched and made a change.")
        used_rules.append(rule['name'])

    text = new_text

# --- REPORT UNUSED RULES ---
unused_rules = [
    rule['name'] for rule in rules 
    if rule['name'] not in used_rules 
    and (selected_profile == 'extended' or rule.get('profile', 'core') == 'core')
]

if unused_rules:
    print("\n⚠️ The following rules did not match anything in the input:")
    for rule_name in unused_rules:
        print(f"  - {rule_name}")

# --- WRAP IN <speak> TAG ---
ssml_output = f"<speak>\n{text}\n</speak>"

# --- WRITE OUTPUT FILE ---
with open(args.output, 'w') as f:
    f.write(ssml_output)

print("✅ Intonate processing complete.")
print(f"Input: {args.input}")
print(f"Output: {args.output}")
