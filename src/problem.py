from enum import Enum
import random
from pydantic import BaseModel


class Operation(str, Enum):
    MUL = 'multiplizieren'
    DIV = 'dividieren'

    def __str__(self) -> str:
        return self.value


class Problem(BaseModel):
    base_factor: int
    multiplicator: int
    inversed: bool = False # turn the multiplication into a division

    @property
    def product(self) -> int:
        return self.base_factor * self.multiplicator

    def flip(self) -> None:
        self.base_factor, self.multiplicator = self.multiplicator, self.base_factor

    def inverse(self) -> None:
        self.inversed = True

    def __str__(self) -> str:
        return f'{self.product} : {self.multiplicator}' if self.inversed else f'{self.base_factor} x {self.multiplicator}'
    
    def __hash__(self):
        if self.base_factor < self.multiplicator:
            return hash((self.multiplicator, self.base_factor))
        return hash((self.base_factor, self.multiplicator))
    
    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return self.__hash__() == other.__hash__()
        return NotImplemented

    @property
    def result(self) -> int:
        return self.base_factor if self.inversed else self.product
    
    @property
    def result_neighbours(self) -> list[int]:
        if self.inversed:
            # anything
            return [self.multiplicator + 1, self.multiplicator - 1]
        else:
            alt = [
                (self.multiplicator + 1, self.base_factor),
                (self.multiplicator - 1, self.base_factor),
                (self.multiplicator, self.base_factor + 1),
                (self.multiplicator, self.base_factor - 1)]
            return [a * b for a, b in alt]


class ProblemFactory(BaseModel):

    problems: list[Problem]
    operations: list[Operation]

    def make(self) -> Problem:
        problem = random.choice(self.problems)
        if random.random() < 0.5:
            problem.flip()
        if random.choice(self.operations) == Operation.DIV:
            problem.inverse()
        return problem