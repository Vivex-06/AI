from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

model = BayesianNetwork([('Burglary', 'Alarm'), ('Earthquake', 'Alarm'), ('Alarm', 'David'), ('Alarm', 'Sophia')])

cpd_burglary = TabularCPD(variable='Burglary', variable_card=2, values=[[0.999], [0.001]])
cpd_earthquake = TabularCPD(variable='Earthquake', variable_card=2, values=[[0.998], [0.002]])
cpd_alarm = TabularCPD(variable='Alarm', variable_card=2, values=[[0.95, 0.94, 0.29, 0.001], [0.05, 0.06, 0.71, 0.999]], evidence=['Burglary', 'Earthquake'], evidence_card=[2,2])
cpd_david = TabularCPD(variable='David', variable_card=2, values=[[0.9, 0.05], [0.1, 0.95]], evidence=['Alarm'], evidence_card=[2])
cpd_sophia = TabularCPD(variable='Sophia', variable_card=2, values=[[0.7, 0.01], [0.3, 0.99]], evidence=['Alarm'], evidence_card=[2])

model.add_cpds(cpd_burglary, cpd_earthquake, cpd_alarm, cpd_david, cpd_sophia)

assert model.check_model()

inference = VariableElimination(model)

result = inference.query(variables=['Alarm'], evidence={'Burglary': 0, 'Earthquake': 0, 'David': 1, 'Sophia': 1})
print(result)

print("P(Alarm=1, Burglary=0, Earthquake=0, David=1, Sophia=1) =", result.values[1])
