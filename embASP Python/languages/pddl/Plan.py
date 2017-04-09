from base.Output import Output
from languages.pddl.PDDLMapper import PDDLMapper
from abc import ABC

class Plan(Output, ABC):
    
    def __init__(self, plan, error):
        super().__init__(plan, error)
        self._actionSequence = None
        self.__actionsObjects = None
        
    def getActions(self):
        if self._actionSequence == None:
            self._actionSequence = list()
            self._parse()
        return self._actionSequence
    
    def getActionsObjects(self):
        if self.__actionsObjects == None:
            self.__actionsObjects = list()
            mapper = PDDLMapper.getInstance()
            for a in self.getActions():
                obj = mapper.getObject(a.getName())
                if obj != None:
                    self.__actionsObjects.append(obj)
        return self.__actionsObjects