import subprocess
import webbrowser
import time

print("Starting Health Chatbot...")

# Kill any existing processes on port 8000
subprocess.run("taskkill /f /im python.exe", shell=True, capture_output=True)
time.sleep(1)

# Start backend
print("Starting backend...")
subprocess.Popen(["python", "main.py"], cwd="health-chatbot-backend")
time.sleep(3)

# Start frontend  
print("Starting frontend...")
subprocess.Popen(["npm", "start"], cwd="health-chatbot-frontend", shell=True)
time.sleep(5)

# Open browser
webbrowser.open("http://localhost:3000")

print("✅ Chatbot is running!")
print("Backend: http://localhost:8000")
print("Frontend: http://localhost:3000")