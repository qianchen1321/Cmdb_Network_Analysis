#coding:utf-8
from CustException.MyCusExcepion import *
import sys
import string

def parse(filename, skip_on_first_error=False):
    HEXDIGITS = frozenset("0123456789ABCDEFabcdef")
    NORMAL, PARSING_TAG, PARSING_ENTITY = range(3)
    state =NORMAL
    entity = ""
    fh = None
    try:
        fh = open(filename, encoding="uft8")
        errors = False
        for lino, line in enumerate(fh, start=1):
            for col, c in enumerate(line, start=1):
                try:
                    if state == NORMAL:
                        if c == "<":
                            state = PARSING_TAG
                        elif c == "&":
                            entity = ""
                            state = PARSING_ENTITY
                    elif state == PARSING_TAG:
                        if c == ">":
                            state = NORMAL
                        elif c == "<":
                            raise InvalidTagContentError()
                    elif state == PARSING_ENTITY:
                        if c == ";":
                            if entity.startswith("#"):
                                if frozenset(entity[1:]) - HEXDIGITS:
                                    raise InvalidNumericEntityError
                            elif not entity.isalpha():
                                raise InvalidAlphaEntityError
                            entity = ""
                            state = NORMAL
                        else:
                            if entity.startswith("#"):
                                if c not in HEXDIGITS:
                                    raise InvalidNumericEntityError()
                                elif(entity and
                                c not in string.ascii_letters):
                                    raise InvalidAlphaEntityError()
                                entity += c
                except (InvalidEntityError,
                        InvalidTagContentError) as err:
                    if isinstance(err, InvalidNumericEntityError):
                        error = "invalid numric entity"
                    elif isinstance(err, InvalidAlphaEntityError):
                        error = "invalid alphabetic entity"
                    elif isinstance(err, InvalidTagContentError):
                        error = "invalid tag"
                    print("ERROR {0} IN {1} on line {2} column {3}"
                          .format(error, filename, lino, col))
                    if skip_on_first_error:
                        raise
                    entity = ""
                    state = NORMAL
                    errors = True
        if state == PARSING_TAG:
            raise EOFError("missing '>' at end of " + filename)
        elif state == PARSING_ENTITY:
            raise EOFError("missing ';' at end of " + filename)
        if not errors:
            print("OK", filename)
    except (InvalidEntityError, InvalidTagContentError):
        pass  # Already handled
    except EOFError as err:
        print("ERROR unexpected EOF:", err)
    except EnvironmentError as err:
        print(err)
    finally:
        if fh is not None:
            fh.close()

