# Get input IP address from the user
ip_address = input("Enter an IP address: ")

# Split the IP address into octets
octets = ip_address.split('.')

# Remove leading zeros from each octet
cleaned_octets = [str(int(octet)) for octet in octets]

# Join the cleaned octets to form the modified IP address
cleaned_ip_address = '.'.join(cleaned_octets)

# Print the original and modified IP addresses
print("Original IP address:", ip_address)
print("IP address without leading zeros:", cleaned_ip_address)
