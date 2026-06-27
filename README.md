# PermitFlow AI – Automated Building Permit Compliance Engine

PermitFlow AI is a lightweight, cloud-ready data extraction and automated auditing pipeline designed for municipal planning authorities. The system automates the processing of unstructured building permit application documents, extracts key operational variables, and dynamically flags applications for regulatory compliance—eliminating manual data entry bottlenecks and compliance errors.

## 🚀 Core Features
* **Zero-Cost Automated Extraction:** Extracts structural, geographical, and financial data fields from text-layer PDFs with 100% precision using open-source tools.
* **Automated Risk Mitigation:** Runs real-time compliance checks to isolate high-risk applications (e.g., missing mandatory tax documentation) before administrative approval.
* **Analytics-Ready Pipelines:** Aggregates unstructured data inputs into a clean, normalized relational database format (`.csv`).

## 🛠️ Tech Stack & Dependencies
* **Core Language:** Python 3.x
* **Libraries:** `pdfplumber` (PDF text extraction), `pandas` (data manipulation & audit rules), `glob` (file ingestion management)
* **Environment:** Google Colab / Jupyter Notebooks

## 📁 Repository Structure
```text
├── Data/
│ ├── Permit_1.pdf to Permit_15.pdf # Source application documents
│ └── permit_mvp_data.csv # Initial mock geographic data
├── Scripts/
│ └── permitflow_parser.py # Main data extraction & audit engine
├── Output/
│ └── permitflow_final_database.csv # Final compiled compliance matrix
└── README.md # Documentation
