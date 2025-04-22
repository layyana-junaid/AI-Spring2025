from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

model = BayesianNetwork([
    ('I', 'G'),
    ('S', 'G'),
    ('D', 'G'),
    ('G', 'P')
])

cpd_i = TabularCPD(
    variable='I', variable_card=2,
    values=[[0.7], [0.3]],
    state_names={'I': ['High', 'Low']}
)

cpd_s = TabularCPD(
    variable='S', variable_card=2,
    values=[[0.6], [0.4]],
    state_names={'S': ['Sufficient', 'Insufficient']}
)

cpd_d = TabularCPD(
    variable='D', variable_card=2,
    values=[[0.4], [0.6]],
    state_names={'D': ['Hard', 'Easy']}
)


cpd_g = TabularCPD(
    variable='G', variable_card=3,
    values=[
        [0.8, 0.6, 0.5, 0.3, 0.6, 0.4, 0.3, 0.1],  
        [0.15, 0.3, 0.3, 0.5, 0.3, 0.4, 0.4, 0.4],  
        [0.05, 0.1, 0.2, 0.2, 0.1, 0.2, 0.3, 0.5]   
    ],
    evidence=['I', 'S', 'D'],
    evidence_card=[2, 2, 2],
    state_names={
        'G': ['A', 'B', 'C'],
        'I': ['High', 'Low'],
        'S': ['Sufficient', 'Insufficient'],
        'D': ['Hard', 'Easy']
    }
)

cpd_p = TabularCPD(
    variable='P', variable_card=2,
    values=[
        [0.95, 0.8, 0.5],  
        [0.05, 0.2, 0.5]   
    ],
    evidence=['G'],
    evidence_card=[3],
    state_names={
        'P': ['Yes', 'No'],
        'G': ['A', 'B', 'C']
    }
)

model.add_cpds(cpd_i, cpd_s, cpd_d, cpd_g, cpd_p)

assert model.check_model()

infer = VariableElimination(model)

result1 = infer.query(variables=['P'], evidence={'S': 'Sufficient', 'D': 'Hard'})
print("\nProbability of passing given sufficient study hours and hard difficulty:")
print(result1)

result2 = infer.query(variables=['I'], evidence={'P': 'Yes'})
print("\nProbability of high intelligence given pass=yes:")
print(result2)
