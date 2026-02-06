import random

#initialize environment

rooms={
    'A':random.choice(['Dirty','Clean']),
    'B':random.choice(['Dirty','Clean'])
}

agent_location=random.choice(['A','B'])

def simple_reflex_agent(location,status):
    if status=='Dirty':
        return 'Clean'
    
    elif location=='A':
        return 'Move Right'
    
    else:
        return 'Move Left'
    
print("Initial Environment Status:",rooms)
print("Initial Agent Location",agent_location)
print("-"*40)

for step in range(5):
    current_status=rooms[agent_location]
    action=simple_reflex_agent(agent_location,current_status)
    
    print(f"step{step+1}:Agent at Rooms{agent_location},Status={current_status}")
    print("Action:",action)
    
    
    if action=='Clean':
        rooms[agent_location]='Clean'
    elif action=='Move Right':
        agent_location='B'
    elif action=='Move Left':
        agent_location='A'
        
    print("Updated Environment:",rooms)
    print("-"*40)   
                 

