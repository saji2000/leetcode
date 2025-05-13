class TransactionProcessor:
    def __init__(self):
        self.transactions_dict = {}
    
    def process_transactions(self, input_str):
        transactions = input_str.split(',')

        for t in transactions:
            info = t.split(':')
            if len(info) != 4 or not all (field.isalpha() for field in [info[0], info[1], info[3]]):
                continue
            value = int(info[2])
            key = info[0] + "->" + info[1] + "$" + info[3]
            if key in self.transactions_dict:
                self.transactions_dict[key] += value
            else:
                self.transactions_dict[key] = value

    def get_transaction(self, sender, receiver, currency):
        return self.transactions_dict.get((sender + "->" + receiver + "$" + currency), 0)
    
processor = TransactionProcessor()
processor.process_transactions("Alice:Bob:100:USD,Bob:Charlie:50:EUR,Alice:Bob:200:USD")
print(processor.get_transaction("Alice", "Bob", "USD"))  # Output: 300
print(processor.get_transaction("Bob", "Charlie", "EUR"))  # Output: 50
print(processor.get_transaction("Alice", "Charlie", "USD"))  # Output: 0