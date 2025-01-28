from typing import List, Dict, Any
from functools import wraps
import warnings
warnings.filterwarnings("ignore")

from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

class BayesItem:
    def __init__(self):
        self.variables = []
        self.evidences = {}
        self.cpd = None

    def when(self, variables: List[str] | str, evidences: Dict[str, Any] | List[str]):
        if isinstance(variables, str):
            variables = [variables]
        self.variables = variables
        if isinstance(evidences, list):
            evidences = {k: None for k in evidences}
        self.evidences = evidences
        return self
    
    def then(self, cpd):
        self.cpd = cpd
        return self
    
    def __str__(self) -> str:
        probability_str = ', '.join(self.variables)
        if self.evidences:
            evidence_str = ', '.join([f"{k}={v}" if v is not None else k for k, v in self.evidences.items()])
            probability_str += f" | {evidence_str}"
        probability_str = f"P({probability_str})"
        if self.cpd is not None:
            probability_str += f" \n{self.cpd}"
        return f"{probability_str}\n"

def _require_valid_model(func):
    """
    Decorator to ensure the model is valid before performing inference.
    """
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        assert self.model.check_model(), "Model is not valid."
        return func(self, *args, **kwargs)
    return wrapper

class BayesModelInstance:
    """
    Bayesian Network model instance.
    """
    def __init__(self, nodes, edges, model):
        self.nodes = nodes
        self.edges = edges
        self.model = model
        is_valid = model.check_model()
        if not is_valid:
            raise AssertionError("Model is not valid.")
        self._bayes_item = BayesItem()

    def when(self, variables: List[str], evidences: Dict[str, Any] = None):
        """
        Set the variables for the Bayesian Network.
        """
        self._bayes_item.when(variables, evidences)
        return self

    @_require_valid_model
    def then(self) -> BayesItem:
        """
        Perform inference on the Bayesian Network.
        """
        evidences = self._bayes_item.evidences
        variables = self._bayes_item.variables
        inference = VariableElimination(self.model)
        result = inference.query(variables=variables, evidence=evidences)
        self._bayes_item.then(result)
        return self._bayes_item
    
class BayesModel:
    """
    Bayesian Network model.
    """
    @staticmethod
    def given(probs: List[Dict[str, Any]]) -> BayesModelInstance:
        """
        Initialize the Bayesian Network model.
        """
        nodes, edges, cpds = {}, [], []
        for prob in probs:
            variable = prob['variable']
            values = prob['values']
            evidences = prob.get('evidences', [])
            nodes[variable] = list(range(len(values)))
            edges += [(e, variable) for e in evidences]
            cpds += [TabularCPD(
                variable=variable,
                variable_card=len(nodes[variable]),
                values=values,
                evidence=evidences,
                evidence_card=[len(nodes[e]) for e in evidences]
            )]

        model = BayesianNetwork(edges)
        model.add_cpds(*cpds)
        return BayesModelInstance(nodes, edges, model)