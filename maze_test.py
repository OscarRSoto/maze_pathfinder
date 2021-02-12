import maze
import pytest

@pytest.mark.parametrize('maze_name, objetivo',
                         [('maze1.txt',(0, 5)),
                          ('maze2.txt',(8, 13)),
                          ('maze3.txt',(2, 1)),
                          ('maze4.txt',(1, 1)),
                          ('maze5.txt',(18, 25))
                          ])
def test_prueba(maze_name, objetivo):
    m = maze.Maze(maze_name)
    m.solve
    assert m.goal == objetivo
