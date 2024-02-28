import streamlit as st
from streamlit.logger import get_logger

from exercises import Medium
from problem import Operation, Problem, ProblemFactory


LOGGER = get_logger(__name__)


def run():
    st.sidebar.title('Multiplikationstrainer')
    factors = st.sidebar.multiselect('Wähle deine Reihe(n)', range(1, 13), None)
    if not factors:
        st.warning('Bitte wähle eine Reihe im Menü links aus.')
        return
    
    operations = st.sidebar.multiselect('Wähle deine Rechenoperation(en)', list(Operation), Operation.MUL)
    if not operations:
        st.warning('Bitte wähle eine Operation im Menü links aus.')
        return

    ex = Medium(target=20, penalty=3)
    st.sidebar.markdown('***')
    st.sidebar.write('Anleitung')
    st.sidebar.markdown(ex.instruction)

    problems = set([Problem(base_factor=i, multiplicator=f) for i in range(1, 11) for f in factors])
    factory = ProblemFactory(problems=list(problems), operations=operations)
    ex.make(factory)


if __name__ == '__main__':
    LOGGER.info('Starting app')
    run()