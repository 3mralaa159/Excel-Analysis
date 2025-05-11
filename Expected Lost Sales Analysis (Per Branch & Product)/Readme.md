### **Objective:**

To identify potential lost sales across branches over the next 10 days due to stock shortages, using historical sales and current inventory data.

---

## 🔧 **1. Data Cleaning & Transformation**

### **Sheet 1 – Raw Sales Data (Last 28 Days)**

#### a. **Branch Name Cleanup**

- The `Branch Name` column contained concatenated codes and names (e.g., `"BR001 - Cairo"`).
    
- Used `LEFT`, `LEN`, and `RIGHT` functions to extract **branch codes** only.
    
- Created a **reference table** with `Branch Code` and `Clean Branch Name`.
    
- Used `VLOOKUP` to map each record to the correct branch name from the reference table.
    

#### b. **Date Format**

- The `Date` column had inconsistent formats.
    
- Split the column and reformatted into standard `DateTime` format (yyyy-mm-dd).
    

#### c. **Blank Cells (Fill Down)**

- Detected and filled blank cells (e.g., `Receipt Number`, `Date`, `Branch`) using **Fill Down** to ensure each transaction row is complete.
    

---

##  **2. Demand Forecasting Using Pivot Table**

### a. **Summarization**

- Created a **Pivot Table** summarizing:
    
    - Total `Quantity Sold` per `Branch` and `Product`.
        

### b. **Calculated Fields**

- **Daily Demand**:
 
    `= Quantity_Sold / 28`
    
- **Expected Sales for Next 10 Days**:

    `= Daily_Demand * 10`
    

---

##  **3. Integrating Current Stock Data**

### Sheet 2 – Current Stock

- Used `INDEX-MATCH` formula to retrieve `Current Stock` for each Branch-Product combo:
- 
    `=INDEX('StockSheet'!$B$3:$DK$5985, MATCH(Dashboard!B2, 'StockSheet'!$A$2:$A$5985, 0), MATCH(Dashboard!A2, 'StockSheet'!$B$2:$DK$2, 0))`
    
- **Cleaned up** mismatched `Product Names` manually and removed:
    
    - Irrelevant entries.
        
    - Products with no valid stock data.
        
- **Left negative stock** values intentionally to flag potentially critical stock errors.
    

---

##  **4. Lost Sales and Risk Analysis**

### a. **Expected Lost Sales**

`= MAX(0, Expected_Sales - Current_Stock)`

### b. **Risk Flag**

`= IF(Expected_Lost_Sales > 0, "At Risk", "Safe")`

### c. **Required Quantity (Rounded)**

`= ROUND(Expected_Lost_Sales, 0)`

### d. **Priority Scoring**

`=IF(AND(Expected_Lost_Sales >= 10, Risk = "At Risk", Current_Stock <= 15), "High",  IF(AND(Expected_Lost_Sales >= 5, OR(Risk = "At Risk", Current_Stock <= 5)), "Medium",  "Low"))`

### e. **Stock Alert Level**

`=IF(Current_Stock < (Daily_Demand * 3), "Likely OOS Soon", "Good")`

---

##  **5. Reporting and Decision Support**

- **Created final report** showing:
    
    - Branch
        
    - Product
        
    - Daily Demand
        
    - Expected 10-Day Demand
        
    - Current Stock
        
    - Expected Lost Sales
        
    - Risk Flag
        
    - Priority Level
        
    - Stock Alert Level
        
- **Pivot Table for Visual Summary**:
    
    - Product vs. Quantity Sold vs. Required Quantity
        
- **Interactive Filters**:
    
    - Risk Level
        
    - Priority
        
    - Branch Name
        

---

##  **Outcome**

The final dashboard/report provides:

- A **quick view** of which products and branches are **at risk**.
    
- **Actionable priority levels** to decide where to send stock **urgently**.
    
- A clear path for **inventory reallocation** or emergency purchase planning.
