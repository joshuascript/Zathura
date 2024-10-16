#!/bin/bash

# Check if a package name is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <package-name>"
    exit 1
fi

PACKAGE_NAME="$1"

# Define the installation directory
INSTALL_DIR="../installs"

# Ensure the installation directory exists
mkdir -p "$INSTALL_DIR"

echo "Installing $PACKAGE_NAME into directory: $INSTALL_DIR"

# Install the package into the installation directory
sudo yum --installroot="$INSTALL_DIR" --releasever=/ install -y "$PACKAGE_NAME"

# Check if the installation was successful
if [ $? -ne 0 ]; then
    echo "Failed to install $PACKAGE_NAME."
    exit 1
fi

echo "Installation complete. Files are located in $INSTALL_DIR."

# Log the installed package
LOG_FILE="../installed_yums.txt"
echo "$PACKAGE_NAME" >> "$LOG_FILE"
echo "Installed package $PACKAGE_NAME logged in $LOG_FILE."

