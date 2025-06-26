
from models import agent
from models.agent import Agent


def create_agent():
    code_name = get_valid_code_name()
    real_name = get_valid_real_name()
    location = get_valid_location()
    status = get_valid_status()
    missions_completed = get_valid_missions_completed()
    return Agent(
        code_name=code_name,
        real_name=real_name,
        location=location,
        status=status,
        missions_completed=missions_completed
    )

def get_valid_code_name():
    while True:
        code_name = input("Enter code name (minimum 8 characters): ").strip()
        if len(code_name) >= 8:
            return code_name
        print("Invalid code name. Must be at least 8 characters. Try again.")

def get_valid_real_name():
    while True:
        real_name = input("Enter real name (minimum 6 letters, letters only): ").strip()
        if real_name and real_name.isalpha() and len(real_name) >= 6:
            return real_name
        print("Invalid real name. Must be at least 6 letters and contain only alphabetic characters. Try again.")

def get_valid_location():
    while True:
        location = input("Enter current location: ").strip()
        if location:
            return location
        print("Location cannot be empty. Please enter a valid location.")

def get_valid_status():
    valid_statuses = ["Active", "Injured", "Missing", "Retired"]
    while True:
        status = input(f"Enter status ({', '.join(valid_statuses)}): ").strip()
        if status in valid_statuses:
            return status
        print(f"Invalid status. Please choose from: {', '.join(valid_statuses)}")

def get_valid_missions_completed():
    while True:
        try:
            missions_completed = int(input("Enter number of missions completed: "))
            if missions_completed >= 0:
                return missions_completed
            print("Number of missions must be non-negative. Try again.")
        except ValueError:
            print("Please enter a valid number.")

def get_valid_agent_id():
    while True:
        try:
            agent_id = int(input("Enter agent ID: "))
            if agent_id > 0:
                return agent_id
            print("Agent ID must be positive. Try again.")
        except ValueError:
            print("Please enter a valid number.")

def get_valid_missions_to_add():
    while True:
        try:
            missions_to_add = int(input("Enter number of missions to add: "))
            if missions_to_add >= 0:
                return missions_to_add
            print("Number of missions to add must be non-negative. Try again.")
        except ValueError:
            print("Please enter a valid number.")




