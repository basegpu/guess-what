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

    @property
    def result(self) -> int:
        return self.base_factor * self.multiplicator
    
    @property
    def result_neighbours(self) -> list[int]:
        multiplicators = [(self.multiplicator + 1), (self.multiplicator - 1)]
        return [m * self.base_factor for m in multiplicators]