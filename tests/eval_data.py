# Harder test set. Includes:
#  - overlapping-topic questions (must distinguish similar chunks)
#  - paraphrased questions (few/no shared words with the answer chunk)

TEST_SET = [
    # Overlapping: mountains
    {"question": "How tall is Everest?", "expected_keyword": "8,849 meters"},
    {"question": "Which mountain is the second highest on Earth?", "expected_keyword": "8,611 meters"},
    {"question": "What is the tallest peak in Africa?", "expected_keyword": "Kilimanjaro"},

    # Overlapping: programming languages
    {"question": "Which language is best for machine learning?", "expected_keyword": "data science"},
    {"question": "What language runs inside web browsers?", "expected_keyword": "JavaScript"},
    {"question": "Which language avoids a garbage collector for memory safety?", "expected_keyword": "Rust"},

    # Overlapping: organs
    {"question": "What organ removes toxins and makes bile?", "expected_keyword": "liver"},
    {"question": "How many times does the heart beat daily?", "expected_keyword": "100,000 times"},

    # Paraphrased / few shared words with source
    {"question": "Where do plants make food from light?", "expected_keyword": "chloroplasts"},
    {"question": "What forest is a major source of the planet's breathable air?", "expected_keyword": "Amazon"},
    {"question": "What ancient barrier was made to stop attackers from the north?", "expected_keyword": "Great Wall"},
    {"question": "What handles gas exchange when you inhale?", "expected_keyword": "lungs"},
]
