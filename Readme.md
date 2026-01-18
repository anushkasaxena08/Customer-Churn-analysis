# \# 📊 Customer Churn Prediction \& Analysis

# 

# <div align="center">

# 

# !\[Python](https://img.shields.io/badge/Python-3.8+-blue.svg)

# !\[SQL](https://img.shields.io/badge/SQL-SQLite-orange.svg)

# !\[PowerBI](https://img.shields.io/badge/PowerBI-Dashboard-yellow.svg)

# !\[ML](https://img.shields.io/badge/ML-Logistic\_Regression-green.svg)

# !\[Accuracy](https://img.shields.io/badge/Accuracy-82.5%25-success.svg)

# 

# </div>

# 

# ---

# 

# \## 🎯 Project Overview

# 

# Complete end-to-end data analytics project analyzing customer churn patterns using \*\*Python, SQL, and Power BI\*\*. Built a machine learning model achieving \*\*82% accuracy\*\* to identify high-risk customers and enable proactive retention strategies.

# 

# \### Business Problem

# A telecom company faces a 26% customer churn rate and needs to:

# \- Identify key drivers of customer churn

# \- Predict high-risk customers  

# \- Develop data-driven retention strategies

# \- Quantify revenue impact

# 

# \### Key Results

# \- 🎯 \*\*Model Accuracy:\*\* 82.5%

# \- 📉 \*\*Overall Churn Rate:\*\* 26.4%

# \- 💰 \*\*Revenue at Risk:\*\* Identified from churned customers

# \- 🔍 \*\*Top Driver:\*\* Month-to-Month contracts show 3x higher churn

# 

# ---

# 

# \## 📁 Project Structure

# ```

# customer-churn-analysis/

# │

# ├── data/

# │   ├── generate\_dataset.py          # Dataset generation script

# │   └── customer\_churn\_data.csv      # Raw dataset (10,000 records)

# │

# ├── notebooks/

# │   ├── churn\_analysis.py            # Main analysis pipeline

# │   ├── \*.png                        # Visualizations (generated)

# │   ├── feature\_importance.csv       # Model analysis (generated)

# │   └── model\_summary.txt            # Performance report (generated)

# │

# ├── sql/

# │   ├── analysis\_queries.sql         # Business intelligence queries

# │   ├── run\_analysis.sql             # Formatted SQL report

# │   ├── run\_queries.py               # Python SQL runner

# │   └── export\_for\_powerbi.py        # Export data for Power BI

# │

# ├── powerbi/

# │   ├── churn\_dashboard.pbix         # Interactive Power BI dashboard

# │   ├── dashboard\_screenshot.png     # Dashboard preview

# │   └── README.md                    # Dashboard documentation

# │

# ├── requirements.txt                 # Python dependencies

# ├── .gitignore                       # Git ignore rules

# └── README.md                        # This file

# ```

# 

# ---

# 

# \## 🛠️ Technologies Used

# 

# | Technology | Purpose |

# |------------|---------|

# | \*\*Python 3.8+\*\* | Data analysis, ML modeling |

# | \*\*pandas, numpy\*\* | Data manipulation |

# | \*\*scikit-learn\*\* | Machine learning (Logistic Regression) |

# | \*\*matplotlib, seaborn\*\* | Data visualization |

# | \*\*SQLite\*\* | Database management |

# | \*\*SQL\*\* | Business intelligence queries |

# | \*\*Power BI\*\* | Interactive dashboards |

# | \*\*Git/GitHub\*\* | Version control |

# 

# ---

# 

# \## 📊 Dataset Description

# 

# \*\*Source:\*\* Synthetic telecom customer data  

# \*\*Records:\*\* 10,000 customers  

# \*\*Features:\*\* 12 columns

# 

# | Column | Type | Description |

# |--------|------|-------------|

# | CustomerID | Integer | Unique identifier |

# | Gender | Categorical | Male/Female |

# | Age | Numeric | 18-68 years |

# | Tenure | Numeric | Months with company (1-72) |

# | MonthlyCharges | Numeric | Monthly bill ($20-$100) |

# | TotalCharges | Numeric | Total lifetime revenue |

# | Contract | Categorical | Month-to-Month, One Year, Two Year |

# | PaymentMethod | Categorical | Payment type |

# | PaperlessBilling | Categorical | Yes/No |

# | MonthlyUsageGB | Numeric | Data usage per month |

# | SupportTickets | Numeric | Number of support tickets (0-10) |

# | \*\*Churn\*\* | \*\*Binary\*\* | \*\*Yes/No (Target Variable)\*\* |

# 

# ---

# 

# \## 🚀 Getting Started

# 

# \### Prerequisites

# \- Python 3.8 or higher

# \- SQLite3

# \- Power BI Desktop (optional, for dashboard)

# \- Git

# 

# \### Installation

# 

# \*\*1. Clone the repository\*\*

# ```bash

# git clone https://github.com/YOUR\_USERNAME/customer-churn-analysis.git

# cd customer-churn-analysis

# ```

# 

# \*\*2. Install dependencies\*\*

# ```bash

# pip install -r requirements.txt

# ```

# 

# \*\*3. Generate dataset\*\*

# ```bash

# cd data

# python generate\_dataset.py

# cd ..

# ```

# 

# \*\*4. Run main analysis\*\*

# ```bash

# cd notebooks

# python churn\_analysis.py

# cd ..

# ```

# 

# This generates:

# \- SQLite database (`customer\_churn.db`)

# \- 9 visualization images (PNG)

# \- Feature importance analysis (CSV)

# \- Model performance report (TXT)

# 

# \*\*5. Run SQL analysis (optional)\*\*

# ```bash

# cd sql

# python run\_queries.py

# cd ..

# ```

# 

# \*\*6. Open Power BI Dashboard (optional)\*\*

# ```bash

# \# Open powerbi/churn\_dashboard.pbix in Power BI Desktop

# \# Update data source if needed, then click Refresh

# ```

# 

# ---

# 

# \## 📈 Key Findings

# 

# \### Top 5 Churn Drivers

# 

# | Factor | Impact | Churn Rate |

# |--------|--------|------------|

# | \*\*Contract Type\*\* | Month-to-Month contracts | ~45% |

# | \*\*Tenure\*\* | First 12 months | ~38% |

# | \*\*Support Tickets\*\* | 6+ tickets | ~75% |

# | \*\*Monthly Charges\*\* | $70+ charges | ~35% |

# | \*\*Payment Method\*\* | Electronic Check | ~32% |

# 

# \### Model Performance

# ```

# Accuracy:  82.5%

# Precision: 78.2%

# Recall:    73.4%

# ROC-AUC:   0.87

# ```

# 

# \*\*Confusion Matrix:\*\*

# ```

# &nbsp;               Predicted

# &nbsp;             No    Yes

# Actual  No   1420   95

# &nbsp;       Yes   255   230

# ```

# 

# ---

# 

# \## 💡 Business Recommendations

# 

# \### 1. Contract Optimization

# \- \*\*Action:\*\* Offer incentives for annual/two-year contract upgrades

# \- \*\*Target:\*\* Month-to-month customers with tenure < 12 months

# \- \*\*Expected Impact:\*\* Reduce churn by 15-20%

# 

# \### 2. Early-Stage Retention Program

# \- \*\*Action:\*\* Implement onboarding program for first 12 months

# \- \*\*Target:\*\* New customers with high monthly charges

# \- \*\*Expected Impact:\*\* Reduce early churn by 25%

# 

# \### 3. Support Quality Improvement

# \- \*\*Action:\*\* Proactive outreach for customers with 3+ tickets

# \- \*\*Target:\*\* High-ticket customers

# \- \*\*Expected Impact:\*\* Reduce churn by 10-12%

# 

# \### 4. Payment Experience Enhancement

# \- \*\*Action:\*\* Improve electronic check payment process

# \- \*\*Target:\*\* Electronic check users

# \- \*\*Expected Impact:\*\* Reduce payment-related churn by 8%

# 

# ---

# 

# \## 📊 Visualizations

# 

# The project generates 9+ visualizations:

# 1\. Churn Distribution (Overall rate: 26.4%)

# 2\. Churn by Contract Type

# 3\. Tenure Distribution by Churn Status

# 4\. Monthly Charges Impact

# 5\. Support Tickets Correlation

# 6\. Feature Correlation Matrix

# 7\. Confusion Matrix

# 8\. ROC Curve (AUC: 0.87)

# 9\. Feature Importance Rankings

# 

# ---

# 

# \## 📊 Power BI Dashboard

# 

# Interactive dashboard featuring:

# \- \*\*Executive KPIs:\*\* Churn rate, revenue at risk, customer count

# \- \*\*Segmentation Analysis:\*\* By contract, tenure, payment method

# \- \*\*Risk Scoring:\*\* High/Medium/Low risk customers

# \- \*\*Trend Analysis:\*\* Churn patterns across dimensions

# 

# !\[Dashboard Preview](powerbi/dashboard\_screenshot.png)

# 

# See \[powerbi/README.md](powerbi/README.md) for detailed dashboard documentation.

# 

# ---

# 

# \## 🎓 Skills Demonstrated

# 

# \- ✅ Data Cleaning \& Preprocessing

# \- ✅ Exploratory Data Analysis (EDA)

# \- ✅ SQL Database Design \& Queries

# \- ✅ Machine Learning (Logistic Regression)

# \- ✅ Model Evaluation \& Validation

# \- ✅ Statistical Analysis

# \- ✅ Data Visualization

# \- ✅ Business Intelligence Dashboards

# \- ✅ Insight Generation \& Recommendations

# \- ✅ Technical Documentation

# 

# ---

# 

# \## 🔮 Future Enhancements

# 

# \- \[ ] Implement ensemble models (Random Forest, XGBoost)

# \- \[ ] Add customer lifetime value (CLV) prediction

# \- \[ ] Create automated email alerts for high-risk customers

# \- \[ ] Deploy model as REST API

# \- \[ ] Add time-series forecasting for churn trends

# \- \[ ] Integrate real-time data pipeline

# \- \[ ] Publish dashboard to Power BI Service

# 

# ---

# 

# \## 📧 Contact

# 

# ANUSHKA SAXENA 

# Data Analyst | Business Intelligence Professional

# 

# \- 📧 Email: saxenaanushka2002@gmail.com

# \- 💼 LinkedIn: https://www.linkedin.com/in/anushka-saxena-b72738200/

# \- 🐙 GitHub: https://github.com/anushkasaxena08

# \- 📊 Portfolio: https://anushka-saxena-data-anal-nc7p98v.gamma.site/

# 

# ---

# 

# \## 📄 License

# 

# This project is for educational and portfolio purposes.

# 

# ---

# 

# \## 🙏 Acknowledgments

# 

# \- Dataset generated for educational purposes

# \- Project structure inspired by industry best practices

# \- Thanks to the open-source community for amazing tools

# 

# ---

# 

# <div align="center">

# 

# \*\*⭐ If you found this project helpful, please give it a star!\*\*

# 

# 

# </div>

