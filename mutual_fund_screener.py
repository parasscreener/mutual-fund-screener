#!/usr/bin/env python3
"""
Indian Mutual Fund Screener & Analyzer
Screens beaten-down mutual funds with momentum recovery potential
Author: AI Financial Analyst
"""

import pandas as pd
import numpy as np
import requests
from datetime import datetime, timedelta
import json
import yfinance as yf
import warnings
warnings.filterwarnings('ignore')

class IndianMutualFundScreener:
    def __init__(self):
        self.funds_data = []
        self.market_data = {}
        self.news_data = []
        self.nifty_valuation = {}

    def fetch_mutual_fund_data(self):
        """Fetch mutual fund data from various sources"""
        print("📊 Fetching mutual fund data...")

        # Sample fund data - in real implementation, this would fetch from AMFI/MorningStar APIs
        sample_funds = [
            {
                'fund_name': 'HDFC Mid Cap Opportunities Fund',
                'fund_code': 'HDFC_MID_CAP',
                'category': 'Mid Cap',
                'aum_cr': 83104,
                '1y_return': -2.5,
                '3y_return': 15.2,
                '5y_return': 18.3,
                '10y_return': 16.8,
                'current_nav': 142.5,
                '52w_high': 165.2,
                '52w_low': 128.4,
                'expense_ratio': 1.25,
                'fund_manager': 'Chirag Setalvad'
            },
            {
                'fund_name': 'SBI Small Cap Fund',
                'fund_code': 'SBI_SMALL_CAP',
                'category': 'Small Cap',
                'aum_cr': 31227,
                '1y_return': -8.2,
                '3y_return': 12.8,
                '5y_return': 20.1,
                '10y_return': 18.5,
                'current_nav': 95.6,
                '52w_high': 118.9,
                '52w_low': 89.3,
                'expense_ratio': 1.45,
                'fund_manager': 'R Srinivasan'
            },
            {
                'fund_name': 'Axis Small Cap Fund',
                'fund_code': 'AXIS_SMALL_CAP',
                'category': 'Small Cap',
                'aum_cr': 25568,
                '1y_return': -5.8,
                '3y_return': 16.2,
                '5y_return': 22.8,
                '10y_return': 17.9,
                'current_nav': 88.4,
                '52w_high': 102.7,
                '52w_low': 82.1,
                'expense_ratio': 1.35,
                'fund_manager': 'Shreyash Devalkar'
            },
            {
                'fund_name': 'Franklin India Smaller Cos Fund',
                'fund_code': 'FRANKLIN_SMALL_CAP',
                'category': 'Small Cap',
                'aum_cr': 8245,
                '1y_return': -12.3,
                '3y_return': 8.9,
                '5y_return': 15.6,
                '10y_return': 14.2,
                'current_nav': 76.8,
                '52w_high': 94.5,
                '52w_low': 72.1,
                'expense_ratio': 1.55,
                'fund_manager': 'Anand Radhakrishnan'
            },
            {
                'fund_name': 'Nippon India Small Cap Fund',
                'fund_code': 'NIPPON_SMALL_CAP',
                'category': 'Small Cap',
                'aum_cr': 57009,
                '1y_return': -3.2,
                '3y_return': 18.5,
                '5y_return': 24.1,
                '10y_return': 20.0,
                'current_nav': 156.3,
                '52w_high': 178.9,
                '52w_low': 145.2,
                'expense_ratio': 1.28,
                'fund_manager': 'Samir Rachh'
            },
            {
                'fund_name': 'Motilal Oswal Midcap Fund',
                'fund_code': 'MOTILAL_MIDCAP',
                'category': 'Mid Cap',
                'aum_cr': 33608,
                '1y_return': -9.8,
                '3y_return': 14.2,
                '5y_return': 19.8,
                '10y_return': 17.4,
                'current_nav': 98.7,
                '52w_high': 124.5,
                '52w_low': 92.3,
                'expense_ratio': 1.42,
                'fund_manager': 'Rakesh Singh'
            },
            {
                'fund_name': 'Kotak Small Cap Fund',
                'fund_code': 'KOTAK_SMALL_CAP',
                'category': 'Small Cap',
                'aum_cr': 18456,
                '1y_return': -7.1,
                '3y_return': 11.8,
                '5y_return': 17.9,
                '10y_return': 15.8,
                'current_nav': 145.8,
                '52w_high': 167.2,
                '52w_low': 132.9,
                'expense_ratio': 1.38,
                'fund_manager': 'Pankaj Tibrewal'
            },
            {
                'fund_name': 'Tata Small Cap Fund',
                'fund_code': 'TATA_SMALL_CAP',
                'category': 'Small Cap',
                'aum_cr': 12348,
                '1y_return': -11.5,
                '3y_return': 9.2,
                '5y_return': 16.2,
                '10y_return': 13.8,
                'current_nav': 89.3,
                '52w_high': 108.7,
                '52w_low': 84.1,
                'expense_ratio': 1.48,
                'fund_manager': 'Meeta Shetty'
            }
        ]

        self.funds_data = sample_funds
        return sample_funds

    def fetch_nifty_valuation_data(self):
        """Fetch current NIFTY valuation metrics"""
        print("📈 Fetching NIFTY valuation data...")

        # Sample NIFTY data - in real implementation, this would fetch from NSE APIs
        nifty_data = {
            'nifty_50_level': 25125,
            'nifty_50_pe': 22.0,
            'nifty_50_pb': 3.34,
            'nifty_500_level': 23182,
            'nifty_500_pe': 24.2,
            'nifty_500_pb': 3.58,
            'market_cap_to_gdp': 120.0,
            'historical_avg_pe': 19.6,
            'current_vs_historical': 'Overvalued',
            'volatility_index': 15.8,
            'fii_outflows_ytd': -15000,  # in crores
            'dii_inflows_ytd': 125000   # in crores
        }

        self.nifty_valuation = nifty_data
        return nifty_data

    def fetch_market_news(self):
        """Fetch current market news and scenarios"""
        print("📰 Fetching market news...")

        # Sample news data - in real implementation, this would fetch from news APIs
        news_data = [
            {
                'headline': 'Indian Markets Navigate US Trade Tensions',
                'summary': 'Markets remain resilient despite trade uncertainties. GST reforms expected to boost consumption.',
                'impact': 'Mixed',
                'date': '2025-09-12'
            },
            {
                'headline': 'Fed Rate Cut Expected This Month',
                'summary': 'US Fed likely to cut rates by 25bps, potentially boosting FII inflows to India.',
                'impact': 'Positive',
                'date': '2025-09-12'
            },
            {
                'headline': 'India GDP Growth Remains Strong at 7.8%',
                'summary': 'Q1 FY26 GDP growth beats estimates, supporting long-term investment thesis.',
                'impact': 'Positive',
                'date': '2025-09-10'
            }
        ]

        self.news_data = news_data
        return news_data

    def calculate_momentum_indicators(self, fund_data):
        """Calculate technical momentum indicators for funds"""

        # Calculate drawdown from 52-week high
        current_nav = fund_data['current_nav']
        high_52w = fund_data['52w_high']
        low_52w = fund_data['52w_low']

        drawdown_from_high = ((high_52w - current_nav) / high_52w) * 100
        recovery_potential = ((current_nav - low_52w) / (high_52w - low_52w)) * 100

        # RSI-like momentum score based on recent performance vs long-term
        short_term_return = fund_data['1y_return']
        long_term_return = fund_data['5y_return']

        momentum_score = 0

        # Beaten down criteria (negative or low returns)
        if short_term_return < -5:
            momentum_score += 30  # Significantly beaten down
        elif short_term_return < 0:
            momentum_score += 20  # Moderately beaten down

        # Recovery potential based on historical performance
        if long_term_return > 15:
            momentum_score += 25  # Strong historical performance
        elif long_term_return > 10:
            momentum_score += 15  # Good historical performance

        # Current positioning vs 52-week range
        if recovery_potential > 70:
            momentum_score += 10  # Near highs (less attractive)
        elif recovery_potential < 30:
            momentum_score += 25  # Near lows (more attractive)
        else:
            momentum_score += 15  # Mid-range

        # Fund quality indicators
        if fund_data['aum_cr'] > 10000:  # Large fund
            momentum_score += 10
        if fund_data['expense_ratio'] < 1.5:  # Reasonable expense ratio
            momentum_score += 10

        return {
            'momentum_score': min(momentum_score, 100),
            'drawdown_from_high': round(drawdown_from_high, 2),
            'recovery_potential_pct': round(recovery_potential, 2),
            'beaten_down_level': 'High' if short_term_return < -10 else 'Medium' if short_term_return < -5 else 'Low'
        }

    def screen_beaten_down_funds(self):
        """Screen and rank beaten-down funds with recovery potential"""
        print("🔍 Screening beaten-down funds...")

        screened_funds = []

        for fund in self.funds_data:
            # Calculate momentum indicators
            momentum_data = self.calculate_momentum_indicators(fund)

            # Combine fund data with momentum analysis
            fund_analysis = {
                **fund,
                **momentum_data,
                'recommendation': self.get_recommendation(fund, momentum_data)
            }

            # Filter for beaten-down funds (negative 1-year returns)
            if fund['1y_return'] < 0:
                screened_funds.append(fund_analysis)

        # Sort by momentum score (highest first)
        screened_funds.sort(key=lambda x: x['momentum_score'], reverse=True)

        return screened_funds

    def get_recommendation(self, fund_data, momentum_data):
        """Generate investment recommendation"""
        momentum_score = momentum_data['momentum_score']

        if momentum_score >= 80:
            return 'Strong Buy'
        elif momentum_score >= 65:
            return 'Buy'
        elif momentum_score >= 50:
            return 'Hold'
        else:
            return 'Avoid'

    def generate_html_report(self, screened_funds):
        """Generate dynamic HTML report"""
        print("📄 Generating HTML report...")

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S IST")

        # Create HTML with proper escaping
        html_content = self.create_html_template(current_time, screened_funds)

        return html_content

    def create_html_template(self, current_time, screened_funds):
        """Create the HTML template"""

        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Indian Mutual Fund Recovery Screener</title>
    <style>
        body {{
            font-family: 'Arial', sans-serif;
            margin: 0;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: #333;
        }}
        .container {{
            max-width: 1400px;
            margin: 0 auto;
            background: white;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            overflow: hidden;
        }}
        .header {{
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
            color: white;
            padding: 30px;
            text-align: center;
        }}
        .header h1 {{
            margin: 0;
            font-size: 2.5em;
            margin-bottom: 10px;
        }}
        .timestamp {{
            font-size: 0.9em;
            opacity: 0.8;
        }}
        .market-overview {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            padding: 30px;
            background: #f8f9fa;
        }}
        .metric-card {{
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            text-align: center;
        }}
        .metric-value {{
            font-size: 1.8em;
            font-weight: bold;
            color: #2a5298;
        }}
        .metric-label {{
            font-size: 0.9em;
            color: #666;
            margin-top: 5px;
        }}
        .funds-table {{
            padding: 30px;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
            background: white;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }}
        th {{
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
            color: white;
            padding: 15px;
            text-align: left;
            font-weight: 600;
        }}
        td {{
            padding: 12px 15px;
            border-bottom: 1px solid #eee;
        }}
        tr:hover {{
            background: #f8f9fa;
        }}
        .recommendation {{
            padding: 8px 12px;
            border-radius: 20px;
            font-weight: bold;
            color: white;
            text-align: center;
        }}
        .strong-buy {{ background: #28a745; }}
        .buy {{ background: #007bff; }}
        .hold {{ background: #ffc107; color: #333; }}
        .avoid {{ background: #dc3545; }}
        .beaten-down-high {{ color: #dc3545; font-weight: bold; }}
        .beaten-down-medium {{ color: #fd7e14; font-weight: bold; }}
        .beaten-down-low {{ color: #20c997; font-weight: bold; }}
        .news-section {{
            padding: 30px;
            background: #f8f9fa;
        }}
        .news-item {{
            background: white;
            margin: 15px 0;
            padding: 20px;
            border-radius: 10px;
            border-left: 5px solid #2a5298;
        }}
        .news-headline {{
            font-weight: bold;
            margin-bottom: 10px;
            color: #1e3c72;
        }}
        .footer {{
            text-align: center;
            padding: 20px;
            background: #1e3c72;
            color: white;
            font-size: 0.9em;
        }}
        .disclaimer {{
            margin-top: 10px;
            font-size: 0.8em;
            opacity: 0.8;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🚀 Indian Mutual Fund Recovery Screener</h1>
            <p>Identifying Beaten-Down Funds with Comeback Potential</p>
            <div class="timestamp">Last Updated: {current_time}</div>
        </div>

        <div class="market-overview">
            <div class="metric-card">
                <div class="metric-value">{self.nifty_valuation['nifty_50_level']:,}</div>
                <div class="metric-label">NIFTY 50 Level</div>
            </div>
            <div class="metric-card">
                <div class="metric-value">{self.nifty_valuation['nifty_50_pe']}</div>
                <div class="metric-label">NIFTY 50 P/E</div>
            </div>
            <div class="metric-card">
                <div class="metric-value">{self.nifty_valuation['market_cap_to_gdp']}%</div>
                <div class="metric-label">Market Cap/GDP</div>
            </div>
            <div class="metric-card">
                <div class="metric-value">{self.nifty_valuation['current_vs_historical']}</div>
                <div class="metric-label">Market Valuation</div>
            </div>
        </div>

        <div class="funds-table">
            <h2>🎯 Top Beaten-Down Funds with Recovery Potential</h2>
            <table>
                <thead>
                    <tr>
                        <th>Fund Name</th>
                        <th>Category</th>
                        <th>AUM (₹Cr)</th>
                        <th>1Y Return</th>
                        <th>3Y Return</th>
                        <th>5Y Return</th>
                        <th>10Y Return</th>
                        <th>Momentum Score</th>
                        <th>Beaten Down Level</th>
                        <th>Recovery Potential</th>
                        <th>Recommendation</th>
                    </tr>
                </thead>
                <tbody>"""

        # Add fund rows
        for fund in screened_funds:
            recommendation_class = fund['recommendation'].lower().replace(' ', '-')
            beaten_down_class = f"beaten-down-{fund['beaten_down_level'].lower()}"

            html += f"""
                    <tr>
                        <td><strong>{fund['fund_name']}</strong><br>
                            <small>Manager: {fund['fund_manager']}</small></td>
                        <td>{fund['category']}</td>
                        <td>₹{fund['aum_cr']:,}</td>
                        <td style="color: red; font-weight: bold;">{fund['1y_return']:+.1f}%</td>
                        <td>{fund['3y_return']:.1f}%</td>
                        <td>{fund['5y_return']:.1f}%</td>
                        <td>{fund['10y_return']:.1f}%</td>
                        <td><strong>{fund['momentum_score']}/100</strong></td>
                        <td class="{beaten_down_class}">{fund['beaten_down_level']}</td>
                        <td>{fund['recovery_potential_pct']:.1f}%</td>
                        <td><span class="recommendation {recommendation_class}">{fund['recommendation']}</span></td>
                    </tr>"""

        html += """
                </tbody>
            </table>
        </div>

        <div class="news-section">
            <h2>📰 Market News & Scenarios</h2>"""

        # Add news items
        for news in self.news_data:
            html += f"""
            <div class="news-item">
                <div class="news-headline">{news['headline']}</div>
                <div>{news['summary']}</div>
                <small style="color: #666;">Impact: {news['impact']} | Date: {news['date']}</small>
            </div>"""

        html += """
        </div>

        <div class="footer">
            <p><strong>Indian Mutual Fund Recovery Screener</strong></p>
            <p>Veteran Analyst's Algorithm for Identifying Comeback Opportunities</p>
            <div class="disclaimer">
                Disclaimer: This is for educational purposes only. Past performance does not guarantee future results. 
                Please consult with a financial advisor before making investment decisions.
            </div>
        </div>
    </div>
</body>
</html>"""

        return html

    def run_analysis(self):
        """Run complete analysis and generate report"""
        print("🚀 Starting Indian Mutual Fund Recovery Analysis...")
        print("=" * 60)

        # Fetch all data
        self.fetch_mutual_fund_data()
        self.fetch_nifty_valuation_data()
        self.fetch_market_news()

        # Screen funds
        screened_funds = self.screen_beaten_down_funds()

        # Generate report
        html_report = self.generate_html_report(screened_funds)

        # Save report
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(html_report)

        # Save data as JSON for reference
        analysis_data = {
            'screened_funds': screened_funds,
            'nifty_valuation': self.nifty_valuation,
            'news_data': self.news_data,
            'analysis_timestamp': datetime.now().isoformat()
        }

        with open('fund_analysis_data.json', 'w', encoding='utf-8') as f:
            json.dump(analysis_data, f, indent=2)

        print("✅ Analysis Complete!")
        print(f"📊 Screened {len(screened_funds)} beaten-down funds")
        print("📄 Report generated: index.html")
        print("📊 Data saved: fund_analysis_data.json")

        return screened_funds

if __name__ == "__main__":
    screener = IndianMutualFundScreener()
    screener.run_analysis()
