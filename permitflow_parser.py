import pdfplumber
import pandas as pd
import glob

# Initialize the master storage list
extracted_records = []

# Gather all uploaded permit PDFs from your sidebar
pdf_files = sorted(glob.glob("Permit_*.pdf"))
print(f"🔄 Scanning folder... Found {len(pdf_files)} PDFs to process.\n")

for file_path in pdf_files:
    with pdfplumber.open(file_path) as pdf:
        # Extract all text on page 1
        raw_text = pdf.pages[0].extract_text()
        
        # Start a blank data card for this specific file
        record = {"File Name": file_path.split("/")[-1]}
        
        # Break the text down line-by-line to isolate fields
        for line in raw_text.split("\n"):
            if "Applicant Name:" in line:
                record["Applicant Name"] = line.split("Applicant Name:")[1].strip()
            elif "Tax Identification Number (TIN):" in line:
                tin_raw = line.split("Tax Identification Number (TIN):")[1].strip()
                # Catch our deliberate blank testing entries
                record["TIN"] = "MISSING" if "[BLANK" in tin_raw else tin_raw
            elif "Proposed Site Address:" in line:
                record["Site Address"] = line.split("Proposed Site Address:")[1].strip()
            elif "City/Town:" in line:
                record["Town"] = line.split("City/Town:")[1].strip()
            elif "State:" in line:
                record["State"] = line.split("State:")[1].strip()
            elif "Proposed Structure Type:" in line:
                record["Structure Type"] = line.split("Proposed Structure Type:")[1].strip()
            elif "Estimated Project Valuation:" in line:
                record["Valuation"] = line.split("Estimated Project Valuation:")[1].strip()
        
        # Add this completed card to our database
        extracted_records.append(record)

# Convert all records into a beautiful data table
final_df = pd.DataFrame(extracted_records)

# Build a compliance feature: Flag records with a missing TIN
final_df["Compliance Flag"] = final_df["TIN"].apply(
    lambda x: "🚨 FLAGGED: Missing TIN" if x == "MISSING" else "✅ Compliant"
)

# Export the master output completely for free
final_df.to_csv("permitflow_final_database.csv", index=False)
print("🏆 Victory! Your engine parsed the documents successfully.")
final_df.head()
