from os import getenv
from dotenv import load_dotenv, find_dotenv
import sys
import contentdeskopendata
import os

load_dotenv(find_dotenv())

## Load from Job Environment Variables
AKENEO_HOST = getenv('AKENEO_HOST')
AKENEO_CLIENT_ID = getenv('AKENEO_CLIENT_ID')
AKENEO_CLIENT_SECRET = getenv('AKENEO_CLIENT_SECRET')
AKENEO_USERNAME = getenv('AKENEO_USERNAME')
AKENEO_PASSWORD = getenv('AKENEO_PASSWORD')

CDN_URL = getenv('CDN_URL')

def main():
    host = AKENEO_HOST
    clientid = AKENEO_CLIENT_ID
    secret = AKENEO_CLIENT_SECRET
    user = AKENEO_USERNAME
    passwd = AKENEO_PASSWORD
    cdnurl = CDN_URL
    path = "/docs"
    projectPath = os.path.dirname(os.path.abspath(__file__))
    
    contentdeskopendata.ContentdeskOpenData(host, clientid, secret, user, passwd, cdnurl, projectPath+path)

if __name__ == '__main__':
    main()