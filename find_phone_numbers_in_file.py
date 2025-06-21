import re

def search_in_file(file_path, search_term):
    results = []
    pattern = re.compile(search_term)

    with open(file_path, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            if pattern.search(line): # pattern.search(line).group(1) --> # returns prefix number
                results.append((line_number, line.strip(), pattern.findall(line)))
                # results.append((line_number, line.strip()))

    return results


if __name__ == "__main__":
    file_path = 'phone_numbers_spreaded.txt'  # Replace with your file path
    # file_path = 'example.txt'  # Replace with your file path
    search_term = r'(\d{3})-\d{7}'  # phone prefix, e.g., 064
    # search_term = r'\d{3}-\d{7}'  # phone number format, e.g., 054-2253998

    matches = search_in_file(file_path, search_term)
    for line_number, line, values in matches:
        print(f"Line {line_number:>2}: {line:<55}|  Values: {values}")

