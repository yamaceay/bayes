from bayes import BayesModel

if __name__ == "__main__":
    model = BayesModel.given([
        {'variable': 'C', 'values': [[0.5], [0.5]]},
        {'variable': 'S', 'values': [[0.5, 0.9], [0.5, 0.1]], 'evidences': ['C']},
        {'variable': 'R', 'values': [[0.8, 0.2], [0.2, 0.8]], 'evidences': ['C']},
        {'variable': 'W', 'values': [[1.0, 0.1, 0.1, 0.01], [0.0, 0.9, 0.9, 0.99]], 'evidences': ['S', 'R']}
    ])

    result1 = model\
        .when(variables = ['S', 'C'], evidences = {'W': 1})\
        .then()
    print(result1)
    
    result2 = model\
        .when(variables = ['S'], evidences = {'W': 1, 'R': 1})\
        .then()
    print(result2)