#!/bin/bash

# CT EVV API Documentation - Quick Start Script

echo "🚀 CT EVV API Documentation Setup"
echo "=================================="
echo ""

# Check if mintlify is installed
if ! command -v mintlify &> /dev/null
then
    echo "📦 Mintlify not found. Installing..."
    npm install -g mintlify
    echo "✅ Mintlify installed successfully!"
else
    echo "✅ Mintlify is already installed"
fi

echo ""
echo "🌐 Starting local development server..."
echo ""
echo "📖 Documentation will be available at: http://localhost:3000"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

# Start the development server
mintlify dev
