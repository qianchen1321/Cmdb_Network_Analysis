
class H3cCmdbExcep(Exception):
    def __init(self):
        super("在配置文本中找不到对应华三接口")

class H3cInterCutExcep(H3cCmdbExcep):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class H3cInterFindExcep(H3cCmdbExcep):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message