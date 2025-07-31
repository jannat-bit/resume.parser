from flask import Flask, request, render_template
from extractor import extract_text_from_pdf, extract_text_from_docx
from parser import parse_resume_text
from database import insert_candidate
import os
from werkzeug.utils import secure_filename

# Flask app configuration
app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Create uploads folder if it doesn't exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route("/", methods=["GET", "POST"])
def upload_resume():
    if request.method == "POST":
        file = request.files['resume']
        if not file:
            return "No file uploaded", 400
        
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Extract text based on file type
        if filename.endswith(".pdf"):
            text = extract_text_from_pdf(file_path)
        elif filename.endswith(".docx"):
            text = extract_text_from_docx(file_path)
        else:
            return "Unsupported file type. Please upload PDF or DOCX.", 400

        # Parse the resume content
        parsed_data = parse_resume_text(text)

        # Store in database
        insert_candidate(parsed_data)

        return f"""
        <h3>Resume Parsed and Stored Successfully</h3>
        <p><strong>Name:</strong> {parsed_data['name']}</p>
        <p><strong>Education:</strong> {', '.join(parsed_data['education'])}</p>
        <p><strong>Organizations:</strong> {', '.join(parsed_data['organizations'])}</p>
        <a href="/">Upload Another</a>
        """
    
    return render_template("upload.html")

if __name__ == "__main__":
    app.run(debug=True)
