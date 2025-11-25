# ReguScan-Flask

**Automated GDPR/CCPA Compliance Scanning and Reporting Tool**

A simple yet powerful web application built with Flask that scans text documents for Personally Identifiable Information (PII) and compliance keywords related to GDPR and CCPA regulations.

## Features

### 🔍 PII Detection
**High Risk Items:**
- **Email Addresses** - Contact information exposure
- **Credit Card Numbers** (VISA/Mastercard) - Financial fraud risk
- **US Social Security Numbers (SSN)** - Identity theft potential
- **Passport Numbers** - International identity documents
- **IBAN (Bank Account Numbers)** - Banking information exposure
- **Date of Birth** - Personal identification data

**Medium Risk Items:**
- **IPv4 Addresses** - Network information
- **Phone Numbers** (US/International) - Contact information
- **MAC Addresses** - Hardware identifiers

### 📋 Compliance Keyword Scanning
Detects keywords across **8 comprehensive categories**:

**Regulatory Frameworks:**
- GDPR, CCPA

**GDPR Compliance (19 keywords):**
- Right to be Forgotten, Right to Rectification, Data Subject Request (DSAR), Lawful Basis, Legitimate Interest
- Data Protection Officer (DPO), Controller, Processor, Joint Controller
- Privacy by Design, Privacy by Default, Data Protection Impact Assessment (DPIA)
- Supervisory Authority, Consent Withdrawal, Profiling, Automated Decision-Making

**CCPA Compliance (9 keywords):**
- Right to Opt-Out, Do Not Sell My Personal Information, California Consumer Privacy Act
- Sale of Personal Information, Consumer Request, Authorized Agent
- Financial Incentive, Notice at Collection, Categories of Personal Information

**Data Rights (General):**
- Right to Access, Data Portability

**Policy/Consent:**
- Cookie Policy, Privacy Notice, Explicit Consent, Data Processing Agreement (DPA)

**Security/Transfers:**
- Data Breach Notification, Data Transfer, Third Parties, Security Measures, Encryption, Anonymization

**Compliance Timeframes:**
- "within 72 hours", "72 hours", "30 days", "within 30 days"

### 🎯 Risk Severity Enhancement
Intelligent risk assessment with critical pattern detection:

**Critical Risk Patterns:**
- **Identity Theft Risk**: SSN + Credit Card combination detected
- **Financial Fraud Risk**: Credit Card/IBAN with Email combination
- **Full Identity Profile**: SSN/Passport + Date of Birth + Email
- **Mass Data Exposure**: 50+ PII items found (or 20+ for high volume warning)

**Severity Levels:**
- 🔴 **Critical**: PII involved in dangerous combinations
- 🟠 **High**: Sensitive PII without additional context
- 🔵 **Medium**: Lower-risk identifiers (IP, Phone, MAC addresses)

**Visual Indicators:**
- Color-coded table rows (red/orange/blue backgrounds)
- Font Awesome icons for each severity level
- Dedicated "Critical Risk Alerts" section with detailed warnings
- Summary cards showing counts per severity level

### 📤 File Upload Support
- **Multiple File Formats**: Upload `.txt`, `.pdf`, or `.docx` documents
- **Drag & Drop**: Intuitive drag-and-drop interface for easy file upload
- **File Size Limit**: Supports files up to 16 MB
- **Automatic Text Extraction**: 
  - Plain text files (`.txt`)
  - PDF documents with PyPDF2
  - Word documents with python-docx (paragraphs and tables)

### ✨ User Interface
- Clean, modern responsive design with tab-based input (Paste Text / Upload File)
- Font Awesome icons throughout
- Color-coded risk levels (High = Red, Medium = Yellow)
- **Page Load Preloader**: Animated brand introduction on first visit
- **Scanning Progress Stages**: Real-time progress bar with detailed scanning stages
  - File Upload: 5 stages (Uploading → Extracting → PII Scan → Compliance Check → Report)
  - Text Input: 3 stages (PII Scan → Compliance Check → Report)
- Dynamic copyright year
- Professional print/PDF export functionality

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/AMR-M-ALSHAMEERI/ReguScan-Flask.git
   cd ReguScan-Flask
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Open your browser**
   Navigate to `http://127.0.0.1:5000`

## Usage

### Input Methods

#### Option 1: Paste Text
1. Click the **"Paste Text"** tab
2. Enter or paste your text in the textarea
3. Click **"Scan Document"** to analyze

#### Option 2: Upload File
1. Click the **"Upload File"** tab
2. Either:
   - **Drag and drop** a file onto the upload area, or
   - **Click** to browse and select a file
3. Supported formats: `.txt`, `.pdf`, `.docx` (max 16 MB)
4. Click **"Scan Document"** to analyze

### Results

After scanning, you'll see:

**Summary Cards (4 cards):**
- Total PII risks found
- Compliance categories scanned
- Critical risk items count
- High risk items count

**Critical Risk Alerts Section:**
- 🚨 Prominent warnings for dangerous PII combinations
- Identity theft risks (SSN + Credit Card)
- Financial fraud risks (Banking + Email)
- Full identity profiles (Passport + DOB + Email)
- Mass exposure warnings (20+ or 50+ items)

**PII Findings Table with Severity:**
- **Severity Column**: Color-coded icons (Critical/High/Medium)
- **Risk Level**: Original risk classification
- **PII Type**: Specific pattern detected (9 types)
- **Line Number**: Location in document
- **Matched Pattern**: Actual sensitive data found
- **Context Snippet**: Surrounding text for verification
- **Row Highlighting**: Red (Critical), Orange (High), Blue (Medium)

**Compliance Grid (8 categories):**
- Regulatory Frameworks (GDPR, CCPA)
- GDPR Compliance (19 keywords)
- CCPA Compliance (9 keywords)
- Data Rights (General)
- Policy/Consent
- Security/Transfers
- Compliance Timeframes
- **Found vs Missing Keywords**: Clear ✓/✗ indicators for compliance gaps

### Progress Tracking

Watch real-time progress during scanning:
- **File uploads** show 5 stages with progress percentage
- **Text input** shows 3 stages with progress percentage
- Detailed descriptions of current operation

### Export Options

- **Print Report**: Opens browser print dialog with optimized layout
- **Save as PDF**: Use browser's "Save as PDF" option
- **Enable "Background graphics"** in print settings to preserve colors

## Project Structure

```
ReguScan-Flask/
├── app.py                 # Main Flask application with file upload logic
├── requirements.txt       # Python dependencies (Flask, PyPDF2, python-docx)
├── templates/
│   ├── index.html        # Input form page with tabs and file upload
│   └── report.html       # Scan results page with export options
├── static/
│   └── style.css         # Styles including preloaders, progress bar, and print media queries
├── uploads/              # Temporary folder for file uploads (auto-created, not tracked)
├── .gitignore           # Git ignore rules (excludes .venv, __pycache__, uploads)
├── test_example.txt      # Sample test document
└── README.md            # Project documentation
```

## Testing

A sample test document (`test_example.txt`) is provided with example PII and compliance keywords. 

**Test with pasted text:**
- Copy the contents of `test_example.txt`
- Paste into the textarea
- Click "Scan Document"

**Test with file upload:**
- Click "Upload File" tab
- Drag and drop `test_example.txt` onto the upload area (or click to browse)
- Click "Scan Document"
- Watch the progress stages update in real-time

**Expected Results:**
- **PII Detection**: Varies by test document (9 different types supported)
- **Compliance Keywords**: 8 categories with 40+ total keywords
- **Risk Severity**: Critical/High/Medium classifications
- **Critical Alerts**: If dangerous combinations detected (SSN+CC, etc.)

## Technologies Used

- **Backend**: Python 3, Flask 3.0.0
- **File Processing**: 
  - PyPDF2 3.0.1 (PDF text extraction)
  - python-docx 1.1.0 (Word document extraction)
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Icons**: Font Awesome 6.4.0
- **Pattern Matching**: Python `re` module (regex)
- **Security**: Werkzeug secure_filename for file upload sanitization

## Security Notes

⚠️ **Important**: This tool is designed for scanning and educational purposes. It:
- Does NOT store any scanned data (in-memory processing only)
- Does NOT transmit data externally
- Should be used in a secure environment
- Is NOT a substitute for professional compliance auditing

## Browser Compatibility

- Chrome/Edge: ✅ Full support
- Firefox: ✅ Full support
- Safari: ✅ Full support
- Print/PDF: ✅ Optimized for all modern browsers

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Authors

**AMR M. ALSHAMEERI**
**OSAMAH HASAN ALREBAKI**

## Version History

- **v2.0** (Current) - Major compliance and security enhancement update:
  - 🎯 **Risk Severity System**: Critical/High/Medium classifications with intelligent pattern detection
  - 🚨 **Critical Risk Alerts**: Identity theft, financial fraud, and mass exposure warnings
  - 🔍 **Expanded PII Detection**: Added 4 new types (Passport, IBAN, Date of Birth, MAC Address) - total 9 types
  - 📋 **Enhanced Compliance**: Expanded from 3 to 8 categories with 40+ keywords
  - 🇪🇺 **GDPR Deep Dive**: 19 keywords including Controller, Processor, DPIA, Privacy by Design
  - 🇺🇸 **CCPA Enhancement**: 9 keywords including Authorized Agent, Notice at Collection
  - ⏱️ **Timeframe Detection**: "within 72 hours", "30 days" compliance deadlines
  - 🎨 **Visual Enhancements**: Color-coded severity rows, Font Awesome icons, animated alerts
- **v1.4** - Added progress bar with real-time scanning stages, implemented functional drag & drop, increased file size limit to 16 MB, added 413 error handler
- **v1.3** - Added file upload feature (.txt, .pdf, .docx) with drag and drop UI
- **v1.2** - Added professional print/PDF export functionality
- **v1.1** - Replaced emojis with Font Awesome icons, dynamic copyright
- **v1.0** - Initial release with PII detection and compliance scanning

## Support

For issues, questions, or suggestions, please open an issue on GitHub.

## Screenshots

### Main Interface
- **Dual Input Methods**: Switch between paste text or file upload with tab navigation
- **Drag & Drop**: Intuitive file upload with visual feedback
- **Page Load Preloader**: Animated brand introduction with floating logo

### Scanning Process
- **Progress Stages**: Real-time updates showing current operation
- **Progress Bar**: Visual indicator from 0% to 95%
- **Detailed Descriptions**: Clear explanation of each scanning stage

### Results Page
- **Summary Cards**: Quick overview of findings
- **PII Table**: Detailed breakdown with risk levels and line numbers
- **Compliance Grid**: Color-coded keywords by category
- **Print-Optimized**: Professional A4 layout with preserved colors

---

*Built with ❤️ A.M ^-^ & OSOS!*
