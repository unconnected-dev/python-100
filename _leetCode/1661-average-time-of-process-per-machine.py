#Average Time Of Process Per Machine
#https://leetcode.com/problems/average-time-of-process-per-machine/description/
import pandas

caseData = {
    'machine_id': [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2],
    'process_id': [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1],
    'activity_type': ['start', 'end', 'start', 'end', 'start', 'end', 'start', 'end', 'start', 'end', 'start', 'end'],
    'timestamp': [0.712, 1.52, 3.14, 4.12, 0.55, 1.55, 0.43, 1.42, 4.1, 4.512, 2.5, 5]
}

caseDataframe = pandas.DataFrame(caseData)

if True:
    def get_average_time(activity):
        activity = activity.sort_values(['machine_id', 'process_id', 'timestamp'])
        activity['diff'] = activity.groupby(['machine_id', 'process_id'])['timestamp'].diff()
        activity = activity.dropna(subset=['diff'])
        return activity.groupby('machine_id')['diff'].mean().round(3).reset_index(name="processing_time")
    
print(f"{get_average_time(caseDataframe)}")
