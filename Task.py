class Task:
    def __init__(self, task_id: int, title: str, description: str):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.completed = False

    def mark_complete(self) -> None:
        if self.completed:
            raise ValueError("Already Completed")

        self.completed = True

    def mark_incomplete(self) -> None:
        if not self.completed:
            raise ValueError("Task already Incomplete")
        
        self.completed = False

    def update_title(self, new_title: str) -> None:
        if not new_title:
            raise ValueError("Title cannot be empty")
    
        self.title = new_title

    def update_description(self, new_description: str) -> None:
        if not new_description:
            raise ValueError("Description cannot be empty")
        
        self.description = new_description

    def __str__(self) -> str:
        return(
            f"task_id: {self.task_id}, "
            f"title: {self.title}, "
            f"description={self.description}, "
            f"completed={self.completed}"
        )
    

    #Test Cases
if __name__ == "__main__":
    task1 = Task(1, "Task 1", "This is the first task")
    print(task1)

    task1.mark_complete()
    print(task1)

    task1.mark_incomplete()
    print(task1)

    task1.update_title("Updated Task 1")
    print(task1)

    task1.update_description("This is the updated description for the first task")
    print(task1)

    #test case 2
    task2 = Task(2, "Task 2", "This is the second task")
    print(task2)   

    task2.mark_complete()
    print(task2)

    task2.mark_incomplete()
    print(task2)

    task2.update_title("Updated Task 2")
    print(task2)

    task2.update_description("This is the updated description for the second task")
    print(task2)

    #test case 3
    task3 = Task(3, "Task 3", "This is the third task")
    print(task3)

    task3.mark_complete()
    print(task3)

    task3.mark_incomplete()
    print(task3)

    task3.update_title("Updated Task 3")
    print(task3)

    task3.update_description("This is the updated description for the third task")
    print(task3)
