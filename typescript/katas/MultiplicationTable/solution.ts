/*
Your task, is to create N×N multiplication table, of size provided in parameter.

For example, when given size is 3:

1 2 3
2 4 6
3 6 9
For the given example, the return value should be:

[[1,2,3],[2,4,6],[3,6,9]]
*/

export function multiplicationTable(size: number): number[][] {
  // Implement me! :)
  let result: number[][] = [];

  for (let i = 1; i <= size; i++) {
    let temp: number[] = [];
    for (let j: number = 1; j <= size; j++) {
      temp.push(i * j);
    }
    result.push(temp);
  }

  return result;
}
