import requests

username = 'mrchiwizi'
password = 'nigeria99'
base_url = "http://127.0.0.1:8000/api/"

# retrieve all courses
r = requests.get(f'{base_url}courses/')
courses = r.json()
available_courses = ', '.join([course['title'] for course in courses])

print(f'Available courses: {available_courses}')


for course in courses:
    course_id = course['id']
    course_title = course['title']

    r = requests.post(f'{base_url}courses/{course_id}/enroll/', auth=(username, password))

    if r.status_code == 200:
        # successful request
        print(f'Successfully enrolled in {course_title}')
    
    print(r.status_code)

# r = requests.get(f'{base_url}courses/3/contents/', auth=(username, password))

# print(r.json())





# import requests

# base_url = "http://127.0.0.1:8000/api/"


# # retrieve all courses
# r = requests.get(f"{base_url}courses/")
# courses = r.json()

# available_courses = ', '.join([course['title'] for course in courses])

# print(f'Available courses: {available_courses}')