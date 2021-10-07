Project structure：
```bash
analysis-bacterium-temperature/
|-- analysis/  # Python project
|   |-- __init__.py
|   |-- thermo.py
|   |-- other
|
|-- data/      # excel file dir
|  |-- testdata.xlsx
|
|-- readme.md
```

大致流程:
- 将uniprot-had+family+phosphatase.xlsx Organism列中含thermo关键字的行写入：uniprot-had+family+phosphatase+is-thermo.xlsx；不含thermo关键字的行数据保存到uniprot-had+family+phosphatase+no-thermo.xlsx
- 将uniprot-had+family+phosphatase+no-thermo.xlsx Organism列进行数据清洗：只保留种名属名(最多两个单词)，之后将结果保存到bacterium.xlsx中
- 将bacterium.xlsx中菌的名字到网址上进行查询，查到有相关结果后，跳转到详细界面寻找温度信息，并将相关信息存储到temperature.csv文件中
- 根据temperature.csv中的信息，存入Sqlite数据库中，
- 最后将uniprot-had+family+phosphatase.xlsx中数据，根据关键字区分的同时进行查数据库
- 根据查询结果，将数据写入：uniprot-had+family+phosphatase+thermo.xlsx 和 result.xlsx


python package
```bash
pip install openpyxl  # working with excel table
pip install lxml      # when use big data
pip install tqdm      # process bar
pip install requests
```