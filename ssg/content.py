import re
from yaml import load, FullLoader
from collections.abc import Mapping


class Content(Mapping):
    __delimiter = "^(?:-|\+){3}\s*$"
    __regex = re.compile(__delimeter, re.MULTILINE)

    def load(cls, string):
        _, fm, content = cls.__regex.split(string, 2)
        cls.load(fm, Loader=FullLoader)
        return cls(metadata, content)