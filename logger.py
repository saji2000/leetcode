class Logger:
    messageTimes = {}

    def cleanup(self, time):
        deleteMessages = []

        for message in self.messageTimes.keys():
            if self.messageTimes[message] + 10 < time:
                deleteMessages.append(message)
        for message in deleteMessages:
            del self.messageTimes[message]

    def shouldPrintMessage(self, message, timestamp):
        self.cleanup(timestamp)

        if message not in self.messageTimes or self.messageTimes[message] + 10 <= timestamp:
            self.messageTimes[message] = timestamp
            return True
        return False

logger = Logger()
print(logger.shouldPrintMessage("foo", 1))
print(logger.shouldPrintMessage("foo", 2))
print(logger.shouldPrintMessage("boo", 1))
print(logger.shouldPrintMessage("foo", 11))
print(logger.shouldPrintMessage("boo", 10))
print(logger.shouldPrintMessage("boo", 50))

