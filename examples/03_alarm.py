from bayes import BayesModel

if __name__ == "__main__":
    model = BayesModel.given([
        {'variable': 'B', 'values': [[0.99], [0.01]]},
        {'variable': 'E', 'values': [[0.999999], [0.000001]]},
        {'variable': 'R', 'values': [[1, 0], [0, 1]], 'evidences': ['E']},
        {'variable': 'A', 'values': [[0.999, 0.59, 0.05, 0.02], [0.001, 0.41, 0.95, 0.98]], 'evidences': ['B', 'E']}
    ])

    result1 = model\
        .when(variables = ['A'])\
        .then()
    print(result1)

    result2 = model\
        .when(variables = ['A'], evidences = {'R': 1})\
        .then()
    print(result2)