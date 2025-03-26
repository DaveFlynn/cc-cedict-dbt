import csv
import os
import re

INPUT_PATH = "./data/cc-cedict.txt"
OUTPUT_PATH = "./seeds/cc_cedict.csv"

# Regular expression to parse CEDICT line
LINE_REGEX = re.compile(r"^(\S+)\s+(\S+)\s+\[(.+?)\]\s+/(.+)/")

def parse_line(line):
    match = LINE_REGEX.match(line)
    if match:
        return {
            "traditional": match.group(1),
            "simplified": match.group(2),
            "pinyin": match.group(3),
            "definitions": match.group(4)
        }
    return None

def main():
    if not os.path.exists(INPUT_PATH):
        print(f"File not found: {INPUT_PATH}")
        return

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

    with open(INPUT_PATH, "r", encoding="utf-8") as infile, \
         open(OUTPUT_PATH, "w", newline='', encoding="utf-8") as outfile:

        writer = csv.DictWriter(outfile, fieldnames=["traditional", "simplified", "pinyin", "definitions"])
        writer.writeheader()

        for line in infile:
            line = line.strip()
            if line.startswith("#") or not line:
                continue
            parsed = parse_line(line)
            if parsed:
                writer.writerow(parsed)

    print(f"Parsed and saved: {OUTPUT_PATH}")

if __name__ == "__main__":
    main()