import random
import streamlit as st
from problem import Problem

from utils import ExerciseState, get_random_problem


class ExerciseFactory():

    name: str
    instruction: str

    def __init__(self, name: str, instruction: str) -> None:
        self.name = name
        self.instruction = instruction

    def __str__(self) -> str:
        return self.name

    def make(self, _: list[(int, int, int)]):
        raise NotImplementedError('Method "make" not implemented')


class Simple(ExerciseFactory):
    
    def __init__(self):
        super().__init__(
            'Rechnen und Überprüfen',
            '- Versuche die Aufgaben zu lösen\n - klicke drauf um die Lösung zu sehen')

    def make(self, problems: list[Problem]):
        for p in problems:
            container = st.empty()
            problem = container.button(f' {p} ')
            if problem:
                container.empty()
                container.button(f' {p.result} ')


class Medium(ExerciseFactory):

    target: int
    penalty: int
    
    def __init__(self, target: int, penalty: int):
        super().__init__(
            f'Erreiche {target} Punkte',
            f'- Klicke auf das richtige Resultat\n - Mache weiter bis du {target} Punkte hast\n - bei falscher Antwort werden {penalty} Punkte abgezogen')
        self.target = target
        self.penalty = penalty

    def make(self, problems: list[Problem]):
        # the problem
        state = ExerciseState()
        problem = state.get_current_problem(problems)
        _, col, _ = st.columns([2, 1, 2])
        with col:
            st.title(f' :blue[{problem}] ')
        st.write('')
        
        # the possible answers
        cols = st.columns(5)
        random.shuffle(cols)

        # this is the right solution
        col = cols.pop().button(
                f' {problem.result} ',
                use_container_width=True,
                on_click=state.success)
        
        # assign the wrong answers to the other buttons
        alt = [problem.result + 1,
                problem.result + 2,
                problem.result - 1,
                problem.result - 2,
                problem.result + 10,
                problem.result - 10]
        alt.extend(problem.result_neighbours)
        # remove negative answers
        alt = [candidate for candidate in alt if candidate >= 0]
        # remove duplicates
        alt = list(set(alt))
        # shuffle it
        random.shuffle(alt)

        for i, col in enumerate(cols):
            col.button(
                    f' {alt[i]} ',
                    use_container_width=True,
                    on_click=state.failure)

        # result reporting
        st.write('')
        achieved = float(state.get_points()) / self.target
        if achieved < 1.0:
            st.progress(max(0.0, achieved))
            st.write(f'Punkte: {state.get_points()}')
        else:
            st.balloons()
            state.reset()