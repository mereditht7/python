
class students: 
    def __init__(self, names, grades):
        self.names = names
        self.grades= grades
    
    def add_grade(self, newgrade):
        self.grades.append(newgrade)

    def get_average (self):
        return(sum(self.grades)/len(self.grades))

    def get_grades (self):
        print(self.grades)

grades = [50, 99, 98, 98, 100]
student1 = students("Alice", grades)
student1.add_grade(50)

print(student1.get_grades())