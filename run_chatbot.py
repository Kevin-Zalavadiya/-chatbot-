import subprocess
import time
import os
import sys

def start_chatbot():
    print("🚀 Starting Health Chatbot...")
    
    # Change to chatbot directory
    os.chdir(r"d:\chatbot")
    
    try:
        # Start backend
        print("📡 Starting backend server...")
        backend_process = subprocess.Popen([
            sys.executable, "main.py"
        ], cwd="health-chatbot-backend")
        
        # Wait for backend to start
        time.sleep(3)
        
        # Start frontend
        print("🌐 Starting frontend server...")
        frontend_process = subprocess.Popen([
            "npm", "start"
        ], cwd="health-chatbot-frontend", shell=True)
        
        print("\n✅ Both servers started!")
        print("🔗 Backend: http://localhost:8000")
        print("🔗 Frontend: http://localhost:3000")
        print("\nPress Ctrl+C to stop both servers...")
        
        # Wait for user to stop
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n🛑 Stopping servers...")
            backend_process.terminate()
            frontend_process.terminate()
            print("✅ Servers stopped!")
            
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    start_chatbot()