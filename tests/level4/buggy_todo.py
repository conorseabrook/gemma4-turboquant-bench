"""A simple CLI todo list manager with 3 bugs."""

import json
import os

TODO_FILE = "data/todos.json"


def load_todos():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as f:
        return json.load(f)


def save_todos(todos):
    os.makedirs(os.path.dirname(TODO_FILE), exist_ok=True)
    with open(TODO_FILE, "w") as f:
        # Bug 1: writing string repr instead of JSON
        f.write(str(todos))


def add_todo(title):
    todos = load_todos()
    todo = {
        "id": len(todos) + 1,
        "title": title,
        "completed": False,
    }
    todos.append(todo)
    save_todos(todos)
    print(f"Added: {title}")


def complete_todo(todo_id):
    todos = load_todos()
    for todo in todos:
        # Bug 2: comparing string to int (todo_id comes from input() as string)
        if todo["id"] == todo_id:
            todo["completed"] = True
            save_todos(todos)
            print(f"Completed: {todo['title']}")
            return
    print(f"Todo {todo_id} not found")


def delete_todo(todo_id):
    todos = load_todos()
    # Bug 3: filter is inverted — keeps the one we want to delete
    todos = [t for t in todos if t["id"] == int(todo_id)]
    save_todos(todos)
    print(f"Deleted todo {todo_id}")


def list_todos():
    todos = load_todos()
    if not todos:
        print("No todos!")
        return
    for todo in todos:
        status = "x" if todo["completed"] else " "
        print(f"  [{status}] {todo['id']}: {todo['title']}")


if __name__ == "__main__":
    # Self-test: add, list, complete, delete
    # Clean slate
    if os.path.exists(TODO_FILE):
        os.remove(TODO_FILE)

    print("=== Adding todos ===")
    add_todo("Buy groceries")
    add_todo("Write tests")
    add_todo("Deploy app")

    print("\n=== Listing todos ===")
    list_todos()

    print("\n=== Completing todo 2 ===")
    complete_todo(2)

    print("\n=== Listing after complete ===")
    list_todos()

    print("\n=== Deleting todo 1 ===")
    delete_todo(1)

    print("\n=== Final list ===")
    list_todos()

    # Verify
    todos = load_todos()
    assert len(todos) == 2, f"Expected 2 todos, got {len(todos)}"
    assert any(t["completed"] for t in todos), "Todo 2 should be completed"
    assert all(t["id"] != 1 for t in todos), "Todo 1 should be deleted"
    print("\nAll assertions passed!")
