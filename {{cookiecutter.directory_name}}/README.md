# {{cookiecutter.project_name}}

## Environment Setup

### Runner Setup (Create self-hosted runner)

- Download on the cluster server under `/nfs/hpc/share/ONID_USERNAME` (replace `ONID_USERNAME` with your username)
```bash
# Create a folder
mkdir actions-runner && cd actions-runner

# Download the latest runner package
curl -o actions-runner-linux-x64-2.281.1.tar.gz -L https://github.com/actions/runner/releases/download/v2.281.1/actions-runner-linux-x64-2.281.1.tar.gz

# Optional: Validate the hash
echo "04f6c17235d4b29fc1392d5fae63919a96e7d903d67790f81cffdd69c58cb563  actions-runner-linux-x64-2.281.1.tar.gz" | shasum -a 256 -c

# Extract the installer
tar xzf ./actions-runner-linux-x64-2.281.1.tar.gz
```
- Configure runner by following instructions in (Settings -> Actions -> Runners -> Add runner), set the names as follows:

Enter the name of the runner group to add this runner to: [press Enter for Default]
Enter the name of runner: `machine-1`
Enter any additional labels (ex. label-1,label-2): `machine-1`
Enter name of work folder: [press Enter for _work]

### Setup secrets

- Weights and Biases
    - Create an account on Weights and Biases
    - Copy API Key (Settings -> API keys)
- GitHub
    - Access the secrets page (Settings -> Secrets -> New reporsitory secret)
    - Enter the name of the secret: `WANDB_API_KEY`
    - Enter the value of the secret from the copied API Key 

### Environment Setup (Local development)

- Install [Conda (miniconda)](https://conda.io/miniconda.html) & [Poetry](https://python-poetry.org/docs/#installation):
- Build and activate environment:
```bash
conda env create -f environment.yml
source activate {{cookiecutter.project_slug}}
```
- Install packages:
```bash
poetry install
```
- Create an account on [Weights and Biases](https://wandb.ai)
- Setup Weights and Biases:
```bash
wandb login
```


## Commands

- Train model
```bash
poetry run train
```
- Test model
```bash
poetry run test
```
- Run pytest
```bash
poetry run pytest tests/
```

## Instructions

- To install/uninstall packages and other commands, please refer to [Poetry's documentation](https://python-poetry.org/docs/cli/)
- To run tests, please refer to [pytest's documentation](https://docs.pytest.org/en/latest/)
- To add more experiments, please refer to `config/experiments.yml`
- To run multiple experiments, please refer to `scripts/experiments.py`