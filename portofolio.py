import chromadb
import pandas as pd
import uuid

class Portfolio:
    def __init__ (self,filepath="C:/Users/HP/Cold_email/my_portfolio.csv"):
        self.filepath=filepath
        self.data=pd.read_csv(filepath)
        self.client=chromadb.PersistentClient("Vecordbq")
        self.collection=self.client.get_or_create_collection(name="portfolio")

    def load_portfolio(self):
        if not self.collection.count():
            for _, row in self.data.iterrows():
                self.collection.add(
                    documents= row['Techstack'],
                    metadatas={'Links':row['Links']},
                    ids=[str(uuid.uuid4())]
        )
    def get_query(self, skill):
        if not skill:  # Check if skill is empty
            print("Error: skill is empty or None!")
        return []  # Return an empty list instead of making the query

        if isinstance(skill, str):  # Convert a single string to a list
            skill = [skill]

        return self.collection.query(query_texts=skill, n_results=2).get('metadatas', [])
