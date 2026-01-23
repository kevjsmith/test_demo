import pandas as pd
import sys

# Define risky ports
RISKY_PORTS = [22, 3389, 445, 80, 135, 5985, 5900, 5938]  # SSH, RDP, SMB, HTTP, RPC, WinRM, VNC, TeamViewer

def load_csv(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"Error loading file: {e}")
        sys.exit(1)

def detect_lateral_movement(df):
    lateral_risks = df[
        df['source_environment'] != df['destination_environment']
    ]
    return lateral_risks

def detect_risky_ports(df, risky_ports):
    risky_hits = df[
        df['dest_port'].isin(risky_ports)
    ]
    return risky_hits

def analyze_policies(file_path):
    print(f"Loading file: {file_path}")
    df = load_csv(file_path)

    print("Detecting lateral movement across environments...")
    lateral_risks = detect_lateral_movement(df)

    print("Detecting access on risky service ports...")
    risky_ports = detect_risky_ports(df, RISKY_PORTS)

    print("Summary Report:")
    print(f"Total Flows Analyzed: {len(df)}")
    print(f"Lateral Movement Risks Detected: {len(lateral_risks)}")
    print(f"Risky Port Hits Detected: {len(risky_ports)}")

    lateral_risks.to_csv("lateral_movement_risks.csv", index=False)
    risky_ports.to_csv("risky_port_hits.csv", index=False)

    print("\nOutput files generated:")
    print(" - lateral_movement_risks.csv")
    print(" - risky_port_hits.csv")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 analyzer.py <input_csv_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    analyze_policies(input_file)
