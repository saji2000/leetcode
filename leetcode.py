class Logger:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.messages = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        print(self.messages)
        if message not in self.messages:
            self.messages[message] = timestamp
            return True
        if  timestamp < self.messages[message] + 10:
            self.messages[message] = timestamp
            return False
        return True

logger = Logger()
print(logger.shouldPrintMessage(1, "foo")); 
print(logger.shouldPrintMessage(2, "bar")); 
print(logger.shouldPrintMessage(3, "foo"));  
print(logger.shouldPrintMessage(8, "bar"));  
print(logger.shouldPrintMessage(10, "foo")); 
print(logger.shouldPrintMessage(11, "foo")); 