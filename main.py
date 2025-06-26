from dal import agent_dal
from helpers import menus
from helpers.validation import create_agent,get_valid_missions_to_add,get_valid_agent_id
import models

def main():
    dal = agent_dal.AgentDal()

    exit = False

    while not exit:
        menus.menu()

        user_choice = input("Choose option: ")

        match(user_choice):
            case "1":
                new_agent = create_agent()
                dal.add_agent(new_agent)
            case "2":
                agents = dal.get_all_agents()
                for a in agents:
                    print(a)
            case "3":
                agent_id = get_valid_agent_id()
                missions_to_add = get_valid_missions_to_add()
                dal.updete_mission_completed(agent_id=agent_id,missions_to_add=missions_to_add)
            case "4":
                agent_id = get_valid_agent_id()
                dal.delete_agent(agent_id=agent_id)
            case "5":
                exit = True
            case _:
                print("invalid choice try again")

if __name__ == "__main__":
    main()

