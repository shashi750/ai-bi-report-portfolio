\# AI-Assisted BI Report



\*\*Elevator pitch:\*\* Power BI dashboard + small Python backend that answers natural-language business questions and generates weekly insights.



\## Repo skeleton

\- `dashboard/` : Power BI file (.pbix) + screenshots

\- `backend/` : Python code for embeddings/index and a small API

\- `data\_sample/` : sanitized CSVs (no PII)

\- `demo/` : demo video + short clip / screenshots

\- `how\_to\_run.md` : exact run instructions


## Project Idea: AI-Powered Sales & Customer Insights

**Goal:** Build a Power BI dashboard showing sales, revenue, products, and customer trends.  
Integrate a Python AI backend to answer natural-language business questions using sample CSV data.  

**Key Features:**  
- Power BI visuals: sales by region, top products, monthly revenue, top customers  
- Python backend: query data using natural language (embeddings + cosine similarity)  
- Sample data: orders_sample.csv, customers_sample.csv  
- Demo: screenshots + short 2-3 min video

## 📊 Power BI Dashboard: Customer Insights

This dashboard provides key insights into customer demographics and behavior:

- **Age Distribution**: Helps identify target age groups.
- **Income Analysis**: Compare average income across different marital statuses.
- **Customer Segmentation**: Donut chart shows % of customers by marital status.
- **KPI Cards**: Highlights overall customer count, average income, and average age.

🔹 **Use Case**:  
Business managers can use these insights to target campaigns more effectively, e.g., focusing high-income married customers with premium offers.

📂 File Location: `data_sample/Dashboard/Customer.pbix`

## 🚀 How to Run the Python Backend

1. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate   # On Windows


pip install -r requirements.txt
python backend/segmentation.py



---

## 📊 Key Insights
- Customers segmented into **3 clusters** based on Income + Demographics.
- Cluster 0 → Low-income group  
- Cluster 1 → Mid-income group  
- Cluster 2 → High-income group  
- Business can target:
  - **Cluster 0** with budget-friendly offers.  
  - **Cluster 1** with cross-sell opportunities.  
  - **Cluster 2** with premium services/products.  

---

## ✅ Next Steps
- Add more features (Age, Spending Score, etc.) to improve clustering.
- Automate the pipeline → schedule Python script for weekly refresh.
- Deploy Power BI dashboard to Power BI Service for online access.
- Enhance demo with short walkthrough video.

---

