try:
    filename = input("Enter the name of the file to read: ")

    # Open the input file and read its contents
    with open("purple.txt", 'r') as file:
        content = file.read()

    # Modify the content (e.g., make it uppercase)
    modified_content = content.upper()

    # Write the modified content to a new file
    with open("modified_" + "purple.txt", 'w') as new_file:
        new_file.write(modified_content)

    print("File read and modified version saved as 'modified_" + "purple.txt" + "'.")

except FileNotFoundError:
    print("Error: The file was not found.")
except IOError:
    print("Error: Could not read or write the file.")
