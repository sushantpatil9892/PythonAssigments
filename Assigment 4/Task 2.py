file_name = "output.txt"
text = input("Enter text to write to the file: ")
with open(file_name, "w") as file:
    file.write(text + "\n")
print("Data successfully written to output.txt.\n")

append_text = input("Enter additional text to append: ")
with open(file_name, "a") as file:
    file.write(append_text + "\n")
print("Data successfully appended.\n")

print(f"Final content of {file_name}:")
with open(file_name, "r") as file:
    print(file.read())