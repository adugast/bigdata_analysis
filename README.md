# BDA  [![Language: Python](https://img.shields.io/badge/Language-python-brightgreen.svg)](https://en.wikipedia.org/wiki/Python_(programming_language))  [![Library: pandas](https://img.shields.io/badge/Library-pandas-brightgreen)](https://pandas.pydata.org/)  [![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg)](https://opensource.org/licenses/MIT)

## Introduction

## Program description

## Usage:

## How it works:

```
+-------------------------------+     +-------------------+     +-----------------------------------+  
| 1) DATA INPUT:                |     | 2) DATA ANALYSIS: |     | 3) DATA OUTPUT:                   |  
|                               |     |                   |     |                                   |  
|- excel files (.xls, .xlsx)    |     |- merging          |     |- excel files (.xls, .xlsx)        |  
|- comma-separated values (.csv)|     |- filters          |     |- comma-separated values (.csv)    |  
|- database (.sql, ...?)        |     |- ...              |     |- database (.sql, ...)             |  
|- ...                          |     |                   |     |- ...                              |
|                               |     |                   |     |                                   |  
+-------------------------------+     +-------------------+     +-----------------------------------+  
```

The program takes two json files as input file to set its configuration.

- data.json     : defines the data to take as input

- filter.json   : defines the filters to apply on the data set    
The key defines the column name and the value the regex used to parse the data.

1) data.json example:
```
{
   "data" : {
       "path" : [
           "samples/file_example_XLS_10.xls",
           "samples/file_example_XLS_50.xls",
           "samples/file_example_XLS_100.xls"
       ]
   }
}
```

2) filter.json example
```
{
    "filter": {
        "First Name": "[LGP]",
        "Country": "[F]",
        "Gender": "Male",
        "Age": 21
    }
}
```

The filter.json file describes every filters that need to be applied:   
- The key should correspond to a column name available   
- The value should describe a regex to will be used to filter the rows  

## More info:

* [Regular Expression Wikipedia](https://en.wikipedia.org/wiki/Regular_expression) - Introduction to regular expression
* [RegEx Tutorial](https://regexr.com/) - Learn, Build, & Test RegEx
* [pandas](https://pandas.pydata.org/) - Python Data Analysis Library
* [JSON w3school](https://www.w3schools.com/js/js_json_intro.asp) - JSON Introduction

## License:

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
