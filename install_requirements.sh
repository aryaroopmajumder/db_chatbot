#!/bin/bash

# This script will check if Python3 and pip are installed, install them if they are not,
# and then install the packages from the requirements.txt file.

# Check for Python3 and install if not exists
if ! command -v python3 &> /dev/null
then
    echo "Python3 could not be found, attempting to install."
    sudo apt update
    sudo apt install -y python3
    echo "Python3 installed successfully."
else
    echo "Python3 is already installed."
fi

# Check for pip and install if not exists
if ! command -v pip3 &> /dev/null
then
    echo "pip for Python3 could not be found, attempting to install."
    sudo apt update
    sudo apt install -y python3-pip
    echo "pip for Python3 installed successfully."
else
    echo "pip for Python3 is already installed."
fi

# Install requirements using pip
if [ -f "requirements.txt" ]; then
    echo "Installing Python packages from requirements.txt..."
    pip3 install -r ./requirements.txt
    echo "Packages installed successfully."
else
    echo "requirements.txt file does not exist. Please ensure it's in the same directory as this script."
    exit 1
fi
