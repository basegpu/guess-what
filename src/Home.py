import streamlit as st
from streamlit.logger import get_logger

from exercises import Medium, Simple
from problem import Problem


LOGGER = get_logger(__name__)


def run():
    st.sidebar.title('Multiplikationstrainer')
    factors = st.sidebar.multiselect('Wähle deine Reihe(n)', range(1, 13), None)
    if not factors:
        st.warning('Bitte wähle deine Reihe im Menü links aus.')
        return
    
    exercises = [ Medium(target=20, penalty=3), Simple()]
    ex = st.sidebar.selectbox('Wähle deine Übung', exercises, None)
    if not ex:
        st.warning('Bitte wähle deine Übung im Menü links aus.')
        return
    st.sidebar.markdown('***')
    st.sidebar.write('Anleitung')
    st.sidebar.markdown(ex.instruction)

    problems = set([Problem(base_factor=i, multiplicator=f) for i in range(1, 11) for f in factors])
    ex.make(list(problems))


if __name__ == '__main__':
    LOGGER.info('Starting app')
    run()