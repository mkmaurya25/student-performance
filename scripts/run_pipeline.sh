#!/bin/bash

# Navigate to the project root directory
project_root=$(dirname "$(realpath "$0")")/..
cd "$project_root" || exit

# Function to run a command and print a description
run_command() {
    echo "------------------------------------"
    echo "$2..."
    if $1; then
        echo "$2 completed successfully."
    else
        echo "$2 failed."
        exit 1
    fi
}

# Set PYTHONPATH to include the src directory
export PYTHONPATH="$project_root/src"

# Run each pipeline step

# Step 2: Data ingestion
run_command "python -m data.data_ingestion" "Running data ingestion"

# Step 3: Data transformation
run_command "python -m data.data_transformation" "Running data transformation"

# Step 4: Model training
run_command "python -m models.model_training" "Training the model"

echo "Pipeline execution completed successfully."
