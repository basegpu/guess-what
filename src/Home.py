import streamlit as st
from streamlit.logger import get_logger

from exercises import Medium, Simple
from problem import Problem


LOGGER = get_logger(__name__)


def run():

    factors = range(1, 11)

    st.sidebar.title('Multiplikationstrainer')
    factor = st.sidebar.selectbox('Wähle deine Reihe', factors, None)
    if not factor:
        st.warning('Bitte wähle deine Reihe im Menü links aus.')
        return

    st.header(f'Die {factor}-er Reihe:')
    
    exercises = [ Medium(20), Simple()]
    ex = st.sidebar.selectbox('Wähle deine Übung', exercises, None)
    if not ex:
        st.warning('Bitte wähle deine Übung im Menü links aus.')
        return

    problems = [Problem(factor1=i, factor2=factor) for i in range(1, 11)]
    ex.make(problems)


if __name__ == '__main__':
    LOGGER.info('Starting app')
    run()