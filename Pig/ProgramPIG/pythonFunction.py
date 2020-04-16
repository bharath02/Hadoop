from pig_util import outputSchema
import datetime

@outputSchema('user_name:chararray')
def getUserName(user_name):
    return user_name

@outputSchema('start_time:chararray')
def getStartTime('start_time'):
    return start_time

@outputSchema('idle_time:chararray')
def getIdleTime('idle_time'):
    return idle_time

@outputSchema('average_seconds:int')
def getWorkingHours(working_hours):
    actualTime=datetime.datetime.strptime(working_hours,'%Y-%m-%d %H:%M:%S')
    totalSeconds=actualTime.hour*3600+actualTime.minute*60+actualTime.second
    return int(totalSeconds)
