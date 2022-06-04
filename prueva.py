class note:
    def __init__(self):
        self.note = "nota"
        
    def __str__(self):
        return f"nueva {self.note}"
    
    
obj=note()
print(obj)