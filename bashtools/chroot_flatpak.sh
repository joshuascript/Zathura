#!/bin/bash

# Check if a package name is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <flatpak-package-name>"
    exit 1
fi

FLATPAK_PACKAGE="$1"

# Define the installation directory for chroot
INSTALL_DIR="../chroot_env"

# Ensure the installation directory exists
sudo mkdir -p "$INSTALL_DIR"

# Create necessary directories fo the chroot enviroment
sudo mkdir -p "$INSTALL_DIR/bin"

sudo mkdir -p "$INSTALL_DIR/lib"

sudo mkdir -p "$INSTALL_DIR/lib64"

# Make sure all the file are copied and updated for the bin, lib, lib64 directories

rsync -a --ignore-existing */bin/ ./bin/

echo "Setting up chroot environment in: $INSTALL_DIR"

# Install necessary base system for chroot environment
sudo debootstrap --variant=minbase stable "$INSTALL_DIR"

# Bind /proc, /dev, /sys for the chroot environment
sudo mount --bind /proc "$INSTALL_DIR/proc"
sudo mount --bind /dev "$INSTALL_DIR/dev"
sudo mount --bind /sys "$INSTALL_DIR/sys"

# Set up flatpak in chroot
echo "Setting up Flatpak inside chroot environment"

sudo chroot "$INSTALL_DIR" /bin/bash -c "
    apt update &&
    apt install -y flatpak &&
    flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo &&
    flatpak install -y flathub $FLATPAK_PACKAGE
"

# Unmount the directories after use
sudo umount "$INSTALL_DIR/proc"
sudo umount "$INSTALL_DIR/dev"
sudo umount "$INSTALL_DIR/sys"

echo "Flatpak package $FLATPAK_PACKAGE installed inside chroot environment at $INSTALL_DIR."

# Log the installed package
LOG_FILE="../installed_flatpaks.txt"
echo "$FLATPAK_PACKAGE" >> "$LOG_FILE"
echo "Installed Flatpak package $FLATPAK_PACKAGE logged in $LOG_FILE."

