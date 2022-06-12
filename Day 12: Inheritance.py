       
class Student(Person):
  
    
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
        

        
     
