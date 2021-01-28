import argparse
import json
import logging
from captcha.solver import load_captcha_data
from course_enroller import take_courses

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)


def _validate_config(config):
    assert type(config["username"]) == str, "username must be of type string"
    assert type(config["password"]) == str, "password must be of type string"
    assert type(config["start_hour"]) == int, "start_hour must be an integer"
    assert type(config["max_requests_per_course"]) == int, "max_requests_per_course must be an integer"
    assert type(config["courses"]) == list, "courses must be of type list"
    for course in config["courses"]:
        assert type(course["course"]) == str, "course number must be of type string"
        assert course["units"] >= 0, "course units must be non-negative"
    assert type(config["request_backoff_sec"]) == int, "request_backoff_sec must be of type integer"


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Automatically take courses.')
    parser.add_argument('--config-path', type=str, help="Config file path", required=True)
    parser.add_argument('--data-path', type=str, help="Data path for the captcha file", required=True)
    args = parser.parse_args()

    load_captcha_data(args.data_path)
    logging.info("Loaded captcha data.")

    with open('config.json', 'r') as f:
        config = json.load(f)
    _validate_config(config)
    logging.info("Loaded Config.")

    take_courses(
        username=config['username'],
        password=config['password'],
        request_backoff_sec=config['request_backoff_sec'],
        start_hour=config['start_hour'],
        courses=config['courses'],
        max_requests_per_course=config['max_requests_per_course']
    )
