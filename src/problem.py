from pydantic import BaseModel


class Problem(BaseModel):
    base_factor: int
    multiplicator: int
    inversed: bool = False

    def inverse(self) -> None:
        self.inversed = True

    def __str__(self) -> str:
        f1, f2 = (self.base_factor, self.multiplicator) if self.inversed else (self.multiplicator, self.base_factor)
        return f'{f1} x {f2}'
    
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
        return self.base_factor * self.multiplicator
    
    @property
    def result_neighbours(self) -> list[int]:
        multiplicators = [(self.multiplicator + 1), (self.multiplicator - 1)]
        return [m * self.base_factor for m in multiplicators]