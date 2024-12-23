## **Capstone Project Scenario: Building a Sales Analytics Pipeline in Azure**

### **Project Title:** 
End-to-End Data Pipeline and Analytics Solution for Sales Data

### **Objective:**
Create an automated data pipeline to process, transform, analyze, and visualize sales data stored in various formats (CSV, JSON). The solution will involve Azure Data Factory for ingestion, Azure Data Lake for storage, Azure Databricks for transformation and analysis, and Delta Lake for storing processed data. Additionally, the solution will be automated for monthly updates.

---

### **Scenario Overview:**

#### **Source Data Details:**
1. **Sales Data (CSV)**  
   - **Location:** GitHub (HTTP source)  
   - **Schema:**
     ```
     |-- SaleID: string
     |-- ProductID: integer
     |-- CustomerID: string
     |-- SalesAmount: double
     |-- Quantity: integer
     |-- Timestamp: timestamp
     ```

2. **Customer Data (JSON)**  
   - **Location:** GitHub (HTTP source)  
   - **Schema:**
     ```
     |-- CustomerID: string
     |-- FirstName: string
     |-- Gender: string
     |-- LastName: string
     |-- Region: string
     |-- SSN: string
     ```

3. **Product Data (CSV)**  
   - **Location:** GitHub (HTTP source)  
   - **Schema:**
     ```
     |-- ProductID: integer
     |-- ProductName: string
     |-- Category: string
     ```

---

### **Steps to Accomplish:**

#### **1. Data Ingestion:**
- **Tool:** Azure Data Factory (ADF)  
- **Process:**  
  - Create pipelines in ADF to fetch data from GitHub (HTTP source) and store it in **Azure Data Lake**.  
  - Separate folders for each dataset:
    - Sales Data: `/raw/sales/`
    - Customer Data: `/raw/customers/`
    - Product Data: `/raw/products/`

---

#### **2. Data Cleansing and Transformation:**
- **Tool:** Azure Databricks (with PySpark)  
- **Process:**  
  - **Read raw data** from Azure Data Lake using PySpark.
  - **Cleansing:**
    - Handle null values and inconsistent data.
    - Validate data formats (e.g., Timestamp format, non-negative SalesAmount, etc.).
  - **Transformation:**
    - Merge datasets based on common keys:
      - `CustomerID` for Sales and Customer Data.
      - `ProductID` for Sales and Product Data.
    - Add derived columns such as `Year` and `Month` from the `Timestamp` field.
  - **Store transformed data** in Delta Lake format in Azure Data Lake (`/processed/`).

---

#### **3. Exploratory Data Analysis (EDA):**
- **Tool:** Databricks Notebooks (Python with Matplotlib/Seaborn/Plotly)  
- **Process:**
  - Perform EDA to uncover insights such as:
    - Sales distribution by region and category.
    - Monthly trends in sales and quantity.
  - Visualize findings using charts and graphs (e.g., bar plots, line charts, pie charts).

---

#### **4. Aggregated Metrics Calculation:**
- **Metrics:**  
  - Total Sales (`SUM(SalesAmount)`) and Quantity (`SUM(Quantity)`) by:
    - **Region**
    - **Category**
    - **Year**
    - **Month**
- **Storage:**
  - Save the aggregated data in Delta Lake format.
  - Register the Delta tables as **External Tables** for easy querying.

---

#### **5. Security:**
- **Tool:** Azure Key Vault  
- **Process:**
  - Store secrets like storage account keys, ADF credentials, and Databricks connection strings in Azure Key Vault.
  - Access secrets securely in ADF and Databricks.

---

#### **6. Automation:**
- **Tool:** Azure Data Factory and Databricks Jobs  
- **Process:**  
  - Schedule the data pipeline in ADF to fetch new data monthly.  
  - Use Databricks Jobs to automate the cleansing, transformation, and metric calculation processes on a monthly basis.

---

#### **Expected Deliverables:**
1. **Automated Data Pipeline:**  
   - Fetch raw data from GitHub to Azure Data Lake.
   - Process and store cleaned data in Delta format.

2. **Insights and Visualizations:**  
   - Sales trends and performance charts.

3. **Aggregated Results:**  
   - Total sales and quantity by Region, Category, Year, and Month.

4. **Automation:**  
   - Scheduled workflows for monthly updates.

---

### **Challenges Addressed:**
1. **Data Integration:** Combining CSV and JSON data into a unified format.
2. **Automation:** Ensuring monthly updates without manual intervention.
3. **Scalability:** Using Delta Lake for fast and efficient querying.
4. **Security:** Protecting sensitive information via Azure Key Vault.

---
