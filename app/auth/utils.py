from enum import Enum

class UserInfo(Enum):
    EMAIL = 'email'
    PASSWORD = 'password'
    CITY = 'city'
    STATE = 'state'
    COUNTRY = 'country'
    ORGANIZATION_NAME = 'organization'
    LOCATION_ID = 'location_id'
    ORGANIZATION_ID = 'organization_id' 


def process_user_data(data):
    credentials = {UserInfo.EMAIL.value: data[UserInfo.EMAIL.value], UserInfo.PASSWORD.value: data[UserInfo.PASSWORD.value]}
    location = {UserInfo.CITY.value: data[UserInfo.CITY.value], 
                UserInfo.STATE.value: data[UserInfo.STATE.value], 
                UserInfo.COUNTRY.value: data[UserInfo.COUNTRY.value]}
    job = {UserInfo.ORGANIZATION_NAME.value: data[UserInfo.ORGANIZATION_NAME.value]}
    for info in UserInfo:
        if info.value in data:
            del data[info.value]
    return credentials, data, location, job
