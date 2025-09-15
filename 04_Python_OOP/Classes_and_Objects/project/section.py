from task import Task
class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task):
        for task in self.tasks:
            if task == new_task:
                return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task{new_task.details()}"

    def complete_task(self, task_name):
        for task in self.tasks:
            if task == task_name:
                task.completed = True
                return f"Completed task {self.name}"

        return f"Could not find task with the name {self.name}"

    def clean_section(self):
        counter = 0
        for task in self.tasks:
            if task.completed:
                self.tasks.remove(task)
                counter += 1
        return f"Cleared {counter} tasks."

    def view_section(self):
        return f"Section {self.name}:\n{[f"{task.details()}" for task in self.tasks]}"


