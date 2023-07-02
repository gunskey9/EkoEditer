import subprocess
import os
import subprocess

# Clear the screen
os.system('clear')

# Use subprocess to run the figlet command and capture its output
output = subprocess.check_output(["figlet", "-f", "slant", "-l", "-w", "160", "EkoEdit"])

# Print the output
print('\033[93m' + output.decode() + '\033[0m')

filename = input("Enter the name or location of the file you would like to edit: ")

while True:
    print("\nChoose an option to edit the file:")
    print("1. Edit spaces between entries")
    print("2. Add https to each domain")
    print("3. Erase extra characters from domain list")
    print("4. Take off http from sites in list")
    print("5. Edit domains into bare urls")
    print("6. Edit out all numbers before domain")
    print("7. Edit out extra extension (suffix)")
    print("8. Edit out all extra commas in file")
    print("9. Edit out all numbers in file")
    print("10. Edit out url parameters")
    print("11. Delete specific text from file")
    print("12. Get IP address of each domain")
    print("13. Check status code of each domain")
    print("0. Edit out repeat domains")
    print("Q. Quit")

    choice = input("\nEnter your choice (0-16, Q): ")

    if choice == "1":
        subprocess.run(f"cat {filename} | tr -d ' ' > output.txt", shell=True)
    elif choice == "2":
        subprocess.run(f"sed 's/^/https:\\/\\//' {filename} > output.txt", shell=True)
    elif choice == "3":
        subprocess.run(f"sed -i 's/[^[:alnum:].-]//g' {filename}", shell=True)
    elif choice == "4":
        subprocess.run(f"sed -i 's/^http:\\/\\///' {filename}", shell=True)
    elif choice == "5":
        subprocess.run(f"sed -i 's/https\?:\\/\\/\\|www\\.//g; s/\\/.*$//' {filename}", shell=True)
    elif choice == "6":
        subprocess.run(f"sed -i 's/^[0-9]*,//g' {filename}", shell=True)
    elif choice == "7":
        subprocess.run(f"sed -i 's/\\.\\([a-z]*\\)\\.\\([a-z]*\\)\\([[:space:]]\\|\\$\\)/\\.\\2\\3/g' {filename}", shell=True)
    elif choice == "8":
        subprocess.run(f"sed -i 's/,[^,]*,//g' {filename}", shell=True)
    elif choice == "9":
        subprocess.run(f"sed -i 's/[0-9]*//g' {filename}", shell=True)
    elif choice == "10":
        subprocess.run(f"sed -i 's/\\(https\\?:\\/\\/[^\\/]*\\).*/\\1/' {filename}", shell=True)
    elif choice == "11":
        text_to_delete = input("Enter the text you want to delete: ")
        subprocess.run(f"sed -i '/{text_to_delete}/d' {filename}", shell=True)
    elif choice == "12":
        with open(filename, "r") as f:
            domains = f.readlines()
        with open("output.txt", "w") as f:
            for domain in domains:
                result = subprocess.run(f"dig +short {domain.strip()}", shell=True, capture_output=True)
                if result.returncode == 0:
                    ip = result.stdout.decode().strip()
                    f.write(f"{domain.strip()}: {ip}\n")
    elif choice == "13":
        subprocess.run(f"awk '{{print $1}}' {filename} | xargs -I {{}} sh -c 'echo -n {{}} && curl -s -o /dev/null -w \"%{{http_code}}\\n\" {{}}' | sed 's/.*\([0-9][0-9][0-9]\)$/\1/' > output.txt", shell=True)
    elif choice == "0":
        subprocess.run(f"sort -u {filename} > output.txt", shell=True)
    elif choice == "Q":
        break
    else:
        print("Invalid choice. Please try again.")
        continue

    new_filename = input("\nEnter the name of the new file to save changes (or press Enter to overwrite the original file): ")

    if not new_filename:
        subprocess.run(f"mv output.txt {filename}", shell=True)
    else:
        subprocess.run(f"mv output.txt {new_filename}", shell=True)

    print("File edited and saved successfully!")

print("Goodbye!")
