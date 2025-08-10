#!/usr/bin/env python3
"""
Test script to debug the backend conversation history issue
"""

import requests
import json

# Backend API configuration
API_BASE_URL = "http://localhost:8002"
CHAT_HISTORY_ENDPOINT = f"{API_BASE_URL}/chathist"
CLEAR_HISTORY_ENDPOINT = f"{API_BASE_URL}/clear_history"

def test_chat_history():
    """Test the chat history endpoint"""
    try:
        print("🔍 Testing chat history endpoint...")
        response = requests.get(CHAT_HISTORY_ENDPOINT)
        
        if response.status_code == 200:
            history = response.json()
            print(f"✅ Chat history retrieved successfully")
            print(f"📊 Total messages: {len(history)}")
            
            if history:
                print("\n📝 Conversation History:")
                for i, msg in enumerate(history):
                    role = msg.get('role', 'unknown')
                    text = msg.get('text', 'no text')
                    print(f"  {i+1}. {role}: {text[:100]}{'...' if len(text) > 100 else ''}")
            else:
                print("   No conversation history yet")
        else:
            print(f"❌ Failed to get chat history: {response.status_code}")
            print(f"   Response: {response.text}")
            
    except Exception as e:
        print(f"❌ Error testing chat history: {e}")

def clear_chat_history():
    """Clear the chat history"""
    try:
        print("\n🧹 Clearing chat history...")
        response = requests.post(CLEAR_HISTORY_ENDPOINT)
        
        if response.status_code == 200:
            result = response.json()
            print(f"✅ Chat history cleared: {result.get('message', 'Success')}")
        else:
            print(f"❌ Failed to clear chat history: {response.status_code}")
            print(f"   Response: {response.text}")
            
    except Exception as e:
        print(f"❌ Error clearing chat history: {e}")

def test_backend_health():
    """Test if the backend is running"""
    try:
        print("🏥 Testing backend health...")
        response = requests.get(f"{API_BASE_URL}/")
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Backend is running: {data}")
            return True
        else:
            print(f"❌ Backend health check failed: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Backend is not accessible: {e}")
        return False

if __name__ == "__main__":
    print("🚀 Backend Testing Script")
    print("=" * 40)
    
    # Test if backend is running
    if not test_backend_health():
        print("\n❌ Backend is not running. Please start it first:")
        print("   cd class3/backend")
        print("   python main.py")
        exit(1)
    
    # Test chat history
    test_chat_history()
    
    # Option to clear history
    print("\n" + "=" * 40)
    choice = input("Do you want to clear the chat history? (y/n): ").lower().strip()
    
    if choice in ['y', 'yes']:
        clear_chat_history()
        print("\n🔄 Testing chat history after clearing...")
        test_chat_history()
    
    print("\n✨ Testing complete!")
