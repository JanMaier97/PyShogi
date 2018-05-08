
class Piece(object):
    """The base class for every shogi pice."""

    def __init__(self, pos):
        """Initialize the class with the starting position of the piece."""
        self.pos = pos

    def get_possible_moves():
        """Return a list of tuples, each containing a possible new position."""
        pass

    def move(self, new_pos):
        """Set the pieces new position."""
        if self._is_valid_move(new_pos):
            self.pos = new_pos

    def _is_valid_move(new_pos):
        """Check that the new position can be reached by a valid move."""
        pass
