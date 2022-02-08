

        
class Student(Person):
    #   Class Constructorsdfsdf
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def __init__(self,firstName, lastName, idNum , scores):

        self.firstName = firstName
        self.lastName = lastName
        self.idNum = idNum
        self.scores = scores
    
    def printPerson(self):
        print("Name: " + lastName + ", " + firstName)
        print("ID:", idNum)
    def calculate(self):
        m = len(scores)
        h = 0
        for i in range(m):
            h += scores[i]
        
        f = h // m
        if 90<= f <= 100:
            return "O"
        elif 80<= f <90:
            return "E"
        elif 70<= f < 80:
            return "A"
        elif 55<= f < 70:
            return "P"
        elif 40<= f < 55:
            return "D"
        elif f < 40:
            return "T"
        
