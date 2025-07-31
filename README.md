Resume Parser (Python + Flask + SQLite)

A simple web app that extracts key information from uploaded resumes (PDF or DOCX) and saves it in a local database.

Features

- Upload resumes (.pdf or .docx)
- Extract name, education, and organizations using spaCy
- Store results in an SQLite database
- View parsed data after upload

Technologies Used

- Python
- Flask
- spaCy
- pdfplumber
- python-docx
- SQLite

git clone https://github.com/your-username/resume-parser.git
cd resume-parser

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
python -m spacy download en_core_web_sm

python app.py

Then open [http://localhost:5000](http://localhost:5000) in your browser.

Folder Structure
resume_parser/
├── app.py
├── database.py
├── extractor.py
├── parser.py
├── templates/
│   └── upload.html
├── uploads/
├── requirements.txt
└── README.md
