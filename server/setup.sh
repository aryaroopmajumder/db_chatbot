#!/bin/bash

# Ensure the script is executed with root privileges
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root"
   exit 1
fi

# Set non-interactive frontend to avoid prompts from apt-get
export DEBIAN_FRONTEND=noninteractive

# Update system and install curl
apt-get update && apt-get install -y curl

# Check if ollama is installed
if command -v ollama >/dev/null 2>&1; then
    echo "ollama is already installed, starting service and pulling llama2."
    ollama pull llama2
else
    echo "ollama is not installed. Installing now."
    curl -fsSL https://ollama.com/install.sh | sh
    ollama serve

    # Verify ollama was installed successfully before proceeding
    if command -v ollama >/dev/null 2>&1; then
        echo "ollama installed successfully."
        ollama serve
        ollama pull llama2
    else
        echo "Installation failed. ollama could not be installed."
        exit 1
    fi
fi

apt install python3-pip
pip install -r ./backend/requirements.txt
