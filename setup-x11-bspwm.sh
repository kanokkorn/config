#!/usr/bin/env bash
#
# Automated setup script for bspwm and sxhkd
#

set -euo pipefail

# 1. Check for required build tools and dependencies
REQUIRED_TOOLS=("git" "gcc" "make" "pkg-config")

echo "==> Checking required system tools..."
for tool in "${REQUIRED_TOOLS[@]}"; do
    if ! command -v "$tool" &>/dev/null; then
        echo "Error: Required tool '$tool' is not installed." >&2
        echo "Please install essential build tools (e.g., base-devel, build-essential, or equivalent) and re-run." >&2
        exit 1
    fi
done
echo "All required system tools are present."

# 2. Create a temporary directory for cloning and compiling
BUILD_DIR=$(mktemp -d -t bspwm-build-XXXXXX)
echo "==> Created temporary working directory: ${BUILD_DIR}"

# Ensure cleanup on exit (even if script fails)
cleanup() {
    echo "==> Cleaning up temporary build files..."
    rm -rf "${BUILD_DIR}"
}
trap cleanup EXIT

cd "${BUILD_DIR}"

# 3. Clone repositories
echo "==> Cloning repositories..."
git clone https://github.com/kanokkorn/bspwm.git
git clone https://github.com/kanokkorn/sxhkd.git
git clone https://github.com/kanokkorn/config.git

# 4. Compile and install bspwm to /usr/local/bin
echo "==> Compiling and installing bspwm..."
cd "${BUILD_DIR}/bspwm"
make
sudo make PREFIX=/usr/local install

# 5. Compile and install sxhkd to /usr/local/bin
echo "==> Compiling and installing sxhkd..."
cd "${BUILD_DIR}/sxhkd"
make
sudo make PREFIX=/usr/local install

# 6. Set up configuration directory structure
CONFIG_HOME="${XDG_CONFIG_HOME:-$HOME/.config}"
echo "==> Setting up configuration files in ${CONFIG_HOME}..."

mkdir -p "${CONFIG_HOME}/bspwm"
mkdir -p "${CONFIG_HOME}/sxhkd"

# 7. Copy configuration files from the cloned repo
REPO_CONFIG="${BUILD_DIR}/config"

if [ -d "${REPO_CONFIG}/bspwm" ]; then
    cp -r "${REPO_CONFIG}/bspwm/"* "${CONFIG_HOME}/bspwm/"
fi

if [ -d "${REPO_CONFIG}/sxhkd" ]; then
    cp -r "${REPO_CONFIG}/sxhkd/"* "${CONFIG_HOME}/sxhkd/"
fi

# Ensure bspwmrc is executable
if [ -f "${CONFIG_HOME}/bspwm/bspwmrc" ]; then
    chmod +x "${CONFIG_HOME}/bspwm/bspwmrc"
fi

echo "==> Setup complete! bspwm and sxhkd are installed and configured."
