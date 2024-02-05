import streamlit as st
from streamlit.logger import get_logger


LOGGER = get_logger(__name__)


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
    
        def make(self, problems: list[(int, int, int)]):
            st.write("Versuche die Aufgaben zu lösen und klicke auf die Buttons um die Lösung zu sehen.")
            for p in problems:
                container = st.empty()
                problem = container.button(f' {p[0]}  x  {p[1]} ')
                if problem:
                    container.empty()
                    container.button(f' {p[2]} ')

class Medium(ExerciseFactory):
    
        def __init__(self):
            super().__init__("mittel")
    
        def make(self, problems: list[(int, int, int)]):
            st.write("Versuche die Aufgaben zu lösen und klicke auf die Buttons um die Lösung zu sehen.")
            for p in problems:
                container = st.empty()
                problem = container.button(f' {p[0]}  x  {p[1]} ')
                if problem:
                    container.empty()
                    container.button('super schwer')



def run():

    factors = range(1, 11)

    st.sidebar.title("Multiplikationstrainer")
    factor = st.sidebar.selectbox("Wähle eine Reihe und versuche die Aufgaben zu lösen.", factors, 0)

    st.header(f"Die {factor}-er Reihe:")
    
    exercises = [Simple(), Medium()]
    exec = st.sidebar.selectbox("Wähle eine Übung aus", exercises, 0)

    problems = [(factor, i, factor * i) for i in range(1, 11)]
    exec.make(problems)


if __name__ == '__main__':
    LOGGER.info('Starting app')
    run()