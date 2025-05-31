#!/bin/bash
echo "Starting CTchargen application..."

# Activate virtual environment
source ./venv/bin/activate

# Start the backend server in the background
echo "Starting backend server..."
python scripts/run_backend.py &
BACKEND_PID=$!

# Wait for the backend to start
echo "Waiting for backend server to start..."
sleep 5

# Start the frontend server in the background
echo "Starting frontend server..."
python scripts/run_frontend.py &
FRONTEND_PID=$!

# Wait for the frontend to start
echo "Waiting for frontend server to start..."
sleep 10

# Open the web interface in the default browser
echo "Opening web interface in browser..."
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    open http://localhost:3000
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # Linux
    xdg-open http://localhost:3000 &> /dev/null || sensible-browser http://localhost:3000 &> /dev/null || x-www-browser http://localhost:3000 &> /dev/null || gnome-open http://localhost:3000 &> /dev/null || kde-open http://localhost:3000 &> /dev/null || firefox http://localhost:3000 &> /dev/null || google-chrome http://localhost:3000 &> /dev/null || chromium-browser http://localhost:3000 &> /dev/null
else
    # Other Unix-like systems
    echo "Please open http://localhost:3000 in your browser"
fi

echo "CTchargen application started successfully!"
echo ""
echo "To stop the application, press Ctrl+C"
echo ""

# Wait for user to press Ctrl+C
trap "echo 'Stopping CTchargen application...'; kill $BACKEND_PID $FRONTEND_PID 2>/dev/null; exit" INT TERM
wait
