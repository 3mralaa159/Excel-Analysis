## **Overview**

This project showcases a robust approach to handling null values in a dataset using Excel and Power Query. The dataset contains transactional data with columns like `Date`, `Region`, `Product`, `Category`, `Price`, `Units Sold`, `Sales Revenue`, and others. The process focuses on automating data cleaning to ensure consistency and reliability for future updates.
The process focuses on automating data cleaning to ensure consistency and reliability for future updates.

This project demonstrates the power of Excel and Power Query in automating data cleaning for real-world scenarios. By combining advanced transformations and logic-based replacements, it ensures data quality, reliability, and readiness for analysis.

---

### **Situation**

A dataset with null values across multiple columns caused inconsistencies and posed challenges for accurate reporting and analytics. The columns affected included `Date`, `Region`, `Product`, `Category`, `Price`, `Units Sold`, and `Sales Revenue`. Without proper cleansing, these gaps would hinder the generation of meaningful insights.

---

### **Task**

- Develop an automated process to handle null values across all columns.
- Apply logic-based transformations to infer missing data.
- Ensure a clean, updated dataset ready for analysis and reporting.
- Create a solution that can adapt to future data updates seamlessly.

---

### **Actions Taken**

1. **Handling Nulls in the `Date` Column**
    
    - Used the `Fill Down` feature to propagate values from the previous row, ensuring no gaps in the date column.
2. **Replacing Nulls in `Region`**
    
    - Replaced null values with a default placeholder.
3. **Resolving Nulls in `Price`**
    
    - Created a grouped table with the product name and maximum price.
    - Merged this grouped table back into the original dataset to replace nulls with the maximum price per product.
    - Removed the old `Price` column.
4. **Fixing Nulls in `Product`**
    
    - Replaced null values with a temporary placeholder (`0`).
    - Used a custom **M Query** to infer the product name based on a combination of `Category` and `Price`:
        
      ```
      Table.AddColumn(#"Replaced Value1", "Custom", each if [Product] = "0" or [Product] = null then
      if [Category] = "Others" and [Price] = 80 then "Widget D"    
      else if [Category] = "Appliances" and [Price] = 60 then "Gadget A"    
      else if [Category] = "Appliances" and [Price] = 75 then "Gadget B"   
       else if [Category] = "Electronics" and [Price] = 50 then "Widget A"    else [Product]  else [Product])`
      ```
 
5. **Fixing Nulls in `Category`**
    
    - Added a logic-based column to infer `Category` from `Product` using:
        
      ```
        Table.AddColumn(#"Renamed Columns1", "Custom", each if Text.Contains([Product], "Gadget") then "Appliances"  
        else if Text.Contains([Product], "Widget") then "Electronics"  else "Others")`
      ```        
6. **Handling Nulls in `Units Sold` and `Sales Revenue`**
    
    - Added a custom column to calculate missing values dynamically:
        
        - If `Units Sold` is null: Compute it as `Sales Revenue ÷ Price`.
        - If `Sales Revenue` is null: Compute it as `Units Sold × Price.
     
      ```
       Table.AddColumn(#"Renamed Columns2", "Ref", each if [Units Sold] = null then    Text.From(Number.Round([Sales Revenue] / [Price], 2))  else if [Sales Revenue] = null then    Text.From(Number.Round([Price] * [Units Sold], 2))  else    Text.From([Units Sold]))`
      ```  
    - Replaced the nulls in `Units Sold` and `Sales Revenue` using the calculated values:
        
      
        ```
        Table.ReplaceValue(#"Added Custom2", null, each [Ref], Replacer.ReplaceValue, {"Units Sold"})`
        ```
7. **Final Touches**
    
    - Applied data transformations such as trimming spaces and converting text to uppercase for consistency.
    - Ensured all columns are cleaned and ready for downstream reporting.
8. **Automation for Future Data Updates**
    
    - Saved the transformations as a Power Query query, enabling automatic null handling whenever new data is added.
  

### **Results**

- Successfully cleaned all null values across the dataset.
- Automated the data cleansing process, ensuring future datasets are handled seamlessly.
- Created a clean, updated table ready for integration into reporting dashboards.
- Improved the reliability of analytics and reporting by ensuring data consistency.
