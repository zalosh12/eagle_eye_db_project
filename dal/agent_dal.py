import mysql.connector
from mysql.connector import Error
from models.agent import Agent

class AgentDal:
    def __init__(self,connection):
       self.conn = connection
       self.cursor = self.conn.cursor(dictionary=True)



    def add_agent(self,agent):
        query = """
        INSERT INTO agents (codeName, realName, location, status,missionsCompleted) 
        VALUES (%s, %s, %s, %s, %s)
        """
        values = (agent.code_name,agent.real_name,agent.location,agent.status,
                  agent.missions_completed)
        try:
            self.cursor.execute(query,values)
            self.conn.commit()
            print("Agent added successfully")
        except mysql.connector.Error as err:
            print(f"Failed to add agent: {err}")

    def get_all_agents(self) :
        query = "SELECT * FROM agents"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return [Agent(
            agent_id=row["id"],
            code_name=row["codeName"],
            real_name=row["realName"],
            location=row["location"],
            status=row["status"],
            missions_completed=row["missionsCompleted"]
        ) for row in result]

    def update_missions_completed(self, agent_id, missions_to_add) :
        query = "UPDATE agents SET missionsCompleted = missionsCompleted + %s WHERE id = %s"
        self.cursor.execute(query, (missions_to_add, agent_id))
        self.conn.commit()
        print("Missions count updated successfully.")

    def delete_agent(self, agent_id) :
        self.cursor.execute("DELETE FROM agents WHERE id = %s", (agent_id,))
        self.conn.commit()
        print("Agent deleted.")

    def close(self) :
        self.cursor.close()
        self.conn.close()


