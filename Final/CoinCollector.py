
class CoinCollector:

    # constructor so you cannot instantiate this class
    def __init(self):
        pass
    def parseChange(coinsUpper):
        depositAmount = 0
        # implement parseChange here
        for coin in coinsUpper:
                    match coin:
                        case 'P':
                            depositAmount += .01
                        case 'N':
                            depositAmount += .05
                        case 'D':
                            depositAmount += .10
                        case 'Q':
                            depositAmount += .25
                        case 'H':
                            depositAmount += .50
                        case 'W':
                            depositAmount += 1.00
                        case _:
                            print(f'Invalid coin {coin}')
        return depositAmount
        
