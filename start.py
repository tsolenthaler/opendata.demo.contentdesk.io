from os import getenv
from dotenv import load_dotenv, find_dotenv
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

APP_ORGANIZATION = getenv('APP_ORGANIZATION')
APP_NAME = getenv('APP_NAME')
APP_WEBSITE= getenv('APP_WEBSITE')
APP_WEBSITE_API = getenv('APP_WEBSITE_API')
APP_ORGANIZATION_WEBSITE = getenv('APP_ORGANIZATION_WEBSITE')
APP_REGION = getenv('APP_REGION')

def main():
    path = "/docs"
    projectPath = os.path.dirname(os.path.abspath(__file__))
    
    contentdeskopendata.ContentdeskOpenData(AKENEO_HOST, AKENEO_CLIENT_ID, AKENEO_CLIENT_SECRET, AKENEO_USERNAME, AKENEO_PASSWORD, CDN_URL, projectPath+path, APP_ORGANIZATION, APP_NAME, APP_WEBSITE, APP_ORGANIZATION_WEBSITE, APP_REGION)

if __name__ == '__main__':
    main()