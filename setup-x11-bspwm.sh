#!/usr/bin/env bash
#
# Optimized setup script for bspwm and sxhkd
#

set -euo pipefail

# 1. Check for required build tools and dependencies
REQUIRED_TOOLS=("git" "gcc" "make" "pkg-config")

echo "==> Checking required system tools..."
for tool in "${REQUIRED_TOOLS[@]}"; do
    if ! command -v "$tool" &>/dev/null; then
        echo "Error: Required tool '$tool' is not installed." >&2
        echo "Please install essential build tools (e.g., base-devel, build-essential) and re-run." >&2
        exit 1
    fi
done
echo "All required system tools are present."

# 2. Setup build working directory
BUILD_DIR="${TMPDIR:-/tmp}/bspwm-build"
mkdir -p "${BUILD_DIR}"
echo "==> Working directory: ${BUILD_DIR}"

cd "${BUILD_DIR}"

# Helper function to clone or update repositories with shallow depth
clone_or_update() {
    local repo_url="$1"
    local dir_name="$2"

    if [ -d "${dir_name}/.git" ]; then
        echo "==> '${dir_name}' already cloned. Fetching latest changes..."
        git -C "${dir_name}" pull origin main || git -C "${dir_name}" pull origin master || true
    else
        echo "==> Cloning '${dir_name}' (depth=1)..."
        git clone --depth 1 "${repo_url}" "${dir_name}"
    fi
}

# 3. Clone repositories
clone_or_update "https://github.com/kanokkorn/bspwm.git" "bspwm"
clone_or_update "https://github.com/kanokkorn/sxhkd.git" "sxhkd"
clone_or_update "https://github.com/kanokkorn/config.git" "config"

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

# 6. Copy specific configuration files to target location
TARGET_CONFIG_DIR="${XDG_CONFIG_HOME:-$HOME/.config}"
SOURCE_CONFIG_DIR="${BUILD_DIR}/config/.config"

echo "==> Copying configuration files to ${TARGET_CONFIG_DIR}..."

# Ensure target directories exist
mkdir -p "${TARGET_CONFIG_DIR}/bspwm"
mkdir -p "${TARGET_CONFIG_DIR}/sxhkd"

# Copy bspwmrc
if [ -f "${SOURCE_CONFIG_DIR}/bspwm/bspwmrc" ]; then
    cp "${SOURCE_CONFIG_DIR}/bspwm/bspwmrc" "${TARGET_CONFIG_DIR}/bspwm/bspwmrc"
    echo "Copied bspwmrc"
else
    echo "Warning: Source bspwmrc not found at ${SOURCE_CONFIG_DIR}/bspwm/bspwmrc" >&2
fi

# Copy sxhkdrc
if [ -f "${SOURCE_CONFIG_DIR}/sxhkd/sxhkdrc" ]; then
    cp "${SOURCE_CONFIG_DIR}/sxhkd/sxhkdrc" "${TARGET_CONFIG_DIR}/sxhkd/sxhkdrc"
    echo "Copied sxhkdrc"
else
    echo "Warning: Source sxhkdrc not found at ${SOURCE_CONFIG_DIR}/sxhkd/sxhkdrc" >&2
fi

# Make bspwmrc executable
if [ -f "${TARGET_CONFIG_DIR}/bspwm/bspwmrc" ]; then
    chmod +x "${TARGET_CONFIG_DIR}/bspwm/bspwmrc"
fi

echo "==> Setup completed successfully!"
