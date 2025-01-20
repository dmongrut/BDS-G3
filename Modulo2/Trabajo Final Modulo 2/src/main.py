from prefect import flow
from tasks.task_extract_linkedin import task_extract_linkedin
from tasks.task_load_linkedin import task_load_linkedin

@flow(name="ETL DE OFERTAS LABORALES PARA LINKEDIN")
def main_flow():
    ofertas = task_extract_linkedin()
    task_load_linkedin(ofertas)

if __name__ == "__main__":
    main_flow()
