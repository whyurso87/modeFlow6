from FlowPool import Parallel_All_RecognitionFlow
import TaskPool
from taskflow.patterns import linear_flow

class ModeFlow():
    def __init__(self):
        self.mode6Flow = linear_flow.Flow(self.__class__.__name__)
        self.parallel_All_RecognitionFlow = Parallel_All_RecognitionFlow(self.__class__.__name__, "frame").buildFlow()

    def buildFlow(self):
        self.mode6Flow.add(
            TaskPool.frameTask(self.__class__.__name__ + '_frameTask', provides = "frame"),
            self.parallel_All_RecognitionFlow 
        )

        return self.mode6Flow
