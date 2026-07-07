from user_model import Model
from validation import String,Float,Integer
class User(Model):
    name = String()
    age = Integer(min=18)
    balance = Float(default=0)
    

u1 = User(name="matin",age=20)

u1.balance = '3'

print(u1.to_dict())
