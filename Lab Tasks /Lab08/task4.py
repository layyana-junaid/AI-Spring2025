import numpy as np

states = ['Sunny', 'Cloudy', 'Rainy']
transition_matrix = [
    [0.6, 0.3, 0.1], 
    [0.3, 0.4, 0.3], 
    [0.2, 0.3, 0.5],  
]

def simulate_weather(days, start_state):
    current = states.index(start_state)
    weather_sequence = [start_state]
    for _ in range(days - 1):
        current = np.random.choice([0, 1, 2], p=transition_matrix[current])
        weather_sequence.append(states[current])
    return weather_sequence

sim = simulate_weather(10, 'Sunny')
print("Weather for 10 days:", sim)
print("Rainy days:", sim.count('Rainy'))

rainy_counts = []
for _ in range(1000):
    sim = simulate_weather(10, 'Sunny')
    rainy_counts.append(sim.count('Rainy') >= 3)

prob_rainy_3plus = sum(rainy_counts) / 1000
print("P(at least 3 rainy days in 10):", prob_rainy_3plus)
