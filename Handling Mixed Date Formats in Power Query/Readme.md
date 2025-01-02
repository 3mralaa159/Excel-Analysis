# Overview
This project provides an automated solution for handling mixed date formats in Power Query. 
Whether your data contains valid dates, inconsistent formats (DD/MM/YYYY, MM-DD-YYYY), or invalid values, this formula ensures:

  - Standardized date parsing.
  - Retention of invalid entries for manual review.
  - Seamless automation for future datasets.

If you’ve ever struggled with converting date columns due to formatting issues, this guide is for you!

## Situation
While working on a sales dataset, I encountered a recurring issue: the date column contained inconsistent formats. Some entries were valid Date types, others were strings in various formats, and a few were invalid. Attempting to convert the column to a Date type in Power Query led to errors, making it difficult to process the data efficiently.
