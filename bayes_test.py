from bayes import BayesModel

if __name__ == "__main__":
    experiments = [
        {
            'probs': [
                {'variable': 'C', 'values': [[0.5], [0.5]]},
                {'variable': 'S', 'values': [[0.5, 0.9], [0.5, 0.1]], 'evidences': ['C']},
                {'variable': 'R', 'values': [[0.8, 0.2], [0.2, 0.8]], 'evidences': ['C']},
                {'variable': 'W', 'values': [[1.0, 0.1, 0.1, 0.01], [0.0, 0.9, 0.9, 0.99]], 'evidences': ['S', 'R']}
            ],
            'queries': [
                {'variables': ['S', 'C'], 'evidences': {'W': 1}},
                {'variables': ['S'], 'evidences': {'W': 1, 'R': 1}}
            ]
        },
        {
            'probs': [
                {'variable': 'B', 'values': [[0.99], [0.01]]},
                {'variable': 'E', 'values': [[0.999999], [0.000001]]},
                {'variable': 'R', 'values': [[1, 0], [0, 1]], 'evidences': ['E']},
                {'variable': 'A', 'values': [[0.999, 0.59, 0.05, 0.02], [0.001, 0.41, 0.95, 0.98]], 'evidences': ['B', 'E']}
            ],
            'queries': [
                {'variables': ['A']},
                {'variables': ['A'], 'evidences': {'R': 1}},
                {'variables': ['B'], 'evidences': {'A': 1}},
                {'variables': ['B'], 'evidences': {'A': 1, 'R': 1}},
            ]
        }
    ]

    for i, experiment in enumerate(experiments, 1):
        print(f"Experiment {i}:\n")
        bn_model = BayesModel.given(experiment['probs'])
        for query in experiment['queries']:
            result = bn_model.when(**query).then()
            print(result)