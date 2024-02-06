import streamlit as st
from problem import Problem

from utils import ExerciseState, get_random_problem


class ExerciseFactory:

    def __init__(self, name: str):
        self.name = name

    def __str__(self) -> str:
        return self.name

    def make(self, _: list[(int, int, int)]):
        raise NotImplementedError("Method make not implemented")


class Simple(ExerciseFactory):
    
        def __init__(self):
            super().__init__("einfach")
    
        def make(self, problems: list[Problem]):
            st.write("Versuche die Aufgaben zu lösen und klicke auf die Buttons um die Lösung zu sehen.")
            for p in problems:
                container = st.empty()
                problem = container.button(f' {p} ')
                if problem:
                    container.empty()
                    container.button(f' {p.result} ')


class Medium(ExerciseFactory):
    
        def __init__(self):
            super().__init__("mittel")
    
        def make(self, problems: list[Problem]):
            st.write("Versuche die Aufgaben zu lösen und klicke auf den richtigen Button.")
            
            state = ExerciseState()
            problem = state.get_current_problem(problems)

            st.write(f' {problem} ')

            cols = st.columns(5)
            for i, col in enumerate(cols):
                if i == 0:
                    col.button(f' {problem.result} ', on_click=state.success)
                else:
                    col.button(f' {problem.result + i} ')

            st.write(f'Punkte: {state.get_points()}')