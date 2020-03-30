import sys

class fighter():
    
    def __init__(self,name,height,health):
        self.name=name
        self.height=height
        self.health=health
    
    def punch(self):
        print("{} threw a punch".format(self.name))    

    def kick(self):
        print("{} kicked".format(self.name))
    
    def jump(self):
        print("{} jumped".format(self.name))
    
    def crouch(self):
        print("{} crouched".format(self.name))

Chan=fighter("Chan",6,"good")    
Chan.kick()
Chan.punch()
Chan.jump()
Chan.crouch()
Chan.punch()
