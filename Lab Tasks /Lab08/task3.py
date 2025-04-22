from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

model = BayesianNetwork([
    ('Disease', 'Fever'), ('Disease', 'Cough'),
    ('Disease', 'Fatigue'), ('Disease', 'Chills')
])

cpd_disease = TabularCPD('Disease', 2, [[0.3], [0.7]], state_names={'Disease': ['Flu', 'Cold']})

cpd_fever = TabularCPD('Fever', 2, [[0.9, 0.5], [0.1, 0.5]], evidence=['Disease'], evidence_card=[2], state_names={'Fever': ['Yes', 'No'], 'Disease': ['Flu', 'Cold']})
cpd_cough = TabularCPD('Cough', 2, [[0.8, 0.6], [0.2, 0.4]], evidence=['Disease'], evidence_card=[2], state_names={'Cough': ['Yes', 'No'], 'Disease': ['Flu', 'Cold']})
cpd_fatigue = TabularCPD('Fatigue', 2, [[0.7, 0.3], [0.3, 0.7]], evidence=['Disease'], evidence_card=[2], state_names={'Fatigue': ['Yes', 'No'], 'Disease': ['Flu', 'Cold']})
cpd_chills = TabularCPD('Chills', 2, [[0.6, 0.4], [0.4, 0.6]], evidence=['Disease'], evidence_card=[2], state_names={'Chills': ['Yes', 'No'], 'Disease': ['Flu', 'Cold']})

model.add_cpds(cpd_disease, cpd_fever, cpd_cough, cpd_fatigue, cpd_chills)
inference = VariableElimination(model)

res1 = inference.query(variables=['Disease'], evidence={'Fever': 'Yes', 'Cough': 'Yes'})
print(res1)


res2 = inference.query(variables=['Disease'], evidence={'Fever': 'Yes', 'Cough': 'Yes', 'Chills': 'Yes'})
print(res2)

res3 = inference.query(variables=['Fatigue'], evidence={'Disease': 'Flu'})
print(res3)
