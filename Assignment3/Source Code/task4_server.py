import socket

"""
TASK 4: Salary Calculator Server
================================
This server implements business logic for salary calculation.

Functionality:
- Listens on port 7000 for incoming connections
- Receives hours worked from clients
- Calculates salary based on Bangladeshi labor rules
- Salary Structure:
  * Regular pay: Tk 200/hour (for hours ≤ 40)
  * Overtime pay: Tk 300/hour (for hours > 40)
  * Threshold: 40 hours/week standard
  * Calculation:
    - If hours ≤ 40: Salary = hours × 200
    - If hours > 40: Salary = (40 × 200) + ((hours - 40) × 300)
                   = 8000 + (excess_hours × 300)
- Validates numeric input
- Sends formatted salary response

Message Protocol:
- Header: 64 bytes containing message length
- Body: Hours worked (numeric string)
- Termination: "End" message triggers disconnection

Examples:
- Input: 30 hours → Salary = 30 × 200 = Tk 6,000
- Input: 40 hours → Salary = 40 × 200 = Tk 8,000
- Input: 50 hours → Salary = 8000 + (10 × 300) = Tk 11,000
- Input: 60 hours → Salary = 8000 + (20 × 300) = Tk 14,000

Features:
- Error handling for non-numeric input
- Floating-point hour support (e.g., 45.5 hours)
- Formatted output with currency symbol
- Professional business logic implementation
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
print("Salary Calculator Server ready...")

def calculate_salary(hours_worked):
    """
    Calculate salary based on hours worked.
    
    Args:
        hours_worked: Float representing hours worked
    
    Returns:
        Float representing calculated salary in Taka
    
    Salary Structure:
    - Regular pay: Tk 200/hour (up to 40 hours)
    - Overtime pay: Tk 300/hour (beyond 40 hours)
    
    Formula:
    - If hours ≤ 40: Salary = hours × 200
    - If hours > 40: Salary = (40 × 200) + ((hours - 40) × 300)
                   = 8000 + (excess_hours × 300)
    """
    if hours_worked <= 40:
        return hours_worked * 200
    else:
        regular_pay = 40 * 200  # Tk 8000
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * 300
        return regular_pay + overtime_pay

def handle_client_connection(client_connection, client_address):
    """
    Handle single client connection for salary calculation.
    
    Args:
        client_connection: Client socket connection
        client_address: Client address tuple (ip, port)
    
    Process:
        1. Receive message header
        2. Parse message length
        3. Receive hours worked (message body)
        4. Validate input (must be numeric)
        5. Calculate salary
        6. Send formatted response
        7. Repeat until "End" message
    """
    print(f"Connected to {client_address}")
    is_connected = True
    
    while is_connected:
        # Receive message header (64 bytes)
        received_header = client_connection.recv(MESSAGE_HEADER_SIZE).decode(ENCODING_FORMAT)
        
        if received_header:
            # Parse message length from header
            message_length = int(received_header)
            
            # Receive message body (hours worked)
            received_message = client_connection.recv(message_length).decode(ENCODING_FORMAT)
            
            # Check for termination message
            if received_message == TERMINATION_MESSAGE:
                response = f"Terminating the connection with {client_address}."
                client_connection.send(response.encode(ENCODING_FORMAT))
                print(f"Disconnected from {client_address}")
                is_connected = False
            else:
                # Process salary calculation
                try:
                    # Convert input to float (hours worked)
                    hours_worked = float(received_message)
                    
                    # Validate input (hours should be positive)
                    if hours_worked < 0:
                        server_response = "Error: Hours worked cannot be negative."
                    else:
                        # Calculate salary
                        calculated_salary = calculate_salary(hours_worked)
                        
                        # Format response
                        server_response = f"Calculated salary: Tk {calculated_salary:.2f}"
                        
                        # Log transaction
                        print(f"[{client_address}] Hours: {hours_worked} → Salary: Tk {calculated_salary:.2f}")
                
                except ValueError:
                    # Handle non-numeric input
                    server_response = "Invalid input. Please enter a number representing hours worked."
                    print(f"[{client_address}] Invalid input: '{received_message}'")
                
                # Send response
                client_connection.send(server_response.encode(ENCODING_FORMAT))
    
    # Close connection
    client_connection.close()

# Main server loop
try:
    while True:
        # Accept client connection
        client_connection, client_address = server_socket.accept()
        
        # Handle client (single connection at a time)
        # For concurrent handling, implement threading like Task 3
        handle_client_connection(client_connection, client_address)

except KeyboardInterrupt:
    print("\\nServer shutting down...")
finally:
    server_socket.close()
    print("Server socket closed.")
