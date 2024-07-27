/*
Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

For example, the score of abad is 8 (1 + 2 + 1 + 4).

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.
*/

export function high(str: string) {
  const offset = 96;
  let wordScores = new Map<string, number>();
  str
    .toLowerCase()
    .split(" ")
    .map((w, _, a) => {
      wordScores.set(w, 0);
      w.split("").map((c) => {
        wordScores.set(w, wordScores.get(w)! + c.charCodeAt(0) - offset);
      });
    });

  let result: { word: string; score: number } = { word: "", score: 0 };

  for (let [word, score] of wordScores) {
    if (score > result.score) {
      result = { word, score };
    }
  }
  return result.word;
}
