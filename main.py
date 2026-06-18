# A simple script to take user data and save it to a file
print("--- Data Engineering Ingestion Script v1.0 ---")

user_name = input("Enter your name: ")
if not user_name.strip():
    print("Error: Name cannot be empty. Please run the script again and provide a valid name.")
    exit(1)
user_role = input("Enter your target career (e.g., Data Engineer): ")
if not user_role.strip():
    print("Error: Target role cannot be empty. Please run the script again and provide a valid role.")
    exit(1)

# Writing the data to a local text file
with open("user_data.txt", "w") as file:
    file.write(f"Name: {user_name}\n")
    file.write(f"Target Role: {user_role}\n")

print("✨ Data successfully ingested into user_data.txt! good")