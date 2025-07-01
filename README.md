# Walmart Sales Data Analysis

1. ## **Background and Overview**
-
This project presents a comprehensive analysis of Walmart’s historical sales data, focusing on identifying trends, evaluating performance across stores, and uncovering key factors influencing sales. Using Python, pandas, seaborn, and matplotlib, the analysis answers strategic business questions through data visualization and statistical summaries. The dataset includes weekly sales figures, holiday indicators, temperature, fuel price, CPI, and unemployment data across multiple store locations.
---

2.## **Data Structure Overview**
Source: Walmart sales CSV file

Records: ~6,435 entries (approx. 45 stores x ~143 weeks)

Features:
Store: Store ID
Date: Weekly date
Weekly_Sales: Sales amount (float)
Holiday_Flag: 1 = holiday week, 0 = regular week
Temperature: Temperature (°F)
Fuel_Price: Fuel cost per gallon
CPI: Consumer Price Index
Unemployment: Regional unemployment rate

-Data preprocessing included filling missing dates, removing duplicates, and deriving monthly summaries.

---
3. ## **Executive Summary**

Key Metrics:
-Top 5 stores contributed ≈29.45% of total weekly sales.
-Holiday weeks drove $45.84M average weekly sales vs $10.37M during non-holiday weeks.
-December showed consistent seasonal peaks across 2011 and 2012.
-Negative correlation detected between unemployment and sales performance.
---

4. ## **Insights Deep Dive**
   
### Insight 1: Top 5 Stores Drive Nearly 30% of Total Sales
Metric: Top 5 stores generated $1.81B out of $6.14B total sales.

Business Implication: High-performing stores are critical revenue centers.

Story: Store 20 led all with the highest cumulative sales, while Store 10 followed closely. These stores consistently outperformed others, showing stronger regional demand or operational excellence.

### Insight 2: Sales Peak in December Each Year
Metric: December monthly sales reached $152.9M in 2011 and $160.3M in 2012.

Business Implication: Holiday season is a critical sales driver.

Story: A clear seasonal trend shows December as a consistent sales peak, likely tied to holiday shopping. Strategic inventory and staffing should align with this demand spike.

### Insight 3: Temperature Influences Sales More Than CPI or Fuel Price
Metric: Sales increased by 15-20% during weeks with 70–80°F temperatures.

Business Implication: Warmer periods correlate with higher consumer spending.

Story: While CPI and fuel price showed weak or inconsistent patterns, temperature positively correlated with sales, especially in warmer months — possibly due to increased foot traffic or outdoor shopping behaviors.

### Insight 4: Wide Variation in Store-Level Performance
Metric: Store 10 averaged $22.15M, while Store 2 lagged at $9.82M weekly.

Business Implication: Not all locations perform equally — local factors or execution gaps may exist.

Story: Some stores (e.g., Store 13 & 14) had mirrored performance, suggesting regional clustering or identical management, while outliers indicate unique strengths or weaknesses.

### Insight 5: Holiday Weeks Outperform Regular Weeks by 342%
Metric: $45.84M (holiday weeks) vs $10.37M (non-holiday weeks)

Business Implication: Holidays are high-return opportunities for promotions.

Story: Regardless of month, holiday weeks boosted sales significantly. This suggests that campaigns, deals, and extended hours around holidays yield strong ROI.

### Insight 6: Sales Drop as Unemployment Rises
Metric: Correlation coefficient ≈ -0.53

Business Implication: Macroeconomic conditions impact consumer behavior.

Story: During higher unemployment periods, sales generally fell, underscoring consumer sensitivity to job market trends and overall confidence.

---
5. ## **Recommendations**

-Double Down on Top Stores: Invest more in Store 20, 10, and others with historically strong performance. These could be pilot locations for new initiatives.

-Holiday Campaign Planning: Begin holiday inventory buildup and marketing well ahead of December. Tailor offers around key holiday weeks.

-Weather-Responsive Stocking: Adjust product mix seasonally, especially during warmer months when sales rise.

-Store-Level Audit: Investigate underperformers like Store 2 to determine causes and possible improvements.

-Monitor Unemployment Trends: Incorporate macroeconomic dashboards into business planning to anticipate demand shifts.
