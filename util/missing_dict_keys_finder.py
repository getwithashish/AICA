from typing import Set


class MissingDictKeysFinder:

    @staticmethod
    def find_missing_keys(required_keys: Set[str], **kwargs) -> Set[str]:
        missing_keys = required_keys - kwargs.keys()
        return missing_keys
