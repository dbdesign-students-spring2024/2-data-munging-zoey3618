def convert_to_fahrenheit(celsius_hundredth_deg):
    """Convert temperature anomalies from 0.01 degrees Celsius to Fahrenheit."""
    celsius = celsius_hundredth_deg / 100.0  # Convert to degrees Celsius
    fahrenheit = celsius * 1.8  # Convert to Fahrenheit
    return fahrenheit

def main():
    input_file_path = "./data/GLB.Ts+dSST.txt"  # Adjust the file path as needed
    output_file_path = "./data/clean_data.csv"

    with open(input_file_path, "r") as infile, open(output_file_path, "w") as outfile:
        data_section_started = False
        for line in infile:
            stripped_line = line.strip()  # Remove leading/trailing whitespace

            if not data_section_started:
                if "Year" in stripped_line:
                    data_section_started = True
                    outfile.write(stripped_line + '\n')  # Write the 'Year' line to CSV
                    continue

            if "*" in stripped_line or not stripped_line or not stripped_line[0].isdigit():
                continue  # Skip lines with missing data, blank lines, or non-data lines

            parts = stripped_line.split()
            # Preserve the first and last parts (year) as is
            year_data = [parts[0]] + parts[1:-1] + [parts[-1]]

            # Convert only the temperature values, excluding the first and last elements
            for i, temp in enumerate(parts[1:-1], start=1):
                try:
                    if temp.replace('.','',1).lstrip('-').isdigit():
                        fahrenheit_temp = round(convert_to_fahrenheit(float(temp)), 1)
                        year_data[i] = str(fahrenheit_temp)  # Update the converted value in place
                except ValueError:
                    # Non-numeric values are preserved as-is, no need to handle them here
                    pass

            outfile.write(','.join(year_data) + '\n')

if __name__ == "__main__":
    main()
