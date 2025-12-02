"""
Ontario Community Service Gap Analysis - Starter Script
This script helps analyze service gaps across Ontario communities.
"""

import pandas as pd
import os

def check_data_files():
    """Check if expected data files exist"""
    print("🔍 Checking for data files...")
    
    expected_files = [
        '../data_raw/census_data.csv',
        '../data_raw/services_data.csv', 
        '../data_raw/postal_codes.csv'
    ]
    
    for file in expected_files:
        if os.path.exists(file):
            print(f"   ✅ Found: {file}")
        else:
            print(f"   ⚠️  Missing: {file}")
    
    print("\n📁 If files are missing, download sample data:")
    print("   1. Statistics Canada census data")
    print("   2. 211 Ontario service directory")
    print("   3. Postal code boundaries")

def create_sample_data():
    """Create sample data if no real data exists yet"""
    print("\n📝 Creating sample data structure...")
    
    # Sample demographics data
    sample_demo = pd.DataFrame({
        'postal_code': ['M5V', 'K1A', 'L5B', 'P0L', 'N0L'],
        'region': ['Toronto-Downtown', 'Ottawa-Central', 'Mississauga', 'Northern-Ontario', 'Southwest-Rural'],
        'population': [15000, 12000, 18000, 5000, 3000],
        'seniors': [3000, 2400, 3600, 1500, 900],
        'low_income': [4500, 3000, 5400, 2000, 1200],
        'newcomers': [2000, 1500, 1800, 200, 100]
    })
    
    # Sample services data
    sample_services = pd.DataFrame({
        'service_id': [1, 2, 3, 4, 5],
        'service_name': ['Senior Center A', 'Food Bank B', 'Health Clinic C', 'Newcomer Center D', 'Community Hub E'],
        'service_type': ['senior_services', 'food_bank', 'health', 'newcomer_services', 'general'],
        'postal_code': ['M5V', 'K1A', 'L5B', 'M5V', 'N0L'],
        'region': ['Toronto-Downtown', 'Ottawa-Central', 'Mississauga', 'Toronto-Downtown', 'Southwest-Rural']
    })
    
    # Save sample data
    os.makedirs('../data_clean', exist_ok=True)
    sample_demo.to_csv('../data_clean/sample_demographics.csv', index=False)
    sample_services.to_csv('../data_clean/sample_services.csv', index=False)
    
    print("   ✅ Created sample data in 'data_clean/' folder")
    print("   📊 Sample files: sample_demographics.csv, sample_services.csv")

def calculate_basic_gaps():
    """Calculate simple service gap metrics"""
    print("\n📈 Calculating basic service gaps...")
    
    try:
        # Try to load the sample data
        demo = pd.read_csv('../data_clean/sample_demographics.csv')
        services = pd.read_csv('../data_clean/sample_services.csv')
        
        # Count services by region
        service_counts = services.groupby('region')['service_id'].count().reset_index()
        service_counts.columns = ['region', 'service_count']
        
        # Merge with demographics
        merged = pd.merge(demo, service_counts, on='region', how='left')
        merged['service_count'] = merged['service_count'].fillna(0)
        
        # Calculate seniors per service
        merged['seniors_per_service'] = merged['seniors'] / merged['service_count'].replace(0, 1)
        
        # Identify gaps
        merged['gap_status'] = merged.apply(
            lambda row: 'HIGH GAP' if (row['seniors'] > 2000 and row['service_count'] < 2) else 'OK',
            axis=1
        )
        
        # Save results
        os.makedirs('../outputs', exist_ok=True)
        merged.to_csv('../outputs/gap_analysis_results.csv', index=False)
        
        print("   ✅ Gap analysis complete!")
        print("   📄 Results saved to: outputs/gap_analysis_results.csv")
        
        # Show summary
        print("\n📋 Summary of gaps found:")
        high_gaps = merged[merged['gap_status'] == 'HIGH GAP']
        if len(high_gaps) > 0:
            for _, row in high_gaps.iterrows():
                print(f"   ⚠️  {row['region']}: {row['seniors']} seniors, only {int(row['service_count'])} services")
        else:
            print("   ✅ No high gaps found in sample data")
            
    except Exception as e:
        print(f"   ⚠️  Could not run full analysis: {e}")
        print("   ℹ️  Make sure to run with real data for complete analysis")

def main():
    """Main function to run the analysis"""
    print("=" * 60)
    print("ONTARIO COMMUNITY SERVICE GAP ANALYSIS")
    print("=" * 60)
    
    # Step 1: Check for data
    check_data_files()
    
    # Step 2: Create sample data if needed
    create_sample_data()
    
    # Step 3: Run analysis
    calculate_basic_gaps()
    
    print("\n" + "=" * 60)
    print("NEXT STEPS:")
    print("1. Add your real data to 'data_raw/' folder")
    print("2. Modify this script to use your actual data files")
    print("3. Run: python python/scripts/simple_analysis.py")
    print("=" * 60)

if __name__ == "__main__":
    main()
