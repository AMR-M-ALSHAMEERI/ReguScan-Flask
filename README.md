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

### ✨ User Interface
- Clean, modern responsive design
- Font Awesome icons throughout
- Color-coded risk levels (High = Red, Medium = Yellow)
- Dynamic copyright year
- Professional print/PDF export functionality
- Real-time scanning with loading indicators

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

1. **Enter or paste text** in the input form on the homepage
2. **Click "Scan Document"** to analyze the content
3. **Review the results** showing:
   - Total PII risks detected with line numbers and context
   - Risk levels for each finding
   - Compliance keyword status by category
4. **Print or export** to PDF using the browser's print function for professional reports

## Project Structure

```
ReguScan-Flask/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── templates/
│   ├── index.html        # Input form page
│   └── report.html       # Scan results page
├── static/
│   └── style.css         # Styles including print media queries
├── test_example.txt      # Sample test document
└── README.md            # Project documentation
```

## Testing

A sample test document (`test_example.txt`) is provided with example PII and compliance keywords. You can copy its contents into the scanner to see how it works.

## Technologies Used

- **Backend**: Python 3, Flask 3.0.0
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Icons**: Font Awesome 6.4.0
- **Pattern Matching**: Python `re` module (regex)

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

## Author

**AMR M. ALSHAMEERI**

## Version History

- **v1.2** - Added professional print/PDF export functionality
- **v1.1** - Replaced emojis with Font Awesome icons, dynamic copyright
- **v1.0** - Initial release with PII detection and compliance scanning

## Support

For issues, questions, or suggestions, please open an issue on GitHub.

---

*Built with ❤️ for data privacy compliance*