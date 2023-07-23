from dataclasses import dataclass
import datetime

@dataclass
class userCredential:
    userName: str
    password: str
    updateDate: datetime

    def __init__(self, userName, password):
        self.userName = userName
        self.password = password
        self.updateDate = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")