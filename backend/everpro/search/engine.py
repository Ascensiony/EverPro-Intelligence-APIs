from .engines.amazon import amazon_search_by_query
from .engines.flipkart import flipkart_search_by_query

from multiprocessing import Process, Manager


def search(query: str):

    try:
        run_cpu_tasks_in_parallel(
            [amazon_search_by_query, flipkart_search_by_query], query
        )
    except Exception as e:
        print(e)
        print("\nEXCEPTION IN ENGINE !!\n")


def run_cpu_tasks_in_parallel(tasks, query):

    running_tasks = [Process(target=task, kwargs=dict(query=query)) for task in tasks]
    for running_task in running_tasks:
        running_task.start()
    for running_task in running_tasks:
        running_task.join()


# search("shoes")
