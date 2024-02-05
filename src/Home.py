import streamlit as st
from streamlit.logger import get_logger


LOGGER = get_logger(__name__)


def run():

    factors = range(1, 11)

    st.sidebar.title("Multiplikationstrainer")
    factor = st.sidebar.selectbox("Wähle eine Reihe und versuche die Aufgaben zu lösen.", factors, 0)
    
    problems = [(factor, i, factor * i) for i in range(1, 11)]

    st.header(f"Die {factor}-er Reihe:")
    st.write("Versuche die Aufgaben zu lösen und klicke auf die Buttons um die Lösung zu sehen.")
    for p in problems:
        container = st.empty()
        problem = container.button(f' {p[0]}  x  {p[1]} ')
        if problem:
            container.empty()
            container.button(f' {p[2]} ')


if __name__ == '__main__':
    LOGGER.info('Starting app')
    run()