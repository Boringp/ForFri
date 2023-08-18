class Player:
    def __init__(self, name: str,stake:int,status=True,round_status=True):
        self.name = name
        self.stake = stake
        self.status = status
        self.round_status = round_status