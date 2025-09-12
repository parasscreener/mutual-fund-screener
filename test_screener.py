#!/usr/bin/env python3
"""
Test script to run the mutual fund screener locally
This helps test the functionality before deploying to GitHub
"""

import sys
import os
from datetime import datetime

def test_screener():
    """Test the mutual fund screener functionality"""
    print("🧪 Testing Indian Mutual Fund Recovery Screener")
    print("=" * 60)

    try:
        # Import the main screener class
        from mutual_fund_screener import IndianMutualFundScreener

        # Create screener instance
        screener = IndianMutualFundScreener()

        print("✅ Screener class imported successfully")

        # Run the analysis
        results = screener.run_analysis()

        # Display results summary
        print("\n📊 Test Results Summary:")
        print(f"- Found {len(results)} beaten-down funds")
        print(f"- Analysis completed at: {datetime.now()}")

        # Check if files were created
        files_to_check = ['index.html', 'fund_analysis_data.json']
        for file in files_to_check:
            if os.path.exists(file):
                print(f"✅ {file} created successfully")
                file_size = os.path.getsize(file)
                print(f"   File size: {file_size:,} bytes")
            else:
                print(f"❌ {file} not found")

        # Display top recommendations
        if results:
            print("\n🎯 Top 3 Recommendations:")
            for i, fund in enumerate(results[:3], 1):
                print(f"{i}. {fund['fund_name']}")
                print(f"   Score: {fund['momentum_score']}/100")
                print(f"   Recommendation: {fund['recommendation']}")
                print(f"   1Y Return: {fund['1y_return']:+.1f}%")
                print()

        print("✅ Test completed successfully!")

        # Open the generated HTML file
        try:
            import webbrowser
            webbrowser.open('index.html')
            print("🌐 Opening generated report in browser...")
        except:
            print("💡 Manually open 'index.html' to view the report")

    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("Make sure all dependencies are installed:")
        print("pip install pandas numpy requests yfinance beautifulsoup4")

    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False

    return True

def check_dependencies():
    """Check if all required dependencies are installed"""
    print("🔍 Checking dependencies...")

    required_packages = [
        'pandas',
        'numpy', 
        'requests',
        'yfinance',
        'beautifulsoup4'
    ]

    missing_packages = []

    for package in required_packages:
        try:
            __import__(package)
            print(f"✅ {package}")
        except ImportError:
            print(f"❌ {package} (missing)")
            missing_packages.append(package)

    if missing_packages:
        print("\n📦 Install missing packages with:")
        print(f"pip install {' '.join(missing_packages)}")
        return False

    print("✅ All dependencies are installed!")
    return True

if __name__ == "__main__":
    print("🚀 Indian Mutual Fund Recovery Screener - Test Suite")
    print("=" * 60)

    # Check dependencies first
    if not check_dependencies():
        sys.exit(1)

    # Run the test
    if test_screener():
        print("\n🎉 All tests passed! Ready for GitHub deployment.")
    else:
        print("\n⚠️  Some tests failed. Check the errors above.")
        sys.exit(1)
