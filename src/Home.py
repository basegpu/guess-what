import streamlit as st
from streamlit.logger import get_logger

from exercises import Medium, Simple
from problem import Problem


LOGGER = get_logger(__name__)


def run():

    factors = range(1, 11)

    st.sidebar.title("Multiplikationstrainer")
    factor = st.sidebar.selectbox("Wähle eine Reihe und versuche die Aufgaben zu lösen.", factors, 0)

    st.header(f"Die {factor}-er Reihe:")
    
    exercises = [Simple(), Medium()]
    exec = st.sidebar.selectbox("Wähle eine Übung aus", exercises, 0)

    problems = [Problem(factor1=i, factor2=factor) for i in range(1, 11)]
    exec.make(problems)


if __name__ == '__main__':
    LOGGER.info('Starting app')
    run()