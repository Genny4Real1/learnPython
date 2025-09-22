def split_text_file(input_file, chunk_size=2000):
    """Splits a text file into smaller parts of specified character length."""
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            text = file.read()
        
        chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
        
        for idx, chunk in enumerate(chunks):
            output_file = f"{input_file}_part{idx+1}.txt"
            with open(output_file, 'w', encoding='utf-8') as out_file:
                out_file.write(chunk)
            print(f"Chunk {idx+1} saved as {output_file}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    input_filename = "messaggio.txt"  # Replace with your file
    split_text_file(input_filename)
