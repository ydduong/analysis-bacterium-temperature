Project structure：
```bash
analysis-bacterium-temperature/
|-- analysis/  # Python project
|   |-- __init__.py
|   |-- thermo.py
|
|-- data/      # excel file dir
|  |-- uniprot-had+family+phosphatase.xlsx
|
|-- readme.md
```

python package
```bash
pip install openpyxl  # working with excel table
pip install lxml      # when use big data
pip install tqdm      # process bar
```