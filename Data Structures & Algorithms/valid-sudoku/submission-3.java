class Solution {
    public boolean isValidSudoku(char[][] board) {
        ArrayList<Character> vals = new ArrayList<Character>(Arrays.asList('1', '2', '3', '4', '5', '6', '7', '8', '9'));

        for (int r = 0; r < board.length; r++) {
            ArrayList<Character> copy = new ArrayList<>(vals);
            for (int c = 0; c < board.length; c++) {
                if (board[r][c] != '.') {
                    if (copy.contains(board[r][c])) {
                        copy.remove(Character.valueOf(board[r][c]));
                    }
                    else {
                        return false;
                    }
                }
            }
        }

        for (int c = 0; c < board.length; c++) {
            ArrayList<Character> copy = new ArrayList<>(vals);
            for (int r = 0; r < board.length; r++) {
                if (board[r][c] != '.') {
                    if (copy.contains(board[r][c])) {
                        copy.remove(Character.valueOf(board[r][c]));
                    }
                    else {
                        return false;
                    }
                }
            }
        }
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                ArrayList<Character> copy = new ArrayList<>(vals);
                for (int r = 3 * i; r < 3 * i + 3; r++) {
                    for (int c = 3 * j; c < 3 * j + 3; c++) {
                        if (board[r][c] != '.') {
                            if (copy.contains(board[r][c])) {
                                copy.remove(Character.valueOf(board[r][c]));
                            }
                            else {
                                return false;
                            }
                        }
                    }
                }
            }
        }

        return true;
    }
}
