#coding:utf-8

class FoundException(Exception):
    pass

class InvalidEntityError(Exception):
    pass

class InvalidNumericEntityError(InvalidEntityError):
    pass

class InvalidAlphaEntityError(InvalidEntityError):
    pass

class InvalidTagContentError(InvalidEntityError):
    pass

