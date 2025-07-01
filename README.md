# Walmart Sales Data Analysis

## 1. Background and Overview

This project presents a comprehensive analysis of Walmart’s historical sales data, focusing on identifying trends, evaluating performance across stores, and uncovering key factors influencing sales.

Using Python, pandas, seaborn, and matplotlib, the analysis answers strategic business questions through data visualization and statistical summaries.

The dataset includes weekly sales figures, holiday indicators, temperature, fuel price, CPI and unemployment data across multiple store locations.

---

## 2. Data Structure Overview

- **Source**: Walmart sales CSV file  
- **Records**: ~6,435 entries (approx. 45 stores × ~143 weeks)

### Features:
- **Store**: Store ID  
- **Date**: Weekly date  
- **Weekly_Sales**: Sales amount (float)  
- **Holiday_Flag**: 1 = holiday week, 0 = regular week  
- **Temperature**: Temperature (°F)  
- **Fuel_Price**: Fuel cost per gallon  
- **CPI**: Consumer Price Index  
- **Unemployment**: Regional unemployment rate  

> *Data preprocessing included filling missing dates, removing duplicates, and deriving monthly summaries.*

---

## 3. Executive Summary

### Key Metrics:
- **Top 5 stores** contributed ≈29.45% of total weekly sales.
- **Holiday weeks** drove $45.84M average weekly sales vs. $10.37M during non-holiday weeks.
- **December** showed consistent seasonal peaks across 2011 and 2012.
- **Negative correlation** detected between unemployment and sales performance.

---

## 4. Insights Deep Dive

### Insight 1: Top 5 Stores Drive Nearly 30% of Total Sales
- **Metric**: Top 5 stores generated $1.81B out of $6.14B total sales.
- **Implication**: High-performing stores are critical revenue centers.

> *Store 20 led all with the highest cumulative sales, followed by Store 10.*

---

### Insight 2: Sales Peak in December Each Year
- **Metric**: $152.9M in Dec 2011, $160.3M in Dec 2012.
- **Implication**: Holiday season is a critical sales driver.

---

### Insight 3: Temperature Influences Sales More Than CPI or Fuel Price
- **Metric**: Sales increased by 15–20% during weeks with 70–80°F.
- **Implication**: Warmer weather correlates with higher spending.

---

### Insight 4: Wide Variation in Store-Level Performance
- **Metric**: Store 10 averaged $22.15M vs. Store 2 at $9.82M.
- **Implication**: Performance gaps suggest local factors or inefficiencies.

---

### Insight 5: Holiday Weeks Outperform Regular Weeks by 342%
- **Metric**: $45.84M vs. $10.37M average weekly sales.
- **Implication**: Strong opportunity for promotional ROI.

---

### Insight 6: Sales Drop as Unemployment Rises
- **Metric**: Correlation coefficient ≈ -0.53
- **Implication**: Sales are sensitive to macroeconomic conditions.

---

## 5. Recommendations

- **Double Down on Top Stores**: Focus investment on Stores 20 and 10.
- **Holiday Campaign Planning**: Begin inventory and marketing early.
- **Weather-Responsive Stocking**: Adapt product mix for warmer months.
- **Store-Level Audit**: Investigate underperformers like Store 2.
- **Monitor Unemployment Trends**: Integrate economic metrics in planning.

---

© 2025 NaweeO

