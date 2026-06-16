# A simple script to take user data and save it to a file
print("--- Data Engineering Ingestion Script v1.0 ---")

user_name = input("Enter your name: ")
user_role = input("Enter your target career (e.g., Data Engineer): ")

# Writing the data to a local text file
with open("user_data.txt", "w") as file:
    file.write(f"Name: {user_name}\n")
    file.write(f"Target Role: {user_role}\n")

print("✨ Data successfully ingested into user_data.txt!")