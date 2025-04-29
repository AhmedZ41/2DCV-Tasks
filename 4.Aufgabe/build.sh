#!/bin/bash

# Stop immediately if anything fails
set -e

# Go to the build directory
cd "$(dirname "$0")/build"

# Re-run cmake
cmake ..

# Build
make

echo "✅ Build completed successfully!"
