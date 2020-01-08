# Report-rank

## Requirements

- Python>=3.5
- networkx>=2.3

## How to use

1. Generate data from submitted papers and save as _./data/data.csv_

```
7300001, 7300003
7300002, 7300001, 7300003
7300003
7300004, 7300001
7300005, 7300001
```
The first row is student ID, and the followings are referenced student IDs.

2. Execute main.py
```
python main.py
```
