"""
Ontario Service Gap Analysis - Data Check Script
Run this FIRST to see if you have data and what to do next.
"""

import os

def main():
    print("=" * 60)
    print("ONTARIO COMMUNITY SERVICE GAP ANALYSIS")
    print("=" * 60)
    
    print("\n📋 CURRENT PROJECT STATUS:")
    print("✅ Project structure created")
    print("✅ Python environment ready")
    print("❌ Waiting for real data")
    
    print("\n📁 Checking your data_raw/ folder...")
    
    # Check if data_raw exists
    if os.path.exists("../data_raw"):
        files = os.listdir("../data_raw")
        if files:
            print(f"Found {len(files)} file(s):")
            for file in files:
                print(f"  📄 {file}")
        else:
            print("data_raw/ folder is EMPTY")
    else:
        print("data_raw/ folder doesn't exist yet")
        os.makedirs("../data_raw", exist_ok=True)
        print("Created data_raw/ folder for you!")
    
    print("\n" + "=" * 60)
    print("🎯 IMMEDIATE NEXT STEP:")
    print("=" * 60)
    print("\n1. Go to Statistics Canada:")
    print("   https://www12.statcan.gc.ca/census-recensement/index-eng.cfm")
    print("\n2. Search for: 'Population and dwelling counts'")
    print("\n3. Filter for: Ontario, Forward Sortation Area (FSA)")
    print("\n4. Download as CSV")
    print("\n5. Save file in: data_raw/census_data.csv")
    print("\n6. Run this script again to check")
    
    print("\n" + "=" * 60)
    print("Need help? Check docs/ folder for more guidance.")
    print("=" * 60)

if __name__ == "__main__":
    main()
