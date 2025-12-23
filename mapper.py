"""
Adaptive Taxonomy Mapper
------------------------
Rule-based, explainable genre inference system.
LLMs are not used for final classification.
"""

print(">>> mapper.py is running <<<")

import json
import re
from pathlib import Path

# -----------------------------
# Robust JSON loader (handles UTF-8 BOM)
# -----------------------------
def load_json(path):
    with open(path, "r", encoding="utf-8-sig") as f:
        return json.load(f)

# -----------------------------
# Load input files
# -----------------------------
BASE_DIR = Path(__file__).parent

taxonomy = load_json(BASE_DIR / "taxonomy.json")["Fiction"]
test_cases = load_json(BASE_DIR / "test_cases.json")

# -----------------------------
# Hand-crafted genre signals
# (carefully chosen to avoid false positives)
# -----------------------------
SIGNALS = {
    "Enemies-to-Lovers": [
        "hated",
        "enemies",
        "rivals",
        "forced to work"
    ],
    "Second Chance": [
        "years later",
        "met again",
        "reunited",
        "after years",
        "second chance"
    ],
    "Legal Thriller": [
        "lawyer",
        "judge",
        "court",
        "trial",
        "cross-examination",
        "verdict"
    ],
    "Espionage": [
        "agent",
        "spy",
        "covert",
        "classified",
        "mission"
    ],
    "Slasher": [
        "masked killer",
        "stalks",
        "teenagers",
        "blood"
    ],
    "Hard Sci-Fi": [
        "physics",
        "scientific theory",
        "ftl",
        "relativity"
    ],
    "Cyberpunk": [
        "neon",
        "artificial intelligence",
        "megacity",
        "megacorp",
        "cybernetic",
        "hacker"
    ],
    "Gothic": [
        "victorian",
        "mansion",
        "dark past",
        "ancestral",
        "decaying estate"
    ]
}

# -----------------------------
# Utility functions
# -----------------------------
def normalize(text: str) -> str:
    return re.sub(r"[^a-z ]", "", text.lower())

def extract_signals(story: str):
    story = normalize(story)
    matches = []

    for genre, keywords in SIGNALS.items():
        for kw in keywords:
            if kw in story:
                matches.append(genre)
                break

    return matches

def validate_against_taxonomy(candidate: str) -> bool:
    for _, subgenres in taxonomy.items():
        if candidate in subgenres:
            return True
    return False

def classify_story(story: str):
    signals = extract_signals(story)

    if not signals:
        return (
            "UNMAPPED",
            "The story lacks sufficiently specific narrative cues to confidently map it to any defined taxonomy sub-genre."
        )

    # Context Wins Rule: strongest signal first
    chosen = signals[0]

    if not validate_against_taxonomy(chosen):
        return (
            "UNMAPPED",
            f"The identified signal '{chosen}' does not exist in the approved taxonomy."
        )

    return (
        chosen,
        f"Story context strongly indicates '{chosen}', overriding generic or noisy user tags."
    )

# -----------------------------
# Run classification
# -----------------------------
results = []

for case in test_cases:
    genre, reasoning = classify_story(case["story"])

    result = {
        "id": case["id"],
        "predicted_genre": genre,
        "reasoning": reasoning
    }

    results.append(result)

    # Terminal output for visibility
    print(f"\nCase {case['id']}")
    print("Predicted Genre:", genre)
    print("Reasoning:", reasoning)

# -----------------------------
# Save reasoning log
# -----------------------------
output_path = BASE_DIR / "reasoning_log.json"

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2)

print("\n Mapping completed successfully.")
print(f" Results saved to: {output_path}")
