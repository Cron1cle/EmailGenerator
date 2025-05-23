import random
import string


def generate_username(length=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def generate_email():
    username_length = random.randint(5,10)
    username = generate_username(username_length)
    return f"{username}@{'web.de'}"

print(generate_email())


def generate_password():
    letters = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    password_length = random.randint(8,12)
    password = ''.join(random.choice(letters) for _ in range(password_length))
    return f"{password}"


def save_to_file(email):
    with open("generated_emails.txt", 'a') as file:
        file.write(email)

if __name__== "__main__":
    num_mails = 10

for _ in range(num_mails):
    email = generate_email()
    password = generate_password()

    print("generated emails", email)
    save_to_file(email+':'+password+'\n')

def read_names_from_file(filename):
    with open(filename, "r") as file:
        names = [line.strip() for line in file]
        return names
    
def save_to_file(name, email):
    with open("generated_data.txt", "a") as file:
        file.write(f"{name}\n")

if __name__ == "__main__":
    names = read_names_from_file("names.txt")

    num_entries = int(input("Geben Sie die Anzahl der zu generierenden Datensätze ein: "))
    
    for _ in range(num_entries):
        name = random.choice(names)
        print("Generierter Name:", name)
        save_to_file(name, email)

def read_from_file(filename):
    with open(filename, "r") as file:
        data = [line.strip() for line in file]
    return data

def generate_username(length=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def generate_email(username, domain):
    return f"{username}@{domain}"

def save_to_file(name, email, location, postcode):
    with open("generated_data.txt", "a") as file:
        file.write(f"{name} - {email} - {location} - {postcode} \n")

if __name__ == "__main__":
    names = read_from_file("names.txt")
    locations = read_from_file("locations.txt")
    postcode = read_from_file("postcode.txt")

    num_entries = int(input("Geben Sie die Anzahl der zu generierenden Datensätze ein: "))
    
    for _ in range(num_entries):
        name = random.choice(names)
        email = generate_email(generate_username(), 'example.com')
        location = random.choice(locations)
        print("Generierter Name:", name)
        print("Generierte E-Mail-Adresse:", email)
        print("Generierter Ort und Postleitzahl:", location)
        print("Generierter Postleitzahl:",postcode)
        save_to_file(name, email, location, postcode)

def generate_adress(streets, numbers):
    street = random.choice(streets)
    number = random.choice(numbers)
    return f"{street} {number}"

def save_to_file(address):
    with open("generated_data.txt", "a") as file:
        file.write(f"{address}\n")

if __name__ == "__main__":
       streets = read_from_file("streets.txt")
       numbers = read_from_file("numbers.txt")  

num_entries = int(input("Geben Sie die Anzahl der zu generierenden Datensätze ein: "))

for _ in range(num_entries):
      address = (streets, numbers)
      print("Generierte Adresse:", address)
      save_to_file(address)


def generate_phonenumber(phonenumber):
    phonenumber = random.choice(phonenumber)
    return f"{phonenumber}"

def save_to_file(phonenumber):
    with open("phonenumber.txt","a") as file:
        file.write(f"{phonenumber}\n")

if __name__ == "__main__":
    phonenumber = read_from_file("phonenumber.txt")

num_entries = int(input("Geben Sie die Anzahl der zu generierenden Datensätze ein: "))

for _ in range(num_entries):
      phonenumber = (phonenumber)
      print("Generierte Adresse:", phonenumber)
      save_to_file(phonenumber)




          