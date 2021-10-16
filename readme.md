python package
```bash
pip install openpyxl  # working with excel table
pip install lxml      # when use big data
pip install tqdm      # process bar
pip install requests
```

Project structure：
```bash
root/
|-- analysis-bacterium-temperature/  
|   |-- homology         # Python project
|   |   |-- __init__.py
|   |   |-- args.py      
|   |   |-- spiderFasta.py
|   |   |-- other
|   |-- temperature      # Python project
|   |   |-- __init__.py
|   |   |-- thermo.py
|   |   |-- other
|-- data/                # data dir
|  |-- testdata.xlsx
|-- readme.md
```

查询菌种的温度（temperature 项目）：

- 原始数据放在 /data/temperature 文件夹下
- 修改args.py文件，只需要修改变量source_xlsx，这是原始的带后缀的文件名
- 运行thermo.py文件，按源文件Organism列中是否含thermo关键字分成两个文件
- 运行bacterium.py文件，将不含thermo关键字的原始数据表格，对所有菌种名称进行清洗和去重，保存这些数据
- 运行spider.py文件，会根据菌种名称去网站查询相关信息，最后保存搜索链接、详细链接和温度信息
- 运行sqlite.py文件，跟据爬取的信息，建立数据库
- 运行query.py文件，将原始表格数据，逐条进行判别和查询，最后保存一份带温度信息的原始数据，和一份耐热菌的数据表（生长温度大于50或有thermo关键字）
- 
- 同样可以只运行main.py文件，代替上述流程

查询菌种的同源性:

- 原始数据放在 /data/homology 文件夹下
- 修改args.py文件，只需要修改变量source_xlsx_file，这是原始的带后缀的文件名
- 运行spiderFasta.py文件，根据原始数据(经过去重后)去下载Fasta序列，保存到 /data/homology/fasta文件夹下；同时会将下载的文件合并到all-fasta.txt文件中，放在/data/homology文件夹下
- 手动将all-fasta.txt文件上传到[https://www.genome.jp/tools-bin/clustalw](https://www.genome.jp/tools-bin/clustalw)，进行同源性查询，将查询结果页保存到/data/homology文件夹下（Ctrl+S，选择html格式）
- 运行preprocessingHtml.py文件，对网页数据进行处理（先筛选出必要数据），在对原始表格数据进行处理，生成结果文件
- 
- 关于检验结结果：
- 运行check-result-homology.py文件，会在/data/homology文件夹下生成一个这些数据的总的Fasta序列集文件，同样上传到[https://www.genome.jp/tools-bin/clustalw](https://www.genome.jp/tools-bin/clustalw)，进行同源性查询

