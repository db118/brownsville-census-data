[![Build Status](https://travis-ci.org/darrylbalderas/brownsville-census-data.svg?branch=master)](https://travis-ci.org/darrylbalderas/brownsville-census-data)

![census bureau](https://upload.wikimedia.org/wikipedia/commons/1/16/U.S._Census_Bureau_logo_post-2011.png)

Data is scraped from the [United States Census Bureau](https://www.census.gov)


## Prerequisites

```
$: brew install python3

$: pip3 install virtualenv

$: git clone git@github.com:darrylbalderas/brownsville-census-data.git

$: cd brownsville-census-data

$: python3 -m venv ./venv

$: source venv/bin/activate  

$: pip install -r requirements.txt
```

To stop python virtual environment 

`$: deactivate`

To freeze your python dependencies

`$: pip freeze > requirements.txt`



## Example of the data being scraped and formated in a csv 
Categories | Brownsville, TX | United States
---------- | --------------- | -------------
Population estimates, July 1, 2017,  (V2017) | NA | 325,719,178 
Population estimates, July 1, 2016,  (V2016) | 183,823 | 323,127,513 
Population estimates base, April 1, 2010,  (V2016) | 175,030 | 308,758,105
Population estimates base, April 1, 2010,  (V2017) | NA | 308,758,105
Population, percent change - April 1, 2010 (estimates base) to July 1, 2017,  (V2017) | NA | 5.5%
Population, percent change - April 1, 2010 (estimates base) to July 1, 2016,  (V2016) | 5.0% | 4.7%
Population, Census, April 1, 2010 | 175,023 | 308,745,538
Persons under 5 years, percent, July 1, 2016,  (V2016) | X | 6.2%
Persons under 5 years, percent, April 1, 2010 | 9.0% | 6.5%


## Value Flags that are in graph
* **D**  - Suppressed to avoid disclosure of confidential information
* **F**  - Fewer than 25 firms
* **FN** - Footnote on this item in place of data
* **NA** - Not available
* **S**  - Suppressed; does not meet publication standards
* **X**  - Not applicable
* **Z**  - Value greater than zero but less than half unit of measure shown
