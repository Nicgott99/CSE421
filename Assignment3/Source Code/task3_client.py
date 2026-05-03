import socket

"""
TASK 3: Multi-threaded Vowel Counter Client
============================================
This client works with the multi-threaded server.

Functionality:
- Connects to multi-threaded server on port 7000
- Sends user input (text messages)
- Receives vowel category from server
- Repeats until "End" command
- Server handles this client in a dedicated thread

Advantages of Multi-threaded Server:
- Multiple clients can connect simultaneously
- Each client doesn't block others
- Improved responsiveness
- Better resource utilization

Message Protocol:
- Header: 64 bytes containing message length
- Body: Text to analyze
- Termination: "End" message to close connection

Interactive Usage:
- Run multiple client instances
- Each will be handled independently by server
- Type messages and receive vowel analysis
- Type "End" to disconnect
"""

ENCODING_FORMAT = "utf-8"
MESSAGE_HEADER_SIZE = 64
TERMINATION_MESSAGE = "End"

# Server configuration
server_ip_address = socket.gethostbyname(socket.gethostname())
server_port_number = 7000
server_address_tuple = (server_ip_address, server_port_number)

# Create and connect socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address_tuple)
print(f"Client connected to server at {server_address_tuple}")
print("This connection is handled in a dedicated server thread.")
print("Multiple clients can connect simultaneously.\\n")

def send_message(message_text):
    """
    Send message to server and receive response.
    
    Args:
        message_text: Message string to send
    
    Protocol:
        1. Encode message to UTF-8 bytes
        2. Calculate message length
        3. Create header with length padded to 64 bytes
        4. Send header and message
        5. Receive server response
        6. Display response
    """
    # Encode message
    encoded_message = message_text.encode(ENCODING_FORMAT)
    message_length = len(encoded_message)
    
    # Create header (message length padded to 64 bytes)
    encoded_length = str(message_length).encode(ENCODING_FORMAT)
    padded_length = encoded_length + ((b" ") * (MESSAGE_HEADER_SIZE - len(encoded_length)))
    
    # Send header and message
    client_socket.send(padded_length)
    client_socket.send(encoded_message)
    
    # Receive and display server response
    server_response = client_socket.recv(2048).decode(ENCODING_FORMAT)
    print(f"Server: {server_response}")

# Interactive loop
try:
    while True:
        user_input = input("Enter a word/sentence (or 'End' to disconnect): ")
        send_message(user_input)
        
        if user_input == TERMINATION_MESSAGE:
            break
except KeyboardInterrupt:
    print("\\nConnection interrupted by user.")
finally:
    # Close connection
    client_socket.close()
    print("Connection closed.")
