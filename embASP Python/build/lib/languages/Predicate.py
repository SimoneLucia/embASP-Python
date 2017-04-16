from abc import ABC
class Predicate(ABC):
    
    def __init__(self, terms):
        index = 0
        self.__mapTermsType = dict()
        for val in terms:
            if len(val) > 2:
                raise Exception("Bad definition of term")
            self.__mapTermsType[index] = val
            index += 1
    
#     @classmethod
#     @abstractmethod
#     def getPredicateName(cls):
#         pass
    
    @classmethod
    def getPredicateName(cls):
        return cls.predicateName
    
    def getTermsType(self):
        return self.__mapTermsType
    