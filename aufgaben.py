# geheimsprache
from dataclasses import dataclass, field

def schwurbel_sentence(sentence: str) -> str:
    schwurbel = ''
    for original_word in sentence.lower().split(' '):
        schwurbel += original_word[2:] + original_word[:2] + ' '
    return schwurbel[:-1]

sentence = 'Python ist eine tolle Programmiersprache'
print(schwurbel_sentence(sentence))

# bierkasten
@dataclass
class Beerkasten:
    rows: int
    columns: int
    content: list[list[int]] = field(init=False)

    def __post_init__(self):
        self.content = [[1 for _ in range(self.columns)] for _ in range(self.rows)]
    
    def __str__(self) -> str:
        representation = ''
        for row in self.content:
            for bottle in row:
                representation += f'{bottle}/'    
            representation = representation[:-1] + '\n'
        return representation

    def get_beer(self, row: int, column: int) -> None:
        if row-1 < 0 or row > self.rows:
            print('Du hast neben den Kasten gefasst')
        elif column-1 < 0 or column > self.columns:
            print('Du hast neben den Kasten gefasst')
        elif self.content[row-1][column-1] == 0:
            print('Die Flasche ist leer')
        else:
            self.content[row-1][column-1] = 0
            print('Have fun drinking')
            print(self)



bk = Beerkasten(4, 5)
bk.get_beer(10,22)
bk.get_beer(0,0)
bk.get_beer(2,3)
bk.get_beer(1,1)
bk.get_beer(4,5)