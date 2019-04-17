from locust import HttpLocust, TaskSet
import os


def factory(uri):
    def _locust(locust):
        locust.client.get(uri)
    return _locust


num, mytasks = 1, {}
while os.getenv('URI'+str(num)):
    mytasks[factory(os.getenv('URI'+str(num)))] = 1
    num += 1


def index(l):
    l.client.get('/')


if mytasks == {}:
    mytasks = {index: 1}


class TestCase(TaskSet):
    tasks = mytasks


class WebsiteUser(HttpLocust):
    task_set = TestCase
    host = os.getenv('HOSTNAME')
    min_wait = int(os.getenv('MIN_WAIT')) if os.getenv('MIN_WAIT') else 5000
    max_wait = int(os.getenv('MAX_WAIT')) if os.getenv('MAX_WAIT') else 15000
