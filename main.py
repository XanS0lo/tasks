from tasks import add_task, show_task
from storage import save_tasks
def main():
    tasks = []

    add_task(tasks, "Изучить модули")
    add_task(tasks, "Изучить ООП")

    show_task(tasks)
    save_tasks(tasks)
if __name__ == "__main__":
    main()
