import pdfplumber
import re
import json

def get_data():
    pdf_path = '/Users/mahendrakolhe/Downloads/3-06-26 Tenterfield REPORT NM.pdf'
    pdf = pdfplumber.open(pdf_path)

    result = []
    current_client_name = None
    current_site_name = None
    current_location_name = None

    for page in pdf.pages:
        tables = page.extract_tables()
        if not tables:
            continue

        for table in tables:
            for row in table:
                line = [cell.strip() if cell else '' for cell in row]
                if not any(line):
                    continue

                # 1. Detect new client
                client_match = next((l for l in line if l.startswith("Client:")), None)
                if client_match:
                    current_client_name = client_match.split("Client:")[1].strip()
                    # Create/find client
                    client_entry = next((c for c in result if c["client"] == current_client_name), None)
                    if not client_entry:
                        client_entry = {"client": current_client_name, "sites": []}
                        result.append(client_entry)
                    continue

                # 2. Detect new site
                site_match = next((l for l in line if l.startswith("Site:")), None)
                if site_match:
                    current_site_name = site_match.split("Site:")[1].strip()
                    # Create/find site in current client
                    site_entry = next((s for s in client_entry["sites"] if s["site"] == current_site_name), None)
                    if not site_entry:
                        site_entry = {"site": current_site_name, "locations": []}
                        client_entry["sites"].append(site_entry)
                    continue

                # 3. Detect new location
                location_match = next((l for l in line if l.startswith("Location:")), None)
                if location_match:
                    current_location_name = location_match.split("Location:")[1].strip()
                    # Create/find location in current site
                    location_entry = next((l for l in site_entry["locations"] if l["location"] == current_location_name), None)
                    if not location_entry:
                        location_entry = {"location": current_location_name, "assets": []}
                        site_entry["locations"].append(location_entry)
                    continue

                # 4. Skip header row
                if any("Asset ID" in l for l in line):
                    continue

                # 5. Parse asset line (if it starts with numeric Asset ID)
                if re.match(r'^\d{6,8}$', line[0]):
                    # Pad row if needed
                    while len(line) < 8:
                        line.append("")

                    asset = {
                        "Asset ID": line[0],
                        "Description": line[1],
                        "User": line[2],
                        "Test Instrument": line[3],
                        "Date": line[4],
                        "Retest Period": line[5],
                        "Next Test": line[6],
                        "Result": line[7]
                    }

                    # Ensure location_entry is available
                    if current_client_name and current_site_name and current_location_name:
                        # Refresh parent references (in case structure changed mid-page)
                        client_entry = next((c for c in result if c["client"] == current_client_name), None)
                        site_entry = next((s for s in client_entry["sites"] if s["site"] == current_site_name), None)
                        location_entry = next((l for l in site_entry["locations"] if l["location"] == current_location_name), None)
                        location_entry["assets"].append(asset)

    return result


# ✅ Extract and write output
data = get_data()
with open("output_hierarchical.json", "w") as f:
    json.dump(data, f, indent=2)
