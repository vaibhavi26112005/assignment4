data = input("Enter text to write to the file: ")
with open("output.txt", "w") as file:
    file.write(data + "\n")
print("Data successfully written to output.txt.\n")

# Step 2: Append additional data
extra_data = input("Enter additional text to append: ")
with open("output.txt", "a") as file:
    file.write(extra_data + "\n")
print("Data successfully appended.\n")

# Step 3: Read and display final content
print("Final content of output.txt:")
with open("output.txt", "r") as file:
    print(file.read())

