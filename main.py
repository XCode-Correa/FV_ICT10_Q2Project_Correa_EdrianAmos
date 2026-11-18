# COMBINED PYSCRIPT FOR Q2 PROJECT
from pyscript import document, display

# Q2 Drill 2 PYSCRIPT
# Predefined sets of already existing members
members_grade10 = {
    'Francis Fernandez', 
    'Gavin Ruiz', 
    'Edrian Correa', 
    'Philip Ponce', 
    'Julian Anaque', 
    'Andrik David', 
    'Annika De Vera', 
    'Eliana Daet',
    'Lance Catu'
}
members_grade9 = {
    'Anthony Aggarao', 
    'Nico Crispino', 
    'Janna Planas'
}
members_grade8 = {
    'Khiane Herrera', 
    'Algene Cabling', 
    'Alexei Janayan', 
    'Vihaan Master'
}
members_grade7 = {
    'Sebastian Fernandez', 
    'Peter Reyes', 
    'Julian Ante', 
    'Kendra Saludar'
}

# Master set combining all sets with |
master_set = members_grade10 | members_grade9 | members_grade8 | members_grade7

def add_member(e):
    global master_set
    
    # Get user input values, clean extra spaces, and convert to title case
    first_name = " ".join(document.getElementById("first_name").value.split()).title()
    last_name = " ".join(document.getElementById("last_name").value.split()).title()
    name = f"{first_name} {last_name}"

    # Create a set containing the new user input with bold tags and add it to the master set
    new_member_set = {f"<strong>{name}</strong>"}
    master_set = master_set | new_member_set

    # Format members with br directly from the set using join()
    formatted_members = "<br>".join(sorted(master_set))

    # Get the total number of unique members using len()
    total_members = len(master_set)

    # Formatting the final output
    result_message = f"""
    <strong>ALL MEMBERS:</strong><br>
    {formatted_members}<br><br>
    <strong>TOTAL MEMBERS:</strong> {total_members}
    """

    # Display result using innerHTML
    document.getElementById("result").innerHTML = result_message

    # Cleared input boxes for new input
    document.getElementById("first_name").value = ""
    document.getElementById("last_name").value = ""


# Q2 Seatwork 1 PYSCRIPT
def check_club(e):
    # Clear previous result
    document.getElementById("result").innerHTML = ""
    
    # Get user input values then combined the first and last name
    first_name = " ".join(document.getElementById("first_name").value.split()).title()
    last_name = " ".join(document.getElementById("last_name").value.split()).title()
    name = f"{first_name} {last_name}"

    # List of candidates
    candidates = [
        'Francis Fernandez', 
        'Gavin Ruiz', 
        'Edrian Correa', 
        'Philip Ponce', 
        'Julian Anaque', 
        'Andrik David', 
        'Annika De Vera', 
        'Eliana Daet',
        'Lance Catu'
    ]

    # Checks if candidate exists in list (True or False)
    check_candidate = name in candidates
    # Turns check_candidate to integer (0 or 1)
    check_candidate = int(check_candidate)

    # Tuple that contains messages with index (0 for Sorry... and 1 for Congratulations...)
    messages = ((f"Sorry {name}, your name is not on the list."), (f"Congratulations {name}! You are now part of the ICT Club."))

    # Select messages based on index of message based on the check_candidate number
    result_message = messages[check_candidate]

    display(result_message, target="result")


# Q2 Skills Test PYSCRIPT
# Dictionary containing non-metal elements: Symbol -> (Name, Atomic Number, Atomic Mass)
non_metals = {
    "H": ("Hydrogen", 1, "1.008"),
    "HE": ("Helium", 2, "4.0026"),
    "C": ("Carbon", 6, "12.011"),
    "N": ("Nitrogen", 7, "14.007"),
    "O": ("Oxygen", 8, "15.999"),
    "F": ("Fluorine", 9, "18.998"),
    "NE": ("Neon", 10, "20.180"),
    "P": ("Phosphorus", 15, "30.974"),
    "S": ("Sulfur", 16, "32.06"),
    "CL": ("Chlorine", 17, "35.45"),
    "AR": ("Argon", 18, "39.948"),
    "SE": ("Selenium", 34, "78.971"),
    "BR": ("Bromine", 35, "79.904"),
    "KR": ("Krypton", 36, "83.798"),
    "I": ("Iodine", 53, "126.90"),
    "XE": ("Xenon", 54, "131.29"),
    "RN": ("Radon", 86, "222"),
    "OG": ("Oganesson", 118, "294")
}

# Function py-click="check_element" when user clicks button
def check_element(event):
    # Retrieve & format element symbol entered in input for function
    Element1 = document.getElementById("element1").value.strip().upper()

    # Search non_metals dictionary or return default error if not found
    result = non_metals.get(Element1, ("Element not found in non-metals list", "-", "-"))

    # Update the HTML elements with retrieved info
    document.getElementById("symbol").innerText = Element1
    document.getElementById("name").innerText = result[0]
    document.getElementById("number").innerText = result[1]
    document.getElementById("mass").innerText = result[2]