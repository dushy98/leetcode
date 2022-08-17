class Solution {
    public int uniqueMorseRepresentations(String[] words) {
        String[] Morse =  new String[]{".-","-...","-.-.","-..",".","..-.","--.",
                         "....","..",".---","-.-",".-..","--","-.",
                         "---",".--.","--.-",".-.","...","-","..-",
                         "...-",".--","-..-","-.--","--.."};
                                       
        Set<String> seen = new HashSet();
        for (String word: words){
            StringBuilder code = new StringBuilder();
            for (char c: word.toCharArray())
                code.append(Morse[c - 'a']);
            seen.add(code.toString());
        }
        return seen.size();
    }
}