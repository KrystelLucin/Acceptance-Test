class Task:
    def __init__(self, name, description='', status='Pending', priority='Medium'):
        self.name = name
        self.description = description
        self.status = status
        self.priority = priority

    def __str__(self):
        return f"{self.name} - {self.description} [{self.status}, {self.priority}]"

    def mark_as_completed(self):
        self.status = 'Completed'

    def update(self, name=None, description=None):
        if name:
            self.name = name
        if description:
            self.description = description

    def update_priority(self, new_priority):
        self.priority = new_priority

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def list_tasks(self):
        for task in self.tasks:
            print(task)

    def mark_task_as_completed(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                task.mark_as_completed()
                return True
        return False

    def update_task(self, old_name, new_name=None, new_description=None):
        for task in self.tasks:
            if task.name == old_name:
                task.update(name=new_name, description=new_description)
                return True
        return False

    def change_task_priority(self, task_name, new_priority):
        for task in self.tasks:
            if task.name == task_name:
                task.update_priority(new_priority)
                return True
        return False

    def clear_all_tasks(self):
        self.tasks.clear()
def add_task_ui(task_manager):
    name = input("Ingrese el nombre de la tarea: ")
    description = input("Ingrese una descripción de la tarea (opcional): ")
    priority = input("Ingrese la prioridad de la tarea (Alta/Media/Baja): ")
    task = Task(name, description, priority=priority)
    task_manager.add_task(task)
    print("Tarea agregada.")

def list_tasks_ui(task_manager):
    print("\nLista de Tareas:")
    task_manager.list_tasks()

def mark_task_as_completed_ui(task_manager):
    task_name = input("Ingrese el nombre de la tarea a marcar como completada: ")
    if task_manager.mark_task_as_completed(task_name):
        print(f"Tarea '{task_name}' marcada como completada.")
    else:
        print("Tarea no encontrada.")

def update_task_ui(task_manager):
    old_name = input("Ingrese el nombre de la tarea a modificar: ")
    new_name = input("Ingrese el nuevo nombre de la tarea (deje en blanco para no cambiar): ")
    new_description = input("Ingrese la nueva descripción de la tarea (deje en blanco para no cambiar): ")

    if task_manager.update_task(old_name, new_name=new_name if new_name else None, new_description=new_description if new_description else None):
        print("Tarea actualizada con éxito.")
    else:
        print("Tarea no encontrada.")

def change_task_priority_ui(task_manager):
    task_name = input("Ingrese el nombre de la tarea para cambiar la prioridad: ")
    new_priority = input("Ingrese la nueva prioridad de la tarea (Alta/Media/Baja): ")

    if task_manager.change_task_priority(task_name, new_priority):
        print(f"Prioridad de la tarea '{task_name}' actualizada a {new_priority}.")
    else:
        print("Tarea no encontrada.")

def clear_all_tasks_ui(task_manager):
    confirmation = input("¿Está seguro de que desea limpiar todas las tareas? (s/n): ")
    if confirmation.lower() == 's':
        task_manager.clear_all_tasks()
        print("Todas las tareas han sido eliminadas.")
    else:
        print("Operación cancelada.")

def main():
    task_manager = TaskManager()

    while True:
        print("\n--- Administrador de Tareas ---")
        print("1. Agregar tarea")
        print("2. Listar tareas")
        print("3. Marcar tarea como completada")
        print("4. Modificar una tarea existente")
        print("5. Cambiar la prioridad de una tarea")
        print("6. Limpiar toda la lista de tareas")
        print("7. Salir")
        choice = input("Ingrese su opción: ")

        if choice == '1':
            add_task_ui(task_manager)
        elif choice == '2':
            list_tasks_ui(task_manager)
        elif choice == '3':
            mark_task_as_completed_ui(task_manager)
        elif choice == '4':
            update_task_ui(task_manager)
        elif choice == '5':
            change_task_priority_ui(task_manager)
        elif choice == '6':
            clear_all_tasks_ui(task_manager)
        elif choice == '7':
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
