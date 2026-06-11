# Regional Sales Performance Analysis

**Author:** Arya Dheffan Shevchenko

## Overview
This project analyzes regional sales performance using a retail sales dataset (2014–2017), 
focusing on identifying which regions drive growth, where profitability issues exist, 
and what factors explain performance gaps between regions.

## Business Questions
1. Which product categories drive sales in each region?
2. How has sales growth trended year-over-year across regions?
3. Does customer segment composition explain regional performance differences?

## Key Findings
- Total sales grew from $484K (2014) to $733K (2017), a ~52% increase, but growth was 
  concentrated in West and East regions.
- **Central** generates the highest sales volume among lower performers ($501K) but the 
  **lowest profit margin (7.92%)**, driven by an average discount of 24%—nearly double 
  that of West (10.93%).
- **South** has the smallest scale across all metrics (sales, profit, orders), with a 
  margin (11.94%) close to East's, suggesting the issue is scale rather than efficiency.
- A clear inverse relationship exists between average discount and profit margin across 
  all four regions.

## Recommendations
- **Central (Priority 1):** Audit and cap discount policy. Aligning discounts closer to 
  East's level (~14.5%) could meaningfully improve margins given Central's already-large 
  sales volume.
- **South (Priority 2):** Before any investment/divestment decision, additional external 
  data is needed—regional market size, distribution coverage, and sales rep allocation. 
  The dashboard alone cannot confirm whether South's low scale is due to market potential, 
  distribution gaps, or sales execution.
- **All regions:** Review whether sales incentive structures reward revenue over profit, 
  as this likely drives the discount-margin pattern observed.

## Limitations
This analysis is based solely on the provided sales dataset. Conclusions about market 
size, distribution coverage, and brand awareness require external data not available 
in this dashboard, and should not be drawn from this analysis alone.

## Project Structure
data-analyst-portfolio-project/
├── data/sales_data.csv          # Raw dataset
├── notebook/[Python Files]     # Exploratory data analysis
├── dashboard/powerbi_dashboard.pbix  # Interactive Power BI dashboard
├── output/[Visualization Images]      # Key chart exports
└── report/summary.pdf            # Written summary report

## Tools Used
- Power BI (dashboard & visualization)
- Jupyter Notebook (exploratory analysis)
