Register '/home/user/Hadoop/Pig/ProgramPIG/pythonFunction.py' USING streaming_python AS py_function;
data=LOAD '/home/user/Hadoop/Pig/ProgramPIG/UserInfo.csv' USING PigStorage(',') AS ( user_name:chararray, end_time:chararray, idle_time:chararray, working_hours:chararray);

users=FOREACH data GENERATE py_functions.getUserName(user_name), py_functions.getIdleTime(idle_time);
sorted_user=ORDER users BY idle_time DESC;
idle_hours=LIMIT sorted_users 10;
top_idle_hours=FOREACH idle_hours GENERATE $0;

DUMP top_idle_hours;
