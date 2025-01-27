import random

class Environment:
   def __init__(self):
     self.state = random.choice(['Dirty', 'Clean'])
   
   def get_percept(self):
        return self.state
    
   def clean_room(self):
        self.state = 'Clean'

   def toggle_state(self):
        self.state = random.choice(['Dirty', 'Clean'])


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
        # Before the agent acts, change the environment's state
        environment.toggle_state()

        percept = environment.get_percept()
        action = agent.act(percept)
        print(f"Step {step + 1}: Percept - {percept}, Action - {action}")
        if percept == 'Dirty':
           environment.clean_room()

agent = SimpleReflexAgent()
environment = Environment()  
run_agent(agent, environment, 5)
