""">>> img = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 1, 1, 0, 0, 0, 0, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 0, 0, 0, 0, 1, 1, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
])
>>> img2ascii(img)
'..........\n..######..\n.##....##.\n.#......#.\n.#......#.\n.#......#.\n.#......#.\n.##....##.\n..######..\n..........'
>>> print(img2ascii(img))
..........
..######..
.##....##.
.#......#.
.#......#.
.#......#.
.#......#.
.##....##.
..######..
..........
>>> print(img2ascii(img, 'O', ' '))
  000000
 00    00
 0      0
 0      0
 0      0
 0      0
 00    00
  000000

    ...
    ..."""

if __name__ == 
import doctest
doctest.testmod()
