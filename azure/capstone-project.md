# **Capstone Project: Building a Sales Analytics Pipeline in Azure**


## **Objective:**
Design and implement a fully automated solution that integrates, processes, and analyzes sales data from multiple sources (CSV, JSON) using Azure Data Factory (ADF), Azure Data Lake, Azure Databricks, and Delta Lake. The system will generate actionable insights, be scalable, and run monthly updates to handle new data.

## **Business Scenario:**
A retail company collects sales, product, and customer data. The sales data comes from transactional systems as CSV files, customer data is available in JSON format from an API, and product details are maintained in CSV files. All data is stored in a GitHub repository. 

The goal is to build a centralized and automated data pipeline that:
1. **Consolidates data:** Brings data into a central repository (Azure Data Lake).  
2. **Processes and cleanses data:** Ensures high-quality, integrated datasets.  
3. **Provides analytics:** Generates insights such as regional sales trends, product performance, and monthly sales summaries.  
4. **Automates updates:** Incorporates new data monthly without manual intervention.

---

## **Pipeline Design Overview**

### **1. Data Sources**
**Source Files:**
1. **Sales Data (CSV)**  
   Contains details of each transaction.  
   - **Fields:** SaleID, ProductID, CustomerID, SalesAmount, Quantity, Timestamp

2. **Customer Data (JSON)**  
   Provides demographic and regional data about customers.  
   - **Fields:** CustomerID, FirstName, LastName, Gender, Region, SSN

3. **Product Data (CSV)**  
   Describes products sold.  
   - **Fields:** ProductID, ProductName, Category

**Storage Location:**  
All files are hosted in a GitHub repository, accessible via an HTTP URL.
- [Get Sales Data](https://raw.githubusercontent.com/pankajcloudthat/deloitte-pyspark/refs/heads/main/azure/sales.csv)
- [Get Customer Data](https://raw.githubusercontent.com/pankajcloudthat/deloitte-pyspark/refs/heads/main/azure/customers.json)
- [Get Product data](https://raw.githubusercontent.com/pankajcloudthat/deloitte-pyspark/refs/heads/main/azure/products.csv)

---

### **2. Ingestion Layer: Azure Data Factory**
**Workflow:**
1. **Create ADF Pipelines:**  
   - **Step 1:** Define HTTP-linked services to connect to the GitHub repository.  
   - **Step 2:** Use copy activities to download files into Azure Data Lake Gen2 (ADLS).  
   - **Destination:** Raw zone in ADLS with a structured folder hierarchy:
     - `/raw/sales/`
     - `/raw/customers/`
     - `/raw/products/`

2. **Parameterize Pipeline:**  
   - Use parameters for dynamic file names, source URLs, and output destinations, ensuring the pipeline works for monthly data uploads.

3. **Trigger Automation:**  
   - Schedule the ADF pipeline to run on the 1st of every month using time-based triggers.

---

### **3. Storage Layer: Azure Data Lake**
**Structure in ADLS:**
- **Raw Data:** Unprocessed data ingested from GitHub.  
- **Processed Data:** Cleaned and transformed data stored in Delta format.  
- **Output Data:** Aggregated metrics for visualization and analytics.

---

### **4. Transformation Layer: Azure Databricks**
**Process:**
1. **Read Raw Data:**  
   - Use PySpark to load CSV and JSON files from the raw zone in ADLS.  

2. **Data Cleansing:**  
   - Handle missing or null values.
   - Normalize inconsistent formats (e.g., unify timestamp format).  
   - Validate numerical fields (e.g., ensure non-negative sales amounts).  

3. **Data Integration:**  
   - **Join Datasets:**  
     - Merge sales data with customer data on `CustomerID`.
     - Merge the result with product data on `ProductID`.  

4. **Data Transformation:**  
   - Extract `Year` and `Month` from the `Timestamp` field.  
   - Calculate additional metrics if required (e.g., `AverageSalesPerProduct`).

5. **Store in Delta Lake:**  
   - Save the cleaned and transformed data in Delta format in the processed zone of ADLS.

6. **Register External Table:**  
   - Use Delta Lake to create an external table for querying.

---

### **5. Analytics and Visualization:**
**EDA (Exploratory Data Analysis):**
- Use Databricks Notebooks with PySpark, Matplotlib, and Plotly to analyze:
  - Regional sales trends.  
  - Monthly and yearly sales growth.  
  - Product category performance.  

**Visualization Outputs:**
1. Bar plots for total sales by region and category.  
2. Line charts for monthly sales trends.  
3. Pie charts showing sales distribution by product category.

---

### **6. Aggregated Metrics and Reporting:**
**Metrics:**  
- Calculate total sales and quantity grouped by:
  - Region.  
  - Product Category.  
  - Year and Month.  

**Output:**
- Save the aggregated metrics as Delta tables.

---

### **7. Security:**
**Azure Key Vault:**
- Store sensitive information like:
  - ADLS storage keys.  
  - Databricks tokens.  
  - ADF Linked Service credentials.  

**Integration:**  
- Configure ADF and Databricks to fetch secrets from Key Vault securely.

---

### **8. Automation:**
1. **Pipeline Scheduling:**  
   - Use ADF triggers for monthly ingestion.  

2. **Databricks Job Scheduling:**  
   - Automate the transformation and aggregation process using Databricks Jobs.  
   - Use the Databricks CLI or REST API to integrate job triggers with ADF.  

---

### **Challenges Addressed**
1. **Data Integration Across Formats:** Unified raw data stored in multiple formats (CSV, JSON) into a consistent format.  

2. **Scalability:**  Delta Lake ensures fast querying and storage optimization for large datasets.  

3. **Automation:**  Monthly updates via ADF and Databricks reduce manual effort.  

4. **Security:**  Leveraging Azure Key Vault to manage sensitive credentials.

---
