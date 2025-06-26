import mysql.connector
from models.agent import Agent

class AgentDal:
    def __init__(self,host='localhost',user='root',password="",database='eagleeyedb'):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor(dictionary=True)

    def add_agent(self,agent):
        query = """
        INSERT INTO agents (codeName, realName, location, status,missionsCompleted) 
        VALUES (%s, %s, %s, %s, %s)
        """
        values = (agent.code_name,agent.real_name,agent.location,agent.status,
                  agent.missions_completed)

        self.cursor.execute(query,values)
        self.conn.commit()
        print("Agent added successfully")

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


    def updete_mission_completed(self,agent_id,missions_to_add):
        query = "UPDATE agents SET missionsCompleted = missionsCompleted + %s WHERE id = %s"
        self.cursor.execute(query(agent_id,missions_to_add))
        self.conn.commit()

    def delete_agent(self, agent_id) :
        self.cursor.execute("DELETE FROM agents WHERE id = %s", (agent_id,))
        self.conn.commit()


