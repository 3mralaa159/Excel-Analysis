# **Project Overview**  
This project focuses on automating the preparation of a Hijri calendar dataset in Excel and transforming it into actionable reminders for Google Calendar. The solution streamlines the process by handling data cleaning, text extraction, and advanced formatting using a mix of Excel formulas, VBA, and conditional formatting.

---

## **💡 Features**

1. **Preserving Hijri Text Values**:
    
    - A VBA script extracts and copies visible Hijri date text to maintain its integrity without altering underlying Gregorian data.
2. **Highlighting Key Dates**:
    
    - Conditional formatting identifies and highlights the 13th, 14th, and 15th of every Hijri month.
    - Additional highlights for Mondays and Thursdays to mark recommended fasting days.
3. **Data Transformation for Customization**:
    
    - Extracted Hijri days, months, and years for advanced filtering.
    - Combined text values for easy identification of day names and important dates.
4. **Google Calendar Integration**:
    
    - Prepared a clean dataset with all necessary columns for seamless import into Google Calendar as fasting reminders.
--- 

## **Situation**  
I worked on a project that involved preparing a dataset for Islamic Hijri calendar-related reminders. The dataset had two main columns:

1. A Gregorian calendar (generated using the `SEQUENCE` function).
2. The Hijri calendar equivalent (formatted dates).

However, preserving the original Hijri text values and preparing the data for reminders in Google Calendar required creative problem-solving and automation.

---

## **Task**  
The goal was to:

1. Extract and preserve Hijri date text values (since they differ from the underlying numerical values).
2. Automate highlighting specific days (e.g., 13th, 14th, and 15th of every Hijri month) and Mondays/Thursdays.
3. Transform the dataset for easy import into Google Calendar as reminders for fasting.

---

## **Actions**  
1️⃣ **Preserved Hijri Text Values**

- Wrote a VBA script to copy the visible Hijri text values from Column B (Hijri dates) to Column C without altering the underlying numerical data.

```

`Sub ExtractHijriTextForColumn()     Dim ws As Worksheet     
Dim sourceRange As Range     Dim targetRange As Range     Dim cell As Range      
' Set your worksheet     
Set ws = ThisWorkbook.Sheets("Sheet1")      
' Define the source and target ranges    
 Set sourceRange = ws.Columns("B")     
Set targetRange = ws.Columns("C")      
' Loop through each cell in the source range    

 For Each cell In sourceRange.Cells         If Not IsEmpty(cell) Then             
' Copy displayed text from source to target             
ws.Cells(cell.Row, targetRange.Column).Value = cell.Text        
 End If    
 Next cell 
End Sub`

```
2️⃣ **Highlighted Key Dates**

- Used `LEFT` to extract the Hijri day and applied conditional formatting to highlight the 13th, 14th, and 15th of each Hijri month.
- Filtered for Mondays and Thursdays to apply custom highlights.

3️⃣ **Enhanced Hijri Data for Filtering**

- Used `Text to Columns` to split Hijri text into day, month, and year values.
- Applied `TEXTJOIN` to create a column summarizing day and month names (e.g., "Monday, 13th Hijri").

4️⃣ **Prepared for Google Calendar**

- Filled the required columns for Google Calendar, including titles like "Fasting Reminder," ensuring proper format for import.

---

## **Result**

- A clean, well-organized dataset ready for direct import into Google Calendar.
- Automated processes for date preservation and highlighting, saving hours of manual effort.
- A functional calendar with fasting reminders for the entire year.
