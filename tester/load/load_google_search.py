from locust import HttpUser, task, between

class GoogleUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def search_python(self):
        self.client.get("/search", params={"q": "Python Selenium pytest"})

    @task
    def search_chatgpt(self):
        self.client.get("/search", params={"q": "OpenAI ChatGPT"})

    @task
    def search_selenium(self):
        self.client.get("/search", params={"q": "Selenium WebDriver"})
