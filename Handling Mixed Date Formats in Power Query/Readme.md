# Overview
This project provides an automated solution for handling mixed date formats in Power Query. 
Whether your data contains valid dates, inconsistent formats (DD/MM/YYYY, MM-DD-YYYY), or invalid values, this formula ensures:

  - Standardized date parsing.
  - Retention of invalid entries for manual review.
  - Seamless automation for future datasets.

If you’ve ever struggled with converting date columns due to formatting issues, this guide is for you!

## Situation
While working on a sales dataset, I encountered a recurring issue: the date column contained inconsistent formats. Some entries were valid Date types, others were strings in various formats, and a few were invalid. Attempting to convert the column to a Date type in Power Query led to errors, making it difficult to process the data efficiently.

## Task
- The goal was to:

  - Parse valid dates into a consistent format (MM/DD/YYYY).
  - Retain invalid entries for further inspection without losing data.
  - Automate the process for similar datasets in the future.
 
## Action
- Using Power Query’s try...otherwise and conditional logic, I created a formula that handles various scenarios:

  - Data Type Check: Ensures only Text values are processed for string-based transformations.
  - Mixed Format Handling: Recognizes delimiters like / and -, rearranging parts into a standard format.
  - Original Data Preservation: Invalid or unrecognized entries remain unchanged for manual review.
 
```powerquery

if Text.Contains([Ship Date], "/") or Text.Contains([Ship Date], "-") then
    let
        parts = Text.SplitAny([Ship Date], "/-"),
        swapped = if List.Count(parts) = 3 then
                    Date.FromText(parts{1} & "/" & parts{0} & "/" & parts{2})
                  else [Ship Date]
    in
        try swapped otherwise [Ship Date]
else
    [Ship Date]

```
