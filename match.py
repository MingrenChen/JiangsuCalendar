from spider import data
import datetime
import pytz


class Club:
    def __init__(self, name, data):
        self.name = name
        self.match = []
        for line in data:
            self.match.append(Match(self.name, line))

    def __str__(self):
        return self.name + str(self.match)


class Match:
    def __init__(self, club, match):
        if match["hteam_name"] != club:
            self.against = match["hteam_name"]
            self.i = self.against + " - " + club
            self.info = "客场"
        else:
            self.against = match["gteam_name"]
            self.i = club + " - " + self.against
            self.info = "主场"
        self.start = datetime.datetime.strptime(match['games_time'], '%Y-%m-%d %H:%M:%S')
        self.start = self.start.replace(tzinfo=pytz.timezone('PRC'))
        self.end = datetime.datetime.strptime(match['games_time'], '%Y-%m-%d %H:%M:%S') + datetime.timedelta(hours=2)
        self.end = self.end.replace(tzinfo=pytz.timezone("PRC"))

    def __str__(self):
        return self.against + " at " + str(self.start)

    def __repr__(self):
        return self.against + " at " + str(self.start)


Jiangsu = Club("江苏苏宁", data)
if __name__ == "__main__":
    print(Jiangsu)


