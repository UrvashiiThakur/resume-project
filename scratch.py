class AgeError(Exception):

     def __init__(self, message):
          self.msg = message
          pass


def validate_age(age:int):
     if age < 0:
          raise AgeError("Too young to live")
     elif age > 200:
          raise AgeError('Too old to live')
     else:
          print("What's the point?")

while True:
    try:
        age = int(input("Enter age\n"))
        validate_age(age)
    except AgeError as e:
        print(e)