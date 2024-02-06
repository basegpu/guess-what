import random
import streamlit as st

from problem import Problem


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
    
    def get_current_problem(self, problems: list[Problem]) -> Problem:
        if self.PROBLEM_KEY not in st.session_state.keys():
            st.session_state[self.PROBLEM_KEY] = get_random_problem(problems)
        return st.session_state[self.PROBLEM_KEY]


def get_random_problem(problems: list[Problem]) -> Problem:
    problem = random.choice(problems)
    problem.inverse(random.random() < 0.5)
    return problem
