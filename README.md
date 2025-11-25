# ReguScan-Flask

**Automated GDPR/CCPA Compliance Scanning and Reporting Tool**

A simple yet powerful web application built with Flask that scans text documents for Personally Identifiable Information (PII) and compliance keywords related to GDPR and CCPA regulations.

## Features

### 🔍 PII Detection
- **Email Addresses** - High Risk
- **Credit Card Numbers** (VISA/Mastercard) - High Risk
- **US Social Security Numbers (SSN)** - High Risk
- **IPv4 Addresses** - Medium Risk
- **Phone Numbers** (US/International) - Medium Risk

### 📋 Compliance Keyword Scanning
Detects keywords across three categories:
- **Data Rights**: Right to be Forgotten, Right to Access, Right to Rectification, Right to Opt-Out, Data Portability, Data Subject Request (DSAR)
- **Policy/Consent**: Cookie Policy, Privacy Notice, Lawful Basis, Legitimate Interest, Explicit Consent, Data Processing Agreement (DPA)
- **Security/Transfers**: Data Breach Notification, Data Transfer, Third Parties, Security Measures, Encryption, Anonymization

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
- **Summary Cards**: Total PII risks and compliance coverage
- **PII Findings Table**: Detailed list with:
  - Type of sensitive data detected
  - Risk level (High/Medium)
  - Line number where found
  - Context snippet
- **Compliance Grid**: GDPR/CCPA keywords organized by category:
  - Data Rights
  - Policy/Consent  
  - Security/Transfers
- **Found vs Missing Keywords**: Clear indicators for compliance gaps

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
- 12 PII instances detected (emails, credit cards, SSNs, IPs, phone numbers)
- 20 compliance keywords found across all three categories

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
