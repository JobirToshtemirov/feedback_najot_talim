class Number:
    def __init__(self,num1 , num2):
        self.num1 = num1
        self.num2 = num2

    def qoshish(self):
            return f"{self.num1 + self.num2}"
    

result = Number (10, 20)
print(result.qoshish())
