# import subprocess
# import os
# import sys

# # Navigate to the project root directory
# project_root = os.path.dirname(os.path.abspath(__file__))
# os.chdir(project_root)

# def run_command(command, description):
#     """Run a shell command and print messages."""
#     print(f"------------------------------------")
#     print(f"{description}...")
#     subprocess.run(command, shell=True, check=True)

# try:
#     # Step 2: Data ingestion
#     run_command('python -m data.data_ingestion', "Running data ingestion")

#     # Step 3: Data transformation
#     run_command('python -m data.data_transformation', "Running data transformation")

#     # Step 4: Model training
#     run_command('python -m models.model_training', "Training the model")


#     # # Step 1: Install dependencies
#     # # run_command('pip install -r requirements.txt', "Installing dependencies")

#     # # Step 2: Data ingestion
#     # run_command('python -m src/data/data_ingestion.py', "Running data ingestion")

#     # # Step 3: Data transformation
#     # run_command('python src/data/data_transformation.py', "Running data transformation")

#     # # Step 4: Model training
#     # run_command('python src/models/model_training.py', "Training the model")

#     # # Step 5: Run tests
#     # run_command('python -m pytest tests/', "Running tests")

#     print("Pipeline execution completed successfully.")

# except subprocess.CalledProcessError as e:
#     print(f"Pipeline execution failed: {e}")

import subprocess
import os

# Navigate to the project root directory
project_root = os.path.dirname(os.path.abspath(__file__))
os.chdir(project_root)

def run_command(command, description):
    """Run a shell command and print messages."""
    print(f"------------------------------------")
    print(f"{description}...")
    subprocess.run(command, shell=True, check=True)

try:
    # Step 2: Data ingestion
    run_command('python -m src.data.data_ingestion', "Running data ingestion")

    # Step 3: Data transformation
    run_command('python -m src.data.data_transformation', "Running data transformation")

    # Step 4: Model training
    run_command('python -m src.models.model_training', "Training the model")

    print("Pipeline execution completed successfully.")

except subprocess.CalledProcessError as e:
    print(f"Pipeline execution failed: {e}")
