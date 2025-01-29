from hcloud import Client
import os

# Get the API token from the environment variable
api_token = os.environ.get('HERTZNER_API_KEY')

if not api_token:
    print("Error: HERTZNER_API_KEY environment variable not set.")
    exit(1)

# Create a client instance
client = Client(token=api_token)

# List all servers
servers = client.servers.get_all()

# Print server details
for server in servers:
    print(f"Server ID: {server.id}")
    print(f"Server Name: {server.name}")
    print(f"Server Status: {server.status}")
    print(f"Server IPv4: {server.public_net.ipv4.ip}")
    print(f"Server IPv6: {server.public_net.ipv6.ip}")
    print(f"Server Type: {server.server_type.name}")
    print(f"Server Location: {server.datacenter.location.name}")
    print("----------------------------------")

# If you want to get a specific server by ID
server_id = '59402674'
server = client.servers.get_by_id(server_id)

print(f"Specific Server ID: {server.id}")
print(f"Specific Server Name: {server.name}")
print(f"Specific Server Status: {server.status}")
print(f"Specific Server IPv4: {server.public_net.ipv4.ip}")
print(f"Specific Server IPv6: {server.public_net.ipv6.ip}")
print(f"Specific Server Type: {server.server_type.name}")
print(f"Specific Server Location: {server.datacenter.location.name}")
