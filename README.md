# 🚀 Indian Mutual Fund Recovery Screener

A comprehensive GitHub Pages deployment that automatically screens beaten-down Indian mutual funds with strong recovery potential. This project combines veteran mutual fund analysis expertise with automated web deployment.

## 🎯 Features

### 📊 Fund Analysis
- **Beaten-Down Screening**: Identifies funds with negative 1-year returns
- **Multi-Period Returns**: Analyzes 1, 3, 5, and 10-year performance
- **Momentum Indicators**: Custom algorithm for recovery potential assessment
- **Fund Quality Metrics**: AUM, expense ratios, fund manager details

### 📈 Market Context
- **NIFTY Valuations**: Current PE, PB ratios vs historical averages
- **Market Sentiment**: Market cap to GDP ratio analysis
- **FII/DII Flows**: Foreign and domestic institutional investor trends

### 📰 News Integration
- **Current Market News**: Latest Indian and global market developments
- **Impact Assessment**: How news affects mutual fund outlook
- **Scenario Analysis**: Trade tensions, Fed policy, GDP growth impacts

### 🤖 Automation
- **Daily Updates**: Runs automatically every weekday at 9:30 AM IST
- **GitHub Pages**: Live web deployment with dynamic HTML reports
- **Data Persistence**: JSON exports for historical analysis

## 🏗️ Technical Architecture

### Core Algorithm
The screening algorithm uses a proprietary momentum scoring system:

```
Momentum Score = 
  Beaten Down Factor (30 pts) +
  Historical Performance (25 pts) + 
  Current Positioning (25 pts) +
  Fund Quality (20 pts)
```

### Screening Criteria
1. **Primary Filter**: 1-year returns < 0%
2. **Recovery Potential**: Based on 52-week positioning
3. **Historical Strength**: 5+ year track record analysis
4. **Fund Quality**: AUM > ₹1000 Cr, expense ratio analysis

## 🛠️ Setup Instructions

### 1. Repository Setup
```bash
# Clone or create new repository
git clone <your-repo-url>
cd mutual-fund-screener

# Copy all files to your repository
```

### 2. GitHub Pages Configuration
1. Go to repository **Settings**
2. Navigate to **Pages** section
3. Set source to **GitHub Actions**
4. Enable **Actions** in repository settings

### 3. Permissions Setup
1. Go to **Settings > Actions > General**
2. Set **Workflow permissions** to **Read and write permissions**
3. Check **Allow GitHub Actions to create and approve pull requests**

### 4. Manual Trigger
- Go to **Actions** tab
- Select **Indian Mutual Fund Recovery Screener**
- Click **Run workflow**

## 📅 Schedule

The screener runs automatically:
- **Time**: Every weekday at 9:30 AM IST
- **Trigger**: GitHub Actions cron job
- **Output**: Updated HTML report and JSON data

## 📊 Output

### Live Web Report
- **URL**: `https://<username>.github.io/<repository-name>/`
- **Format**: Responsive HTML dashboard
- **Updates**: Real-time data with timestamp

### Data Exports
- **fund_analysis_data.json**: Complete analysis dataset
- **index.html**: Web dashboard

## 🎨 Report Features

### Visual Dashboard
- **Market Overview Cards**: Key NIFTY metrics
- **Interactive Table**: Sortable fund analysis
- **Color-Coded Recommendations**: Strong Buy, Buy, Hold, Avoid
- **Responsive Design**: Mobile and desktop friendly

### Fund Metrics Display
- Fund name and manager details
- AUM and category information  
- Multi-period returns analysis
- Momentum score (0-100)
- Recovery potential percentage
- Investment recommendation

## 🔧 Customization

### Adding New Funds
Edit the `sample_funds` list in `mutual_fund_screener.py`:

```python
{
    'fund_name': 'Your Fund Name',
    'fund_code': 'FUND_CODE',
    'category': 'Category',
    'aum_cr': 10000,
    '1y_return': -5.0,
    # ... other metrics
}
```

### Modifying Scoring Algorithm
Adjust weights in `calculate_momentum_indicators()` method:

```python
if short_term_return < -5:
    momentum_score += 30  # Adjust this value
```

### Changing Schedule
Edit the cron expression in `.github/workflows/mutual_fund_screener.yml`:

```yaml
schedule:
  - cron: '0 4 * * 1-5'  # 9:30 AM IST weekdays
```

## 🔍 Analysis Methodology

### Momentum Scoring
1. **Beaten Down Assessment** (30 points)
   - Heavily beaten: < -10% (30 pts)
   - Moderately beaten: -5% to -10% (20 pts)

2. **Historical Performance** (25 points)
   - Excellent: > 15% 5-year returns (25 pts)
   - Good: 10-15% 5-year returns (15 pts)

3. **Recovery Positioning** (25 points)
   - Near lows: < 30% of 52-week range (25 pts)
   - Mid-range: 30-70% of range (15 pts)
   - Near highs: > 70% of range (10 pts)

4. **Fund Quality** (20 points)
   - Large AUM: > ₹10,000 Cr (10 pts)
   - Low expenses: < 1.5% ratio (10 pts)

### Market Context Integration
- **Valuation Overlay**: NIFTY PE vs historical averages
- **Flow Analysis**: FII outflows vs DII inflows impact
- **News Sentiment**: Macro events affecting fund performance

## 📈 Investment Recommendations

### Strong Buy (80+ Score)
Funds with exceptional recovery potential:
- Significant recent underperformance
- Strong historical track record
- Currently near 52-week lows
- High-quality fund management

### Buy (65-79 Score)  
Attractive opportunities with good recovery potential

### Hold (50-64 Score)
Moderate opportunities, suitable for existing investors

### Avoid (<50 Score)
Funds with limited recovery potential or quality concerns

## ⚠️ Disclaimers

- **Educational Purpose**: This tool is for educational and research purposes only
- **Not Investment Advice**: Past performance does not guarantee future results
- **Risk Warning**: Mutual fund investments are subject to market risks
- **Consult Professionals**: Always consult with qualified financial advisors

## 🤝 Contributing

Contributions welcome! Areas for enhancement:
- Real-time data API integration
- Additional technical indicators
- Portfolio optimization features
- Risk assessment metrics
- Mobile app development

## 📞 Support

For issues or questions:
1. Check existing GitHub issues
2. Create new issue with detailed description
3. Tag with appropriate labels

---

**Built with ❤️ for the Indian mutual fund investor community**

*Helping identify tomorrow's winners from today's beaten-down funds*
