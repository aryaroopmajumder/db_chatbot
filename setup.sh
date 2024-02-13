#!/bin/bash

# Ensure the script is executed with root privileges
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root"
   exit 1
fi

# Set non-interactive frontend to avoid prompts from apt-get
export DEBIAN_FRONTEND=noninteractive

# Update system and install curl
apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Download and execute the install script
curl -fsSL https://ollama.com/install.sh | sh

ollama run llama2
