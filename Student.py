class Student:
    # Constructor to initialize the student's name, age, and grades
    def __init__(self, name : str, age: int, grades: list[float]):
        self.name = name
        self.age = age
        self.grades = grades

    # method to calculate the average grade of the student
    def get_average_grade(self) -> float:
        if len(self.grades) == 0:
            return 0.0
        return sum(self.grades) / len(self.grades)
    
    # method to add a grade to the student's list of grades
    def add_grade(self, grade: float) -> None:
        self.grades.append(grade)

    # method to remove a grade from the student's list of grades
    def remove_grade(self, grade: float) -> None:
        if grade in self.grades:
            self.grades.remove(grade)
    
    # method to get the student's grades using property decorator to allow for copy not affecting initial grades list
    @property
    def grades(self) -> list[float]:
        return self._grades.copy()
    
    # return student's information as a string
    def __str__(self) -> str:
        return f"Student name={self.name}, age={self.age}, average={self.get_average_grade()}"