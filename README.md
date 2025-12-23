# Adaptive Taxonomy Mapper

## Overview
The Adaptive Taxonomy Mapper is a rule-based genre inference system designed to map noisy user-provided tags and short story descriptions to a predefined internal fiction taxonomy.

The system prioritizes **story context over user tags**, avoids forced classification, and explicitly supports an **UNMAPPED** outcome when confidence is insufficient. The goal is to produce **accurate, explainable, and trustworthy genre mappings**.

---

## Key Features
- Context-first genre inference
- Deterministic, rule-based classification
- Strict validation against a predefined taxonomy
- Explicit handling of ambiguous cases using UNMAPPED
- Human-readable reasoning for every decision
- No end-to-end LLM dependency for final classification

---

## Project Structure
adaptive-taxonomy-mapper/
├── mapper.py
├── taxonomy.json
├── test_cases.json
├── reasoning_log.json
├── Vinaya_Vincent_Reasoning_Log.pdf
├── Vinaya_Vincent_System_Design_Document.pdf
└── README.md

---

## How the System Works
1. **Input**: User-provided tags and a short story description  
2. **Preprocessing**: Text normalization to reduce noise  
3. **Signal Extraction**: Detection of curated genre-specific signals  
4. **Context Wins Rule**: Story content takes precedence over user tags  
5. **Taxonomy Validation**: Ensures predicted sub-genres exist in the taxonomy  
6. **Final Decision**:
   - Valid strong signal → sub-genre assigned
   - Weak or ambiguous signal → UNMAPPED
7. **Explainability**: A concise reasoning is generated for each case

---

## Running the Project

### Requirements
- Python 3.8 or above
- No external dependencies

### Run Command
```bash
python mapper.py

Output

Results are printed to the terminal

A structured reasoning log is saved to reasoning_log.json

Design Principles

Explainability over aggressiveness: The system avoids guessing

Precision over recall: Incorrect mappings are worse than UNMAPPED

Controlled outputs: No hallucinated categories

Reproducibility: Deterministic rules, consistent results

Handling UNMAPPED Cases

UNMAPPED is a deliberate design choice used when story context does not provide sufficiently strong or unambiguous signals to confidently assign a taxonomy-defined sub-genre. This prevents forced classification, reduces misclassification risk, and preserves taxonomy integrity.


Documentation

Reasoning Log: Vinaya_Vincent_Reasoning_Log.pdf

System Design Document: Vinaya_Vincent_System_Design_Document.pdf

These documents provide detailed explanations of classification decisions and architectural choices.

Conclusion

This project demonstrates a responsible and transparent approach to genre inference by combining rule-based reasoning, strict taxonomy adherence, and explicit uncertainty handling. The system is designed to be scalable, explainable, and safe for real-world use.


---




