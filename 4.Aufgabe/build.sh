#!/bin/bash

# Stop immediately if anything fails
set -e

# Go to the build directory
cd "$(dirname "$0")/build"

# Re-run cmake
cmake ..

# Build
make
mv libsobel_demo.so sobel_demo$(python3-config --extension-suffix)


echo "✅ Build completed successfully!"
