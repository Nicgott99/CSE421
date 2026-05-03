import socket

"""
TASK 2: Vowel Counter Server
============================
This server analyzes text for vowel content.

Functionality:
- Listens on port 7000 for incoming connections
- Receives text messages from clients
- Counts vowels (a, e, i, o, u - case insensitive)
- Categorizes vowel count:
  * 0 vowels: "Not enough vowels"
  * 1-2 vowels: "Enough vowels I guess"
  * 3+ vowels: "Too many vowels"
- Sends categorization back to client

Message Protocol:
- Header: 64 bytes containing message length
- Body: Text to analyze
- Termination: "End" message triggers disconnection

Note: This version handles one client at a time.
See Task 3 for multi-client handling with threading.
"""

FORMAT = "utf-8"
HEADER = 64
DISCONNECT_MSG = "End"

# Server configuration
SERVER = socket.gethostbyname(socket.gethostname())
PORT = 7000
ADDR = (SERVER, PORT)

# Create and bind socket
SERVER_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER_SOCKET.bind(ADDR)
SERVER_SOCKET.listen()
print(f"Server is listening on {ADDR}")

def handle_client(conn, addr):
    """
    Handle single client connection.
    
    Args:
        conn: Client socket connection
        addr: Client address tuple (ip, port)
    
    Process:
        1. Receive message header
        2. Parse message length
        3. Receive message body
        4. Count vowels
        5. Categorize and respond
        6. Repeat until "End" message
    """
    print(f"Connected to {addr}")
    connected = True
    
    while connected:
        # Receive message length from header
        msg_length = conn.recv(HEADER).decode(FORMAT)
        
        if msg_length:
            msg_length = int(msg_length)
            # Receive actual message
            msg = conn.recv(msg_length).decode(FORMAT)
            
            if msg == DISCONNECT_MSG:
                # Handle disconnection
                response = f"Terminating the connection with {addr}."
                conn.send(response.encode(FORMAT))
                print(f"Disconnected from {addr}")
                connected = False
            else:
                # Count vowels in message
                vowel_count = sum(1 for char in msg if char.lower() in "aeiou")
                
                # Categorize vowel count
                if vowel_count == 0:
                    response = "Not enough vowels"
                elif vowel_count <= 2:
                    response = "Enough vowels I guess"
                else:
                    response = "Too many vowels"
                
                # Send response
                print(f"Message: '{msg}' | Vowels: {vowel_count} | Response: '{response}'")
                conn.send(response.encode(FORMAT))
    
    # Close client connection
    conn.close()

# Main server loop - currently handles one client at a time
# For concurrent handling, see Task 3 with threading
try:
    while True:
        conn, addr = SERVER_SOCKET.accept()
        handle_client(conn, addr)
except KeyboardInterrupt:
    print("\\nServer shutting down...")
finally:
    SERVER_SOCKET.close()
