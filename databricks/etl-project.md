# **Project Title**:  
**"End-to-End ETL Pipeline using Databricks with Azure SQL and Data Lake Storage"**

---

## **Objective**:  
Students will build an end-to-end ETL pipeline using Databricks to extract, transform, and load data from Azure SQL Database and Azure Data Lake Storage. They will perform data transformations, calculations, and store the processed results into SQL Database and Delta tables.

---

## **Project Description**:  
This project focuses on creating an **ETL pipeline** to analyze sales and user profile data. Students will learn to connect to Azure SQL Database, read and flatten JSON files from ADLS, perform transformations, calculate metrics, and store the processed data into Azure SQL and Delta tables.

---

## **Data Sources**:
1. **Azure SQL Database**: Sales Transaction Data  
   - Schema: `TransactionId`, `CustomerId`, `ProductId`, `Quantity`, `Price`, `TotalAmount`, `TransactionDate`, `ProfitAmount`, `Hour`, `Minute`,`StoreId`
2. **Azure Data Lake Storage**: User Profile Data (JSON format)
   - Sample JSON Schema:  
     ```json
      [
          {
              "visitorId": 9529082,
              "topProductPurchases": [
                  {
                      "productId": 4679,
                      "itemsPurchasedLast12Months": 26
                  },
                  {
                      "productId": 1779,
                      "itemsPurchasedLast12Months": 32
                  },
                  {
                      "productId": 2125,
                      "itemsPurchasedLast12Months": 75
                  },                  
                  {
                      "productId": 1219,
                      "itemsPurchasedLast12Months": 56
                  },
                  {
                      "productId": 2982,
                      "itemsPurchasedLast12Months": 59
                  }
              ]
          },
          {
              ...
          },
          {
              ...
          }
      ]

     ```

---

## **Project Tasks**:  

### **Task 1: Extract Data**  

#### a) **Load User Profile Data from ADLS**  
- Read the JSON file stored in Azure Data Lake Storage into a Databricks DataFrame.  
- Flatten the nested JSON data into individual columns.

#### b) **Load Sales Data from Azure SQL Database**  
- Connect to Azure SQL Database using JDBC and read the `sales` table.

---

### **Task 2: Transform Data**  

Perform the following transformations:

1. **Flatten JSON Data**:  
   Flatten the user profile JSON into columns:  
   - `visitorId`,`productId`,`itemsPurchasedLast12Months`.

2. **Calculate Metrics**:
   - **Profit by Date and Product**: Group by `TransactionDate` and `ProductId` and calculate the sum of `ProfitAmount`.
   - **Products Purchased by Each Customer**: Count the productss for each `visitorId`.
   - **Total Items Purchased by Each Customer**: Sum the `quantity` for each `userId`.
   - **Total Amount Spent on Each Product in December**: Filter transactions for December and calculate the total amount (Quantity * Price).

---

### **Task 3: Load Data**  

1. **Store Transformed JSON Data**:  
   Write the flattened JSON data into the **Azure SQL Database** table `toppurchase`.

2. **Store December Spending Data**:  
   Save the total amount spent on each product in December as a **Delta table** in **DBFS**.

---

## **Deliverables**  

### 1. **Code and Output**  
- Submit the Databricks Notebook containing:  
  - Code for loading, transforming, and storing the data  
  - Outputs for all calculated metrics (Profit, Product Types, Total Items, December Spend).

### 2. **Results Verification**  
- Verify that:  
   - The `toppurchase` table is updated in Azure SQL Database  
   - The December spending data is stored as a Delta table in DBFS.

### 3. **Project Report**  
Prepare a brief report (1-2 pages) describing:  
- The project goals  
- The ETL process  
- The insights derived from the calculations  

---

## **Skills Developed**  
1. Extracting data from Azure SQL and ADLS  
2. Performing transformations with PySpark  
3. Writing data to Azure SQL Database and Delta tables  
4. Using Databricks for ETL pipelines  
5. Querying and analyzing JSON data  

---

## **Evaluation Criteria**  
1. Correct implementation of data extraction, transformation, and loading.  
2. Proper code structure and documentation in Databricks Notebooks.  
3. Accuracy of calculated metrics.  
4. Successful verification of results in Azure SQL Database and Delta tables.

---

This project ensures that students gain real-world experience in ETL processes, data transformations, and using Azure Databricks for end-to-end data engineering workflows.
