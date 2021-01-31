## Sharif Auto Course Enroller
This repo contains a python code for automatically enrolling you in your courses by solving the captcha and taking the courses you want.

### Quick Start
* Install `python 3.x` and the packages in `requirements.txt` using pip.
* Change the config file:
    * `username`: Your student id.
    * `password`: Your Edu Password.
    * `start_hour`: Your course selection start hour (AKA rand). Note that if the time is passed this hour, the code will start taking courses immediately.
    * `courses`: A list of courses you wish to take with their ids, groups, and units (See the example config).
    * `max_requests_per_course`: The maximum number of times you want the code to send a request for each course (Set it to a large number if you want it to run infinitely).
    * `request_backoff_sec`: The backoff time after each unique course request (currently the website does not allow for less than 15 secs).
* Run the code using the following command:
```bash
python3 src/main.py --config-path ./config.json --data-path data/captcha_data.npz
```
* It will start sending course enrollment request as soon as your registration time comes.

Note 1: Although this code has been working for a couple semesters, **It is highly recommended that you take your courses manually while running this code to take them faster.**

Note 2: It only sends requests and does not check if the course has been taken. So, you have to do it manually.
