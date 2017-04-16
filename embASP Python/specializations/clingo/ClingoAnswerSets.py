from languages.asp.AnswerSets import AnswerSets
import re
from languages.asp.AnswerSet import AnserSet
import traceback


class ClingoAnswerSets(AnswerSets):
    
    def __init__(self, out, err=None):
        super().__init__(out, err)
        
#     OUTPUT CON OPTIMUM NON TESTATO
    def _parse(self):
        optimum = "OPTIMUM" in self._output
        
        if not optimum:
            match = tuple(re.finditer(r"Answer: (\d+)\r?\n(.*)", self._output))
        else:
            match = tuple(re.finditer(r"Answer: (\d+)\r?\n(.*)(\r?\nOptimization: (.+))", self._output))
        
        for m in match:
            try:
                if m.group(1) == None or int(m.group(1)) <= len(self._answersets):
                    continue
            except Exception:
                traceback.print_exc()
                break
            
            matcherAnswerSet = tuple(re.finditer(r"-?[a-z][A-Za-z0-9_]*(\(.*?\))?", m.group(2)))
            answerSetList = list()
            
            for ma in matcherAnswerSet:
                answerSetList.append(ma.group())
                
            
            if optimum:
                weightMap = dict()
                try:
                    split = m.group(4).split(" ")
                    level = len(split)
                    for weight in split:
                        weightMap[level] = int(weight)
                        level-=1
                except Exception:
                    traceback.print_exc()
                    
                self._answersets.append(AnserSet(answerSetList, weightMap))
                
            else:
                self._answersets.append(AnserSet(answerSetList))
            
            
            
            
            
            
            
            
            
            
            
                