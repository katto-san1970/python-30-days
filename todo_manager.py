import json

FILENAME = "task.json"

def load_tasks():
    try:
        with open(FILENAME, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return[]
    
def save_tasks(tasks):
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=4)
        
def add_task(tasks):
    name = input("Название задачи: ")
    task = {
        "name": name,
        "done": False
    }
    tasks.append(task)
    save_tasks(tasks)
    print("Задача добавлена!")

def show_tasks(tasks):
    if len(tasks) == 0:
        print("Задач нет!")
        return
    print("\n" + "=" * 30)
    for i, task in enumerate(tasks):
        status = "DONE!" if task["done"] else "X"
        print(f"{i+1}. {status} {task['name']}")
    print("=" * 30)

def complete_task(tasks):
    show_tasks(tasks)
    num = int(input("Номер выполненной задачи: ")) - 1
    tasks[num]["done"] = True
    save_tasks(tasks)
    print("Отмечено как выполнено!")

def delete_task(tasks):
    show_tasks(tasks)
    num = int(input("Номер задачи для удаления: ")) - 1
    tasks.pop(num)
    save_tasks(tasks)
    print("Задача удалена!")

tasks = load_tasks()

while True:
    print("\n" + "=" * 30)
    print("TO-DO МЕНЕДЖЕР")
    print("=" * 30)
    print("1 - Добавить задачу")
    print("2 - Показать задачи")
    print("3 - Отметить выполненное")
    print("4 - Удалить задачу")
    print("5 - Выйти")
    print("=" * 30)

    vibor = input("Выбери: ")

    if vibor == "1":
        add_task(tasks)
    elif vibor == "2":
        show_tasks(tasks)
    elif vibor == "3":
        complete_task(tasks)
    elif vibor == "4":
        delete_task(tasks)
    elif vibor == "5":
        print("Пока!")
        break
    else:
        print("Неверный выбор!")
    