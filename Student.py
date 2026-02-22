class Student:
    # Constructor to initialize the student's name, age, and grades
    def __init__(self, name : str, age: int, grades: list[float]):
        self.name = name
        self.age = age
        self._grades = list(grades)
        self._validations()

    # method to calculate the average grade of the student
    def get_average_grade(self) -> float:
        if len(self._grades) == 0:
            return 0.0
        return sum(self._grades) / len(self._grades)
    
    # method to add a grade to the student's list of grades
    def add_grade(self, grade: float) -> None:
        if grade < 0 or grade > 100:
            raise ValueError("Grade must be between 0 and 100")
        
        self._grades.append(grade)

    # method to remove a grade from the student's list of grades
    def remove_grade(self, grade: float) -> None:
        if grade in self._grades:
            self._grades.remove(grade)
    
    # method to get the student's grades using property decorator to allow for copy not affecting initial grades list
    @property
    def grades(self) -> list[float]:
        return self._grades.copy()
    
    # return student's information as a string
    def __str__(self) -> str:
        return f"Student name={self.name}, age={self.age}, average={self.get_average_grade()}"
    
    def _validations(self) -> bool:
        if self.age < 0:
            raise ValueError("Age cannot be negative")
        
        for grade in self._grades:
            if grade < 0 or grade > 100:
                raise ValueError("Grades must be between 0 and 100")
            
    # method to sort grades in ascending order
    def sort_grades(self) -> None:
        self._grades.sort()

    # method to get the highest grade of the student
    def highest_grade(self) -> int:
        if not self.grades:
            return 0
        return max(self.grades)
    
    # method to get the lowest grade of the student
    def lowest_grade(self) -> int:
        if not self.grades:
            return 0
        return min(self.grades)