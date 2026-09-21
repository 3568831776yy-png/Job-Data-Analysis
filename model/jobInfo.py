class JobInfo:
    def __init__(self, job_title, job_salary, job_education, job_experience,
                 job_type, company_name, company_type, personnel_size,
                 work_location, platform, collect_time, clean_status):
        self.t_job_title = job_title
        self.t_job_salary = job_salary
        self.t_job_education = job_education
        self.t_job_experience = job_experience
        self.t_job_type = job_type
        self.t_company_name = company_name
        self.t_company_type = company_type
        self.t_personnel_size = personnel_size
        self.t_work_location = work_location
        self.t_platform = platform
        self.t_collect_time = collect_time
        self.t_clean_status = clean_status
    def __str__(self):
        return (f"Job Title: {self.t_job_title}, Salary: {self.t_job_salary}, "
                f"Education: {self.t_job_education}, Experience: "
                f"{self.t_job_experience}, "
                f"Type: {self.t_job_type}, Company: {self.t_company_name}, "
                f"Company Type: {self.t_company_type}, Size: {self.t_personnel_size}, "
                f"Location: {self.t_work_location}, Platform: {self.t_platform}, "
                f"Collect Time: {self.t_collect_time}, Clean Status: "
                f"{self.t_clean_status}")