from bayes import BayesModel

if __name__ == "__main__":
    # construct the Bayesian Network model
    model = BayesModel.given([
        {'variable': 'Rain', 'values': [[0.8], [0.2]]},
        {'variable': 'Sprinkler', 'values': [[0.99, 0.6], [0.01, 0.4]], 'evidences': ['Rain']},
        {'variable': 'GrassWet', 'values': [[0.9, 0.1, 0.1, 0.01], [0.1, 0.9, 0.9, 0.99]], 'evidences': ['Rain', 'Sprinkler']}
    ])

    # perform inference on the Bayesian Network
    result = model\
        .when(variables = ['GrassWet'], evidences = {'Rain': 1})\
        .then()
    print(result)