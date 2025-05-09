class Solution:
    def __init__(self):
        self.flightCostsDict = {}

    def flightCosts(self, input):

        flights = input.split(',')

        for flight in flights:
            info = flight.split(':')

            trip = str(info[0] + "->" + info[1])

            self.flightCostsDict[trip] = int(info[3])

    def flightCost(self, input):
        if input in self.flightCostsDict:
            return self.flightCostsDict[input]
        else:
            return "No Information"

solution = Solution()

solution.flightCosts("UK:US:FedEx:4,UK:FR:Jet1:2,US:UK:RyanAir:8,CA:UK:CanadaAir:8")

print(solution.flightCost("UK->FR"))