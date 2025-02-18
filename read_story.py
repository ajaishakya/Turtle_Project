# Function to Read from Dictionary
def read_story(filename):
    options = {}
    try:
        with open(filename, "r", encoding="utf-8") as f:  
            for line in f:
                line = line.strip()  # Remove leading/trailing whitespace
                if line == "":
                    continue  # Skip empty lines
                # Split the line by the first comma and handle cases where there might be extra commas
                parts = line.split(",", 1)  # Limit split to two parts
                if len(parts) == 2:  # Only process lines that have both key and value
                    options[parts[0]] = parts[1]
                else:
                    print(f"Skipping malformed line: {line}") 
    except UnicodeDecodeError:
        print("Error reading file. Try changing the encoding or check for corrupted characters.")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
    return options
