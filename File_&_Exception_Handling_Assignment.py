def read_and_write_file():
    try:
        # Step 1: Ask the user for the input filename
        file = input("Enter the filename to read: ").strip()
        
        # Step 2: Attempt to read the file
        with open(file, 'r') as infile:
            data = infile.read()
        
        # # Step 3: Modify the content (example: add line numbers)
        modified_content = [f"{idx + 1}: {line}" for idx, line in enumerate(data)]
        
        # Step 4: Write the modified content to a new file
        output_filename = "modified_" + file
        with open(output_filename, 'w') as outfile:
            outfile.writelines(modified_content)
        
        print(f"File successfully read and modified content written to '{output_filename}'!")
    
    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename and try again.")
    except IOError:
        print("Error: The file cannot be read or written to. Please check permissions.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
if __name__ == "__main__":
    read_and_write_file()
