import math
from locust import HttpUser, TaskSet, task, constant
from locust import LoadTestShape


class UserTasks(TaskSet):
    
    @task
    def registrar(self):
        self.client.post("/registrar", json={
            "name": "Roberto Campos",
            "email": "robertocampos@email.com",
            "password": "1234",
            "cellphoneNumber": "12999998888"
        })
        
    @task
    def usuarios(self):
        self.client.get("/usuarios")


class WebsiteUser(HttpUser):
    wait_time = constant(0.5)
    tasks = [UserTasks]


class DoubleWave(LoadTestShape):
    
    """
    A step load shape
    Keyword arguments:
        step_time -- Time between steps
        step_load -- User increase amount at each step
        spawn_rate -- Users to stop/start per second at every step
        time_limit -- Time limit in seconds
    """

    step_time = 30
    step_load = 10
    spawn_rate = 10
    time_limit = 600

    def tick(self):
        run_time = self.get_run_time()

        if run_time > self.time_limit:
            return None

        current_step = math.floor(run_time / self.step_time) + 1
        return (current_step * self.step_load, self.spawn_rate)

# locust -f locust2.py --host=https://pycemaker.herokuapp.com --headless
