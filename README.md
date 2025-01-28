# Bayes
Bayes is a Python library for building and querying Bayesian Networks, designed for flexible experimentation and probabilistic reasoning. The project leverages pgmpy for constructing and performing inference on Bayesian Networks.

## Features

- Easy definition of Bayesian Network structures using nodes, edges, and conditional probability tables (CPTs).
- Flexible query system to calculate probabilities of variables given evidence.
- Built-in error handling and model validation to ensure robust computations.

## Setup

This project requires Python 3.12 or newer.

1. Clone the repository:

    ```sh
    git clone <repository_url>
    cd bayes
    ```

2. [Optional] Install [uv](https://docs.astral.sh/uv/getting-started/installation/) to manage the project's dependencies: 

     ```sh
     curl -LsSf https://astral.sh/uv/install.sh | sh
     ```

3. Install the dependencies:

     ```sh
     uv sync
     ```

     or install directly from `pyproject.toml`:

     ```sh
     pip install .
     ```

After that, you can run the tests to ensure everything is working as expected:

```sh
uv run bayes_test.py
```

or 

```sh
python3 bayes_test.py
```

## API Documentation

### BayesModel

Static class for building Bayesian Network models.

#### `given(probs: List[Dict[str, Any]]) -> BayesModelInstance`

Initializes a Bayesian Network model.

**Arguments:**

- `probs`: A list of dictionaries defining variables, conditional probability distributions, and evidences.

**Returns:**

- A `BayesModelInstance` for querying the network.

### BayesModelInstance

An instance of a Bayesian Network model.

#### `when(variables: List[str], evidences: Dict[str, Any] = None) -> BayesModelInstance`

Sets the query variables and evidence.

**Arguments:**

- `variables`: Variables to query.
- `evidences`: Evidence variables with their observed values.

**Returns:**

- The same instance for chaining.

#### `then() -> BayesItem`

Performs inference on the network.

**Returns:**

- A `BayesItem` containing query results.

### BayesItem

Holds the result of a Bayesian Network query.

**Properties:**

- `variables`: List of queried variables.
- `evidences`: Evidence variables and their observed values.
- `cpd`: The computed probability distribution.