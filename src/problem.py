from pydantic import BaseModel


class Problem(BaseModel):
    factor1: int
    factor2: int

    def inverse(self, inverse: bool) -> None:
        if inverse:
            self.factor1, self.factor2 = self.factor2, self.factor1

    def __str__(self) -> str:
        return f'{self.factor1} x {self.factor2}'

    @property
    def result(self) -> int:
        return self.factor1 * self.factor2    