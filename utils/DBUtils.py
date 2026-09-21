import pymysql
from pymysql import OperationalError

def create_connection(host_name, user_name, user_password, db_name):
    """建立连接的工具类"""
    connection = None
    try:
        connection = pymysql.connect(host=host_name, user=user_name, password=user_password, database=db_name)
        print("Connection to MySQL DB successful")
    except OperationalError as e:
        print("The error occurred", e)
    return connection

def batch_insert_job_info(conn, job_infos):
    """批量添加操作"""
    # 通过连接对象获取游标
    cursor = conn.cursor()
    sql = """
    INSERT INTO job_base (t_job_title, t_job_salary, t_job_education, t_job_experience,
    t_job_type, t_company_name, t_company_type, t_personnel_size, t_work_location,
    t_platform, t_collect_time, t_clean_status)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    data = [(job_info.t_job_title, job_info.t_job_salary, job_info.t_job_education,
             job_info.t_job_experience, job_info.t_job_type, job_info.t_company_name,
             job_info.t_company_type, job_info.t_personnel_size, job_info.t_work_location,
             job_info.t_platform, job_info.t_collect_time, job_info.t_clean_status) for job_info in job_infos]
    try:
        cursor.executemany(sql, data)
        conn.commit()
        print(f'{len(job_infos)} records inserted')
    except OperationalError as e:
        print("The error occurred", e)

def save_job_info_to_mysql(job_infos):
    """保存数据到mysql数据库"""
    host_name = "localhost"
    user_name = "root"
    user_password = "123456"
    db_name = "job_info"

    # 创建连接
    connection = create_connection(host_name, user_name, user_password, db_name)
    # 批量添加
    if connection:
        batch_insert_job_info(connection, job_infos)
        # 关闭资源
        connection.close()
if __name__ == '__main__':
    # 记得把密码换成你自己的！
    conn = create_connection("localhost", "root", "123456", "job_info")
    if conn:
        print("数据库连接测试成功！")
        conn.close()