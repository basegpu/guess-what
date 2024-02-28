import streamlit as st

from problem import Problem, ProblemFactory


class ExerciseState:

    POINTS_KEY: str = 'points'
    PROBLEM_KEY: str = 'problem'

    def __init__(self):
        if self.POINTS_KEY not in st.session_state.keys():
            st.session_state[self.POINTS_KEY] = 0

    def get_points(self) -> int:
        return st.session_state[self.POINTS_KEY]

    def success(self) -> None:
        st.session_state[self.POINTS_KEY] += 1
        st.session_state.pop(self.PROBLEM_KEY)
    
    def failure(self) -> None:
        st.session_state[self.POINTS_KEY] -= 3
    
    def get_current_problem(self, factory: ProblemFactory) -> Problem:
        if self.PROBLEM_KEY not in st.session_state.keys():
            st.session_state[self.PROBLEM_KEY] = factory.make()
        return st.session_state[self.PROBLEM_KEY]
    
    def reset(self) -> None:
        st.session_state[self.POINTS_KEY] = 0
