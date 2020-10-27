from todo_list.task import Task

class Section:

    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        tasks = [t for t in self.tasks if t.name == task_name]
        if tasks:
            task = tasks[0]
            task.completed = True
            return f"Completed task {task.name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        amount_of_removed_tasks = len([t for t in self.tasks if t.completed])
        self.tasks = [t for t in self.tasks if not t.completed]
        return f"Cleared {amount_of_removed_tasks} tasks."

    def view_section(self):
        section_line = [f"Section {self.name}:"]
        details_line = [t.details() for t in self.tasks]
        return '\n'.join(section_line + details_line) + '\n'