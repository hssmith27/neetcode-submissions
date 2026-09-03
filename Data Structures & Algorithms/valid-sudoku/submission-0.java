class Solution {
    public boolean isValidSudoku(char[][] board) {
        HashMap<Integer, Set<Character>> columns = new HashMap<>();
        HashMap<Integer, Set<Character>> rows = new HashMap<>();
        HashMap<Integer, Set<Character>> squares = new HashMap<>();

        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board.length; j++) {
                char current = board[i][j];
                if (current != '.') {
                    if (rows.getOrDefault(i, new HashSet<>()).contains(current) || columns.getOrDefault(j, new HashSet<>()).contains(current) || 
                    squares.getOrDefault((i/3) * 3 + j / 3, new HashSet<>()).contains(current)) {
                        return false;
                    }
                    columns.computeIfAbsent(j, k -> new HashSet<>()).add(current);
                    rows.computeIfAbsent(i, k -> new HashSet<>()).add(current);
                    squares.computeIfAbsent((i / 3) * 3 + j / 3, k -> new HashSet<>()).add(current);
                }
            }
        }
        return true;
    }
}
