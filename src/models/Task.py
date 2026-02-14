class Task:
    def __init__(self, name: str, description: str):
        self.__name = name
        self.__description = description
        self.__done = False
    
    def mark_done(self):
        self.__done = True
    
    def mark_undone(self):
        self.__done = False

    def is_done(self):
        return self.__done
    
    def get_name(self):
        return self.__name
    
    def get_description(self):
        return self.__description
    
    def set_name(self, name):
        self.__name = name

    def set_description(self, description):
        self.__description = description

    def __str__(self):
        return f"Task: {self.__name}, Description: {self.__description}, Done: {self.__done}"
    
    def __repr__(self):
        return str(self)

    def to_json(self):
        return {
            "name": self.__name,
            "description": self.__description,
            "done": self.__done
        }
    
    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Task):
            return False
        
        return self.__name == value.__name and self.__description == value.__description