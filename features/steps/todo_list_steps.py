from behave import given, when, then
from todo_list import TaskManager, Task
from io import StringIO
import sys

@given('the todo list is empty')
def step_impl(context):
    # Crear una nueva instancia de TaskManager
    context.manager = TaskManager()

@when('I add a task "{task_name}"')
def step_impl(context, task_name):
    # Crear y agregar una nueva tarea
    task = Task(task_name)
    context.manager.add_task(task)

@then('the todo list should contain "{task_name}"')
def step_impl(context, task_name):
    # Verificar si la tarea está en la lista
    tasks = [task.name for task in context.manager.tasks]
    assert task_name in tasks

@given('the todo list has the following tasks')
def step_impl(context):
    context.manager = TaskManager()
    for row in context.table:
        task = Task(row['Task'])
        context.manager.add_task(task)

@when('I list all tasks')
def step_impl(context):
    captured_output = StringIO()
    sys.stdout = captured_output
    context.manager.list_tasks()
    sys.stdout = sys.__stdout__
    context.captured_output = captured_output.getvalue()

@then('the output should contain "{tasks}"')
def step_impl(context, tasks):
    expected_outputs = tasks.split(" and ")
    for expected_output in expected_outputs:
        assert expected_output in context.captured_output

@given('the todo list contains the following tasks with status')
def step_impl(context):
    context.manager = TaskManager()
    for row in context.table:
        task = Task(row['Task'], status=row.get('Status', 'Pending'))
        context.manager.add_task(task)

@when('I mark the task "{task_name}" as completed')
def step_impl(context, task_name):
    context.manager.mark_task_as_completed(task_name)

@then('the task "{task_name}" should have the status "{status}"')
def step_impl(context, task_name, status):
    task = next((task for task in context.manager.tasks if task.name == task_name), None)
    assert task is not None and task.status == status

@given('the todo list contains tasks')
def step_impl(context):
    context.manager = TaskManager()
    for row in context.table:
        task = Task(row['Task'])
        context.manager.add_task(task)

@when('I clear the todo list')
def step_impl(context):
    context.manager.clear_all_tasks()

@then('the todo list should be empty')
def step_impl(context):
    assert len(context.manager.tasks) == 0

@given('the todo list contains the following tasks with descriptions')
def step_impl(context):
    context.manager = TaskManager()
    for row in context.table:
        task = Task(row['Task'], description=row.get('Description', ''))
        context.manager.add_task(task)

@when('I update the task "{task_name}" with description "{new_description}"')
def step_impl(context, task_name, new_description):
    context.manager.update_task(task_name, new_description=new_description)

@then('the task "{task_name}" should have the description "{description}"')
def step_impl(context, task_name, description):
    task = next((task for task in context.manager.tasks if task.name == task_name), None)
    assert task is not None and task.description == description

@given('the todo list contains the following tasks')
def step_impl(context):
    context.manager = TaskManager()
    for row in context.table:
        task = Task(row['Task'], priority=row.get('Priority', 'Medium'))
        context.manager.add_task(task)

@when('I change the priority of the task "{task_name}" to "{new_priority}"')
def step_impl(context, task_name, new_priority):
    context.manager.change_task_priority(task_name, new_priority)

@then('the task "{task_name}" should have the priority "{priority}"')
def step_impl(context, task_name, priority):
    task = next((task for task in context.manager.tasks if task.name == task_name), None)
    assert task is not None and task.priority == priority