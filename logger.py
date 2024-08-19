class Logger:
    message_times = {}

    def cleanup(self, timestamp):
        for i in self.message_times.keys():
            if self.message_times[i] + 10 < timestamp:
                del self.message_times[i]
    def shouldPrintMessage(self, message, timestamp):

        self.cleanup(timestamp)

        if message not in self.message_times or self.message_times[message] + 10 <= timestamp:
            self.message_times[message] = timestamp
            return True
        return False
    
logger = Logger()
print(logger.shouldPrintMessage("foo", 1))
print(logger.shouldPrintMessage("foo", 2))
print(logger.shouldPrintMessage("boo", 1))
print(logger.shouldPrintMessage("foo", 11))
print(logger.shouldPrintMessage("boo", 10))

