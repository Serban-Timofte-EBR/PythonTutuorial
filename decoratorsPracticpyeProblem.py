 #Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:

#Create a decorator to check the time spent to performe a task (a function)

from time import time

user1 = {
    'name': 'Sorna',
    'valid': True #changing this will either run or not run the message_friends function.
}

def authenticated(fn):
  def wrapper(*args, **kawrgs):
    if args[0]['valid']:
      return fn(*args, **kawrgs)
  return wrapper

def performance(fn):
  def wrapper(*args, **kawrgs):
    t1 = time()
    result = fn(*args, **kawrgs)
    t2 = time()
    print(f"This task took {t2 - t1} seconds!")
    return result
  return wrapper

@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)

@performance
def longTimeTask():
  for i in range(100):
    i*5

longTimeTask()
