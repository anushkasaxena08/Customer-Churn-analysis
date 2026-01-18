-- ============================================================
-- CUSTOMER CHURN ANALYSIS - SQL QUERIES
-- Database: customer_churn.db (SQLite)
-- ============================================================

-- 1. OVERALL CHURN METRICS
-- Executive summary of key metrics
SELECT 
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
    ROUND(SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS churn_rate_pct,
    ROUND(AVG(MonthlyCharges), 2) AS avg_monthly_charge,
    ROUND(SUM(MonthlyCharges), 2) AS total_monthly_revenue,
    ROUND(AVG(Tenure), 2) AS avg_tenure_months
FROM customers;

-- 2. CHURN BY CONTRACT TYPE
-- Analyze churn patterns across different contract types
SELECT 
    Contract,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
    ROUND(SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS churn_rate_pct,
    ROUND(AVG(MonthlyCharges), 2) AS avg_monthly_charge
FROM customers
GROUP BY Contract
ORDER BY churn_rate_pct DESC;

-- 3. REVENUE AT RISK ANALYSIS
-- Calculate revenue impact of churn
SELECT 
    Churn,
    COUNT(*) AS customer_count,
    ROUND(SUM(MonthlyCharges), 2) AS total_monthly_revenue,
    ROUND(AVG(MonthlyCharges), 2) AS avg_monthly_charge,
    ROUND(SUM(TotalCharges), 2) AS total_lifetime_value,
    ROUND(AVG(TotalCharges), 2) AS avg_lifetime_value
FROM customers
GROUP BY Churn;

-- 4. CHURN BY TENURE GROUPS
-- Identify critical retention periods
SELECT 
    CASE 
        WHEN Tenure <= 12 THEN '0-12 months'
        WHEN Tenure <= 24 THEN '13-24 months'
        WHEN Tenure <= 48 THEN '25-48 months'
        ELSE '48+ months'
    END AS tenure_group,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
    ROUND(SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS churn_rate_pct
FROM customers
GROUP BY tenure_group
ORDER BY 
    CASE tenure_group
        WHEN '0-12 months' THEN 1
        WHEN '13-24 months' THEN 2
        WHEN '25-48 months' THEN 3
        ELSE 4
    END;

-- 5. CHURN BY PAYMENT METHOD
-- Analyze payment method impact on churn
SELECT 
    PaymentMethod,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
    ROUND(SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS churn_rate_pct
FROM customers
GROUP BY PaymentMethod
ORDER BY churn_rate_pct DESC;

-- 6. SUPPORT TICKETS IMPACT ANALYSIS
-- Correlation between support tickets and churn
SELECT 
    CASE 
        WHEN SupportTickets = 0 THEN '0 tickets'
        WHEN SupportTickets <= 2 THEN '1-2 tickets'
        WHEN SupportTickets <= 5 THEN '3-5 tickets'
        ELSE '6+ tickets'
    END AS ticket_category,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
    ROUND(SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS churn_rate_pct
FROM customers
GROUP BY ticket_category
ORDER BY churn_rate_pct DESC;

-- 7. HIGH-RISK CUSTOMERS
-- Identify customers at high risk of churning
SELECT 
    CustomerID,
    Gender,
    Age,
    Tenure,
    MonthlyCharges,
    Contract,
    SupportTickets,
    Churn
FROM customers
WHERE Contract = 'Month-to-Month'
  AND Tenure < 12
  AND (SupportTickets > 3 OR MonthlyCharges > 70)
ORDER BY MonthlyCharges DESC
LIMIT 100;

-- 8. CUSTOMER SEGMENTATION BY RISK
-- Categorize customers into risk segments
SELECT 
    CASE 
        WHEN Contract = 'Month-to-Month' AND Tenure < 12 THEN 'High Risk'
        WHEN Contract = 'Month-to-Month' AND Tenure >= 12 THEN 'Medium Risk'
        WHEN Contract IN ('One Year', 'Two Year') AND SupportTickets > 5 THEN 'Medium Risk'
        ELSE 'Low Risk'
    END AS risk_segment,
    COUNT(*) AS customer_count,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
    ROUND(SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS churn_rate_pct,
    ROUND(SUM(MonthlyCharges), 2) AS total_monthly_revenue
FROM customers
GROUP BY risk_segment
ORDER BY churn_rate_pct DESC;

-- 9. CHURN BY AGE GROUPS
-- Demographic analysis of churn
SELECT 
    CASE 
        WHEN Age < 30 THEN '18-29'
        WHEN Age < 40 THEN '30-39'
        WHEN Age < 50 THEN '40-49'
        WHEN Age < 60 THEN '50-59'
        ELSE '60+'
    END AS age_group,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
    ROUND(SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS churn_rate_pct
FROM customers
GROUP BY age_group
ORDER BY age_group;

-- 10. MONTHLY CHARGES ANALYSIS
-- Revenue tier analysis
SELECT 
    CASE 
        WHEN MonthlyCharges < 30 THEN 'Low ($0-$30)'
        WHEN MonthlyCharges < 60 THEN 'Medium ($30-$60)'
        WHEN MonthlyCharges < 90 THEN 'High ($60-$90)'
        ELSE 'Very High ($90+)'
    END AS charge_tier,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
    ROUND(SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS churn_rate_pct,
    ROUND(AVG(MonthlyCharges), 2) AS avg_charge
FROM customers
GROUP BY charge_tier
ORDER BY 
    CASE charge_tier
        WHEN 'Low ($0-$30)' THEN 1
        WHEN 'Medium ($30-$60)' THEN 2
        WHEN 'High ($60-$90)' THEN 3
        ELSE 4
    END;

-- 11. GENDER-BASED CHURN ANALYSIS
SELECT 
    Gender,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
    ROUND(SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS churn_rate_pct
FROM customers
GROUP BY Gender;

-- 12. COHORT ANALYSIS - CONTRACT & PAYMENT METHOD
-- Identify high-risk combinations
SELECT 
    Contract,
    PaymentMethod,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
    ROUND(SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS churn_rate_pct
FROM customers
GROUP BY Contract, PaymentMethod
HAVING COUNT(*) > 50
ORDER BY churn_rate_pct DESC;

-- 13. AVERAGE METRICS BY CHURN STATUS
SELECT 
    Churn,
    ROUND(AVG(Age), 2) AS avg_age,
    ROUND(AVG(Tenure), 2) AS avg_tenure,
    ROUND(AVG(MonthlyCharges), 2) AS avg_monthly_charges,
    ROUND(AVG(MonthlyUsageGB), 2) AS avg_usage_gb,
    ROUND(AVG(SupportTickets), 2) AS avg_support_tickets
FROM customers
GROUP BY Churn;

-- 14. TOP 20 HIGHEST VALUE CHURNED CUSTOMERS
-- For targeted win-back campaigns
SELECT 
    CustomerID,
    Tenure,
    MonthlyCharges,
    TotalCharges,
    Contract,
    PaymentMethod,
    SupportTickets
FROM customers
WHERE Churn = 'Yes'
ORDER BY TotalCharges DESC
LIMIT 20;

-- 15. PAPERLESS BILLING IMPACT
SELECT 
    PaperlessBilling,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
    ROUND(SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS churn_rate_pct
FROM customers
GROUP BY PaperlessBilling;
