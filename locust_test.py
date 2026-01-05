from locust import HttpUser, task, between
import random
import string

class User(HttpUser):
    wait_time = between(0.5, 1)

    def random_keyword(self):
        return "term_" + ''.join(random.choices(string.ascii_lowercase, k=8))

    @task
    def get_all_terms(self):
        self.client.get("/terms")

    @task
    def get_one_term(self):
        self.client.get("/terms/Honeypot")

    @task
    def create_term(self):
        kw = self.random_keyword()
        data = {
            "keyword": kw,
            "description": "Created by Locust"
        }
        self.client.post("/terms", json=data)

    @task
    def update_term(self):
        data = {
            "description": "Updated by Locust"
        }
        self.client.put("/terms/Honeypot", json=data)

    #@task
    #def delete_term(self):
    #    kw = self.random_keyword()
    #    self.client.delete(f"/terms/{kw}")
