"""
Programming the Finite State Machine
    - FSM is used for the 'membership' problem. 
    i.e. determining whether a string or a sequence of string belongs to a formal language

https://www.python-course.eu/finite_state_machine.php
"""
class StateMachine(object):
    def __init__(self):
        self.handlers = {}
        self.startState = None
        self.endStates = []                     # a number of end states
    
    def add_state(self, name, handler, end_state=False):
        name = name.upper()
        self.handlers[name] = handler       # handler is the transition function
        if end_state:
            self.endStates.append(name)

    def set_start(self, name):
        self.startState = name.upper()

    def run(self, cargo):
        try:
            handler = self.handlers[self.startState]
        except:
            raise InitializationError("must call .set_start() before .run()")
        if not self.endStates:
            raise InitializationError("at least one state must be an end_state")
        
        while True:
            (newState, cargo) = handler(cargo)
            if newState.upper() in self.endStates:
                print("reached ", newState)
                break
            else:
                handler = self.handlers[newState.upper()]       # if it is not an end state, then
                                                                # get the new transition function
                                                                # based on new state
    