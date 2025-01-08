## Overview

This farm dashboard was designed to efficiently manage inventory, sales, collections, and expenses while providing actionable insights through an interactive dashboard. The system integrates data analysis techniques using Excel formulas, Power Pivot, macros, and advanced features like date hierarchies and dynamic slicers.

## Key Features

### 1. **Inventory Management**

- **Items Sheet**: Maintains a master list of all items.
    
- **Inventory Stock Sheet**: Calculates the stock of each item dynamically by:
    
    - Subtracting sold quantities from collected quantities using:
        
        ```
        =SUMIF('Daily Collection'!C$1:C$10006,Inventory!A2,'Daily Collection'!D$1:D$10006)-SUMIF('Daily Sales'!C$1:C$10006,Inventory!A2,'Daily Sales'!D$1:D$10006)
        ```
        

### 2. **Daily Logs**

- **Daily Collection Sheet**:
    
    - Automatically generates a unique collection ID using:
        
        ```
        =LEFT(A7,1)&(VALUE(RIGHT(A7,LEN(A7)-1))+1)
        ```
        
- **Daily Sales Sheet**:
    
    - Includes additional columns to extract date components for use in Power Pivot’s data model.
        
    - Facilitates the creation of a date hierarchy for enhanced reporting.
        

### 3. **Input Sheet**

- Uses macros to automate data entry by:
    
    - Creating a new row.
        
    - Assigning a unique ID.
        
    - Copying, pasting, and clearing user inputs.
        
- Includes:
    
    - A calendar add-in for quick date selection.
        
    - Data validation to ensure item consistency with the Items Sheet.
        

### 4. **Expenses Sheet**

- Tracks detailed user expenses for better financial management.
    

### 5. **Dashboard**

- Features interactive buttons and charts:
    
    - **Daily Total Revenue Button**: Calculates total revenue for the previous day using:
        
        ```
        =SUMIF(B:B,TODAY()-1,D:D)
        ```
        
    - **Daily Item Tracker Button**: Tracks unique items sold/collected using:
        
        ```
        =COUNTA(UNIQUE(FILTER(C2:C100, (C2:C100<>"")*(B2:B100=TODAY()-1))))
        ```
        
    - **Today’s Date Button**: Displays the current date dynamically.
        
- **Charts**:
    
    - Revenue and sales by item.
        
    - Inventory and expenses bar chart.
        

### 6. **Power Pivot Integration**

- Combines and analyzes data across sheets.
    
- Includes a DAX column to merge month and year for slicer optimization:
    
    ```
    MonthYear = FORMAT([Date], "MMM YYYY")
    ```
    

