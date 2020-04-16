Register '/home/user/Hadoop/Pig/ProgramPIG/pythonFunction.py' USING streaming_python AS py_function;
data=LOAD '/home/user/Hadoop/Pig/ProgramPIG/UserInfo.csv' USING PigStorage(',') AS ( user_name:chararray, end_time:chararray, idle_time:chararray, working_hours:chararray);

users=FOREACH data GENERATE py_functions.getUserName(user_name), py_functions.getStartTime(start_time);
sorted_user=ORDER users BY start_time DESC;
late_commers=LIMIT sorted_users 10;
top_late_commers=FOREACH late_commers GENERATE $0;

DUMP top_late_commers;
