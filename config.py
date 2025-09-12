# Configuration file for Indian Mutual Fund Recovery Screener

# Screening Criteria
SCREENING_CONFIG = {
    "min_negative_1y_return": 0,  # Only funds with 1Y returns below this threshold
    "min_aum_crores": 1000,       # Minimum AUM in crores for liquidity
    "max_expense_ratio": 2.0,     # Maximum expense ratio threshold
    "min_track_record_years": 3,  # Minimum years of operation
}

# Momentum Scoring Weights
SCORING_WEIGHTS = {
    "beaten_down_factor": 30,     # Weight for how beaten down the fund is
    "historical_performance": 25, # Weight for long-term performance
    "current_positioning": 25,    # Weight for current vs 52-week range
    "fund_quality": 20,          # Weight for AUM and expense ratio
}

# Recommendation Thresholds
RECOMMENDATION_THRESHOLDS = {
    "strong_buy": 80,    # Score >= 80
    "buy": 65,           # Score 65-79
    "hold": 50,          # Score 50-64
    "avoid": 0,          # Score < 50
}

# Market Data Sources (for future API integration)
DATA_SOURCES = {
    "mutual_funds": {
        "primary": "AMFI",
        "backup": "MorningStar",
        "api_endpoint": "https://www.amfiindia.com/spages/NAVAll.txt"
    },
    "market_data": {
        "nifty": "NSE",
        "api_endpoint": "https://www.nseindia.com/api/equity-stockIndices?index=NIFTY%2050"
    },
    "news": {
        "primary": "Economic Times",
        "backup": "Reuters"
    }
}

# HTML Report Styling
REPORT_CONFIG = {
    "title": "Indian Mutual Fund Recovery Screener",
    "subtitle": "Identifying Beaten-Down Funds with Comeback Potential", 
    "theme_colors": {
        "primary": "#1e3c72",
        "secondary": "#2a5298",
        "success": "#28a745",
        "danger": "#dc3545",
        "warning": "#ffc107"
    }
}
