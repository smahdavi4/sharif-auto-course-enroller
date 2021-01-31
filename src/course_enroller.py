from datetime import datetime
import json
import requests
import threading
import time
import logging
import urllib3

from captcha.solver import solve_captcha

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class EduClient:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.jwt_auth = None

    def initialize(self):
        self._set_auth()
        threading.Thread(target=self._periodic_auth_update).start()

    def send_take_course_request(self, course_name, course_units):
        if self.jwt_auth is None:
            raise Exception("Edu Client not initialized")
        data = {
            "action": "add",
            "course": course_name,
            "units": course_units
        }
        response = requests.post(
            'https://my.edu.sharif.edu/api/reg',
            headers=self._get_headers(),
            data=json.dumps(data),
            verify=False
        )
        return response

    def _periodic_auth_update(self):
        while True:
            time.sleep(10 * 60)
            self._set_auth()

    def _set_auth(self):
        while True:
            try:
                auth_jwt = self._fetch_auth()
                self.jwt_auth = auth_jwt
                logging.info("Updated Auth JWT token: {}".format(auth_jwt))
                break
            except Exception as e:
                logging.error(e)
                logging.info("Failed to fetch auth. Retrying in 10 seconds")
                time.sleep(10)

    def _get_headers(self):
        return {
            'sec-fetch-mode': 'cors',
            'origin': 'https://my.edu.sharif.edu',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9,fa-IR;q=0.8,fa;q=0.7',
            'authorization': self.jwt_auth,
            'content-type': 'application/json',
            'accept': 'application/json',
            'referer': 'https://my.edu.sharif.edu/courses/offered',
            'authority': 'my.edu.sharif.edu',
            'sec-fetch-site': 'same-origin',
        }

    def _fetch_auth(self):
        captcha_req = requests.get('https://my.edu.sharif.edu/api/auth/captcha').json()
        text = solve_captcha(captcha_req['data'])
        challenge = captcha_req['challenge']
        auth_req = requests.post(
            'https://my.edu.sharif.edu/api/auth',
            data={
                'username': self.username,
                'password': self.password,
                'challenge': challenge,
                'captcha': text
            }
        ).json()
        return auth_req['token']


def take_courses(username, password, request_backoff_sec, start_hour, courses, max_requests_per_course):
    start_time = datetime.now().replace(hour=start_hour, minute=0, second=0, microsecond=0)

    if start_time < datetime.now():
        logging.warning("WARNING: You have set a start_hour in the past.")
    logging.info("Sending requests will start in {} seconds".format((start_time - datetime.now()).total_seconds()))

    edu_client = EduClient(username=username, password=password)
    edu_client.initialize()

    course_threads = []
    for course in courses:
        t = threading.Thread(target=take_single_course, args=(
            edu_client,
            course,
            start_time,
            request_backoff_sec,
            max_requests_per_course
        ))
        t.start()
        course_threads.append(t)
    for t in course_threads:
        t.join()
    logging.info("Done")


def take_single_course(edu_client: EduClient, course, start_time, request_backoff_sec, max_requests_per_course):
    _wait_until(start_time)
    for _ in range(max_requests_per_course):
        try:
            response = edu_client.send_take_course_request(course_name=course['course'], course_units=course['units'])
            # print(response.json()['messages'][-1])
            logging.info("Successfully Sent Request for course={}, units={}.".format(course['course'], course['units']))
        except Exception as e:
            # print(response.json())
            logging.error("Request for course={}, units={} was unsuccessful.".format(course['course'], course['units']))
        time.sleep(request_backoff_sec)


def _wait_until(execute_time):
    while True:
        diff = (execute_time - datetime.now()).total_seconds()
        if diff <= 0:
            return
        elif diff <= 0.1:
            time.sleep(0.001)
        elif diff <= 0.5:
            time.sleep(0.01)
        elif diff <= 1.5:
            time.sleep(0.1)
        else:
            time.sleep(1)
