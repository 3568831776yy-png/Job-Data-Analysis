# 招聘数据采集与薪资可视化分析项目 (JobSpider)

## 项目背景
本项目为实训项目，旨在通过自动化手段获取招聘网站数据，存入 MySQL 数据库，并进行数据分析与可视化，以探究不同岗位、学历对薪资的影响。

## 技术栈
*   **数据采集**：Python (Selenium, undetected-chromedriver)
*   **数据存储**：MySQL, PyMySQL
*   **数据分析与可视化**：Pandas, Matplotlib, Seaborn
*   **IDE**：PyCharm

## 项目结构
```text
JobSpider/
├── model/
│   └── jobInfo.py          # 职位信息实体类
├── utils/
│   └── DBUtils.py          # 数据库连接与批量插入工具
├── data/                   # 存放城市、岗位类型的配置文本
├── mock_data.py            # 模拟数据生成与入库 (因反爬机制，采用模拟数据完成闭环)
├── Job_Analysis.py         # 数据读取、清洗与可视化分析
└── README.md
