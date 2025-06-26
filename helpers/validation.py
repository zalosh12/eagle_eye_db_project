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
    code_name = None
    while not code_name or len(code_name) < 8:
        code_name = input("Enter code name in length 8: ").strip()
        if len(code_name) >= 8:
            return code_name
        print("invalid code name try again")

def get_valid_real_name():
    real_name = None
    while not real_name:
        real_name = input("Enter a real name").strip()
        if not real_name.isalpha() or len(real_name) < 6:
            print("invalid real name try again")
            real_name = None
        return real_name

def get_valid_location():
    location = input("מיקום נוכחי: ")
    return location

def get_valid_status():
    status = input("סטטוס (Active, Injured, Missing, Retired): ")
    return status

def get_valid_missions_completed():
    missions_completed = int(input("כמות משימות שבוצעו: "))
    return missions_completed

def get_valid_agent_id():
    return int(input("enter agent id: "))

def get_valid_missions_to_add():
    return int(input("enter missions to add: "))




