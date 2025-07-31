import spacy

nlp = spacy.load("en_core_web_sm")

def parse_resume_text(text):
    doc = nlp(text)
    name = [ent.text for ent in doc.ents if ent.label_ == "PERSON"]
    organizations = [ent.text for ent in doc.ents if ent.label_ == "ORG"]
    education = [ent.text for ent in doc.ents if ent.label_ in ["ORG", "EDUCATION"]]
    # Skills will likely need custom rule-based logic
    return {
        "name": name[0] if name else "Unknown",
        "education": education,
        "organizations": organizations,
    }
