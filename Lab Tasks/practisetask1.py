import random

class Environment:
   def __init__(self):
     self.state = random.choice(['Dirty', 'Clean']) 
     '''using random function we will make the random choice happen'''
   
   def get_percept(self):
        return self.state
    
   def clean_room(self):
        self.state = 'Clean'


class SimpleReflexAgent:
  def __init__(self):
    pass
  
  def act(self, percept):
    if percept == 'Dirty':
      return 'Clean the room'
    else:
      return 'Room is already clean'
  
def run_agent(agent, environment, steps):
    for step in range(steps):
        percept = environment.get_percept()
        action = agent.act(percept)
        print(f"Step {step + 1}: Percept - {percept}, Action -{action}")
        if percept == 'Dirty':
           environment.clean_room()

agent = SimpleReflexAgent()
environment = Environment() 
run_agent(agent, environment, 3)
