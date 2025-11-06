from flask import Flask, render_template, request
import re
import os
from werkzeug.utils import secure_filename
import PyPDF2
from docx import Document


app = Flask(__name__)

# Upload configuration
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'.txt', '.pdf', '.docx'}
MAX_FILE_SIZE = 16 * 1024 * 1024  # 16 MB

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_FILE_SIZE

# Create upload folder if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# PII Risk Patterns Dictionary
PII_RISK_PATTERNS = {
    "Email Address": {
        "pattern": r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,6}",
        "risk": "High"
    },
    "Credit Card (VISA/Mastercard)": {
        "pattern": r"(?:4\d{3}|5[1-5]\d{2})[ -]?\d{4}[ -]?\d{4}[ -]?\d{4}",
        "risk": "High"
    },
    "US Social Security Number (SSN)": {
        "pattern": r"\b\d{3}[ -]?\d{2}[ -]?\d{4}\b",
        "risk": "High"
    },
    "IPv4 Address": {
        "pattern": r"\b(?:\d{1,3}\.){3}\d{1,3}\b",
        "risk": "Medium"
    },
    "Phone Number (US/Simple Intl)": {
        "pattern": r"\b(?:\d{3}[-.\s]?){2}\d{4}\b",
        "risk": "Medium"
    }
}

# Compliance Keyword Patterns Dictionary
COMPLIANCE_KEYWORDS = {
    "Data Rights": [
        "Right to be Forgotten",
        "Right to Access",
        "Right to Rectification",
        "Right to Opt-Out",
        "Data Portability",
        "Data Subject Request",
        "DSAR"
    ],
    "Policy/Consent": [
        "Cookie Policy",
        "Privacy Notice",
        "Lawful Basis",
        "Legitimate Interest",
        "Explicit Consent",
        "Data Processing Agreement",
        "DPA"
    ],
    "Security/Transfers": [
        "Data Breach Notification",
        "Data Transfer",
        "Third Parties",
        "Security Measures",
        "Encryption",
        "Anonymization"
    ]
}


def allowed_file(filename):
    """Check if file extension is allowed."""
    return any(filename.lower().endswith(ext) for ext in ALLOWED_EXTENSIONS)


def extract_text_from_file(filepath, filename):
    """Extract text from uploaded file based on extension."""
    extension = os.path.splitext(filename.lower())[1]
    
    try:
        if extension in ['.txt']:
            # Plain text files
            with open(filepath, 'r', encoding='utf-8') as f:
                return f.read()
        
        elif extension == '.pdf':
            # PDF files
            text = ""
            with open(filepath, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                for page in pdf_reader.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"
            return text
        
        elif extension == '.docx':
            # Word documents
            doc = Document(filepath)
            text = ""
            
            # Extract paragraphs
            for paragraph in doc.paragraphs:
                text += paragraph.text + "\n"
            
            # Extract tables
            for table in doc.tables:
                for row in table.rows:
                    for cell in row.cells:
                        text += cell.text + " "
                    text += "\n"
            
            return text
        
        else:
            return None  # Unsupported format
            
    except Exception as e:
        print(f"Error extracting text from {filename}: {e}")
        return None


@app.route("/")
def index():
    """Serve the main input form."""
    return render_template("index.html")


@app.route("/scan", methods=["POST"])
def scan():
    """Process the text and perform PII and compliance scanning."""
    text = ""
    error_message = None
    
    # Check if file was uploaded
    if 'file' in request.files and request.files['file'].filename != '':
        file = request.files['file']
        
        # Validate file
        if not allowed_file(file.filename):
            error_message = "Invalid file type. Only .txt, .pdf, and .docx files are allowed."
        else:
            # Save file temporarily
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            
            try:
                file.save(filepath)
                
                # Extract text from file
                text = extract_text_from_file(filepath, filename)
                
                # Clean up temporary file
                os.remove(filepath)
                
                if text is None or text.strip() == "":
                    error_message = "Could not extract text from file. Please ensure it's not empty or corrupted."
                    
            except Exception as e:
                error_message = f"Error processing file: {str(e)}"
                # Clean up file if it exists
                if os.path.exists(filepath):
                    os.remove(filepath)
    
    else:
        # Get text from textarea
        text = request.form.get("text", "")
    
    # Check if we have text to scan
    if not text or text.strip() == "":
        if not error_message:
            error_message = "Please provide text to scan or upload a file."
        return render_template("index.html", error=error_message)
    
    # If there was an error during file processing, show it
    if error_message:
        return render_template("index.html", error=error_message)
    
    # Split text into lines for line number tracking
    lines = text.split("\n")
    
    # PII Risk Findings
    risk_findings = []
    
    # Scan for PII patterns
    for pii_type, pii_info in PII_RISK_PATTERNS.items():
        pattern = pii_info["pattern"]
        risk_level = pii_info["risk"]
        
        # Search each line for matches
        for line_num, line in enumerate(lines, start=1):
            matches = re.finditer(pattern, line)
            for match in matches:
                # Extract snippet with context (up to 50 chars around match)
                start = max(0, match.start() - 10)
                end = min(len(line), match.end() + 10)
                snippet = line[start:end]
                
                risk_findings.append({
                    "type": pii_type,
                    "risk_level": risk_level,
                    "line_number": line_num,
                    "snippet": snippet,
                    "matched_text": match.group()
                })
    
    # Compliance Keyword Status
    compliance_status = []
    
    # Check for compliance keywords (case-insensitive)
    text_lower = text.lower()
    
    for category, keywords in COMPLIANCE_KEYWORDS.items():
        found_keywords = []
        missing_keywords = []
        
        for keyword in keywords:
            if keyword.lower() in text_lower:
                found_keywords.append(keyword)
            else:
                missing_keywords.append(keyword)
        
        compliance_status.append({
            "category": category,
            "found": found_keywords,
            "missing": missing_keywords,
            "has_any": len(found_keywords) > 0
        })
    
    # Render results template with findings
    return render_template("report.html", 
                         risk_findings=risk_findings, 
                         compliance_status=compliance_status,
                         total_risks=len(risk_findings))


@app.errorhandler(413)
def request_entity_too_large(error):
    """Handle file too large error."""
    return render_template("index.html", 
                         error="File is too large! Maximum file size is 16 MB. Please upload a smaller file."), 413


if __name__ == "__main__":
    app.run(debug=True)
