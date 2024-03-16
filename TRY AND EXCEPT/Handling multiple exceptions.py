try:
    file_name = input("Enter the name of a file:")

    # Open and read the contents of the file
    with open(file_name, 'r') as file:
        contents = file.read()
        print("File contents:", contents)

except FileNotFoundError:
    # Handle the specific exception (file not found)
    print("Error: File not found.")

except PermissionError:
    # Handle the specific exception ( permission error )
    print("Error: Permission denied to this file")

except Exception as e:
    # Handle any other exceptions not explicitly caught.
    print(f"An unexpected error occurred: {e}")
