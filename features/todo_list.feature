Feature: Todo List Management
  As a user of the Todo List application
  I want to be able to manage my tasks efficiently
  So that I can keep track of my work and priorities

  Scenario: Add a task to the todo list
    Given the todo list is empty
    When I add a task "Buy groceries"
    Then the todo list should contain "Buy groceries"

  Scenario: List all tasks in the todo list
  Given the todo list has the following tasks
    | Task          |
    | Buy groceries |
    | Pay bills     |
  When I list all tasks
  Then the output should contain "Buy groceries -  [Pending, Medium] and Pay bills -  [Pending, Medium]"


  Scenario: Mark a task as completed
  Given the todo list contains the following tasks with status
      | Task          | Status  |
      | Buy groceries | Pending |
    When I mark the task "Buy groceries" as completed
    Then the task "Buy groceries" should have the status "Completed"

  Scenario: Clear the entire to-do list
    Given the todo list has the following tasks
      | Task          |
      | Buy groceries |
      | Pay bills     |
    When I clear the todo list
    Then the todo list should be empty

  Scenario: Update a task
  Given the todo list contains the following tasks with descriptions
      | Task          | Description         |
      | Buy groceries | Buy before weekend  |
    When I update the task "Buy groceries" with description "Buy before Friday"
    Then the task "Buy groceries" should have the description "Buy before Friday"

  Scenario: Prioritize a task
    Given the todo list contains the following tasks
      | Task          | Priority |
      | Buy groceries | Medium   |
      | Pay bills     | Low      |
    When I change the priority of the task "Pay bills" to "High"
    Then the task "Pay bills" should have the priority "High"

