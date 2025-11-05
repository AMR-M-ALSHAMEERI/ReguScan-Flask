from flask import Flask, render_template, request
import re


app = Flask(__name__)


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


@app.route("/")
def index():
    """Serve the main input form."""
    return render_template("index.html")


@app.route("/scan", methods=["POST"])
def scan():
    """Process the text and perform PII and compliance scanning."""
    # Get the text from the form
    text = request.form.get("text", "")
    
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


if __name__ == "__main__":
    app.run(debug=True)
