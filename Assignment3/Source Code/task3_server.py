import socket
import threading

"""
TASK 3: Multi-threaded Vowel Counter Server
===========================================
This server improves Task 2 by handling multiple clients concurrently.

Functionality:
- Listens on port 7000 for incoming connections
- Creates new thread for each client connection
- Each client handled independently without blocking others
- Same vowel analysis as Task 2
- Can handle 100+ concurrent connections efficiently

Message Protocol:
- Header: 64 bytes containing message length
- Body: Text to analyze
- Termination: "End" message triggers connection closure

Threading Benefits:
- Scalability: Handle multiple clients simultaneously
- Responsiveness: No blocking while waiting for one client
- Resource Efficiency: Threads share process resources
- Performance: Suitable for I/O-bound operations (network)

Limitations:
- Python's GIL (Global Interpreter Lock) limits true parallelism
- For CPU-intensive tasks, consider multiprocessing
- For extreme scalability, consider async/await patterns
"""

ENCODING_FORMAT = "utf-8"
MESSAGE_HEADER_SIZE = 64
TERMINATION_MESSAGE = "End"

# Server configuration
server_ip_address = socket.gethostbyname(socket.gethostname())
server_port_number = 7000
server_address_tuple = (server_ip_address, server_port_number)

# Create and bind socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(server_address_tuple)
server_socket.listen()
print(f"Server is listening on {server_address_tuple}")
print("Multi-threaded vowel counter ready to accept connections...")

# Thread counter for monitoring
active_connections = 0
connection_lock = threading.Lock()

def handle_client_connection(client_connection, client_address):
    """
    Handle single client in dedicated thread.
    
    Args:
        client_connection: Client socket connection
        client_address: Client address tuple (ip, port)
    
    Process:
        1. Receive message header
        2. Parse message length
        3. Receive message body
        4. Count vowels
        5. Categorize and respond
        6. Repeat until "End" message
        7. Clean up and close connection
    """
    global active_connections
    
    # Increment active connection count
    with connection_lock:
        active_connections += 1
        print(f"Connected to {client_address} | Active connections: {active_connections}")
    
    is_connected = True
    
    try:
        while is_connected:
            # Receive message header (64 bytes)
            received_header = client_connection.recv(MESSAGE_HEADER_SIZE).decode(ENCODING_FORMAT)
            
            if received_header:
                # Parse message length from header
                message_length = int(received_header)
                
                # Receive message body
                received_message = client_connection.recv(message_length).decode(ENCODING_FORMAT)
                
                # Check for termination message
                if received_message == TERMINATION_MESSAGE:
                    response = f"Terminating the connection with {client_address}."
                    client_connection.send(response.encode(ENCODING_FORMAT))
                    print(f"Disconnected from {client_address}")
                    is_connected = False
                else:
                    # Count vowels (case-insensitive)
                    vowel_count = sum(1 for character in received_message if character.lower() in "aeiou")
                    
                    # Categorize vowel count
                    if vowel_count == 0:
                        server_response = "Not enough vowels"
                    elif vowel_count <= 2:
                        server_response = "Enough vowels I guess"
                    else:
                        server_response = "Too many vowels"
                    
                    # Send response
                    client_connection.send(server_response.encode(ENCODING_FORMAT))
                    print(f"[{client_address}] Message: '{received_message}' | Vowels: {vowel_count}")
    
    except Exception as e:
        print(f"Error handling client {client_address}: {e}")
    
    finally:
        # Close connection
        client_connection.close()
        
        # Decrement active connection count
        with connection_lock:
            active_connections -= 1
            print(f"Closed connection with {client_address} | Active connections: {active_connections}")

# Main server loop with threading
try:
    while True:
        # Accept new client connection
        client_connection, client_address = server_socket.accept()
        
        # Create dedicated thread for this client
        client_thread = threading.Thread(
            target=handle_client_connection,
            args=(client_connection, client_address),
            daemon=False  # Non-daemon threads won't prevent server shutdown
        )
        
        # Start thread
        client_thread.start()

except KeyboardInterrupt:
    print("\\nServer shutting down...")
finally:
    server_socket.close()
    print("Server socket closed.")
