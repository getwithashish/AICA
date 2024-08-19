from uuid import UUID, uuid5


class StringToUuidConverter:

    @staticmethod
    def convert_to_uuidv5(string_value: str) -> UUID:
        namespace = UUID("39d6ab6b-2c33-4739-a968-6a81ec5373d5")
        return uuid5(namespace, string_value)
