# FiniteStateMachine
A simple implementation of the finite state machine.

The purpose of this repo is to understand how finite state machines work.
source: https://www.python-course.eu/finite_state_machine.php

How it works:
Setting up the machine
  1. define a number of states -- (optionally) with a transition function.
     
     The transition function consumes 1 element from the input.
     Returns 
          -- a next state based on the element (this next state is passed to the machine again.)
          -- the rest of the input elements.
  
     if a state has a transition function, it'll perform the function on the input element.
     if not, it is just a state (likely an end state)
  
  
  2. add all the desired states to the machine.
  
  3. add all the end states to the machine.
  
  4. set the start state.
  

Running the machine
  1. define a array of input elements. (e.g. sequence of strings or a sequence of characters i.e. a string)
  2. input the input elements to the machine.
  3. the start state of the machine performs its start state transition function to the FIRST element of the input sequence.
  4. the transition function returns the next state and the rest of the input elements.
  5. the next element in the input sequence is passed to the transition function of the next state.
  6. this continues until an end state is reached.
     (e.g. positive state, negative state or error state)

