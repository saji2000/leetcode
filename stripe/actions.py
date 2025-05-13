import collections
class LogAnalyzer:
    def __init__(self):
        self.logs_dict = collections.defaultdict(set)
    
    def process_logs(self, input_str):
        logs = input_str.split(',')
        for log in logs:
            info = log.split(':')
            if len(info) != 6 or not all (field for field in info):
                continue
            time = info[0] + info[1] + info[2]
            key = info[3] + info[4] + info[5]
            print(time)
            self.logs_dict[key].add(time)
        return
            
    def get_action_count(self, user, action, resource):
        key = user + action + resource

        if key in self.logs_dict:
            return len(self.logs_dict[key])
        
        return 0

analyzer = LogAnalyzer()
analyzer.process_logs("2023-10-01T10:00:00:Alice:read:document1,2023-10-01T10:01:00:Bob:write:document2,2023-10-01T10:02:00:Alice:read:document1")
print(analyzer.get_action_count("Alice", "read", "document1"))  # Output: 2
print(analyzer.get_action_count("Bob", "write", "document2"))  # Output: 1
print(analyzer.get_action_count("Alice", "write", "document1"))  # Output: 0