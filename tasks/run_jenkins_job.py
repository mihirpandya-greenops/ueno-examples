# import jenkins
import os
# import sys
import time


print("here")
i = 0
while i < 10:
    print("here again")
    token_name = os.environ['TOKEN_NAME']
    if token_name != "":
        print(token_name)
    else:
        print("no token name found")
    time.sleep(1)
    i+=1
    

# jenkins_url = os.getenv('JENKINS_URL')
# print(jenkins_url)
# jenkins_username = 'admin' #os.getenv('JENKINS_USERNAME')
# jenkins_password = '1c92025660084d239a4e9a5e89c33d2d' #os.getenv('JENKINS_PASSWORD')
# job_name = os.getenv('JOB_NAME')
# token_name = os.getenv('TOKEN_NAME')

# jenkins_srv = jenkins.Jenkins(jenkins_url, username=jenkins_username, password=jenkins_password)
# next_build_number = jenkins_srv.get_job_info(job_name)['nextBuildNumber']
# jenkins_srv.build_job(job_name, token=token_name)

# while True:
#     time.sleep(10)
#     build_info = jenkins_srv.get_build_info(job_name, next_build_number)
#     if build_info['result'] != None:
#         print(build_info['result'])
#         if build_info['result'] == "FAILURE":
#             sys.exit(1)
#         break
# sys.exit(0)
