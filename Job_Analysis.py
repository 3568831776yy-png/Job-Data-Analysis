import pandas as pd
import pymysql
import matplotlib.pyplot as plt
import seaborn as sns
import re

# 1. 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 2. 从数据库读取数据
conn = pymysql.connect(host="localhost", user="root", password="123456", database="job_info")
df = pd.read_sql("SELECT * FROM job_base", conn)
conn.close()

print(f"成功读取 {len(df)} 条数据！")

# 3. 数据清洗：把“15-25K”变成“20”（取平均值）
def parse_salary(salary_str):
    try:
        nums = re.findall(r'\d+', salary_str)
        if len(nums) >= 2:
            return (int(nums[0]) + int(nums[1])) / 2
        return int(nums[0])
    except:
        return 0

df['avg_salary'] = df['t_job_salary'].apply(parse_salary)

# 4. 画图：各岗位薪资分布（箱线图）
plt.figure(figsize=(12, 6))
sns.boxplot(x='t_job_type', y='avg_salary', data=df)
plt.title('不同岗位类型的薪资分布（单位：K）')
plt.xticks(rotation=45)
plt.show()

# 5. 画图：学历要求与平均薪资（柱状图）
plt.figure(figsize=(8, 5))
sns.barplot(x='t_job_education', y='avg_salary', data=df, estimator='mean')
plt.title('不同学历要求的平均薪资')
plt.show()