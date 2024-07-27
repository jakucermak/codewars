/*
There is an array with some numbers. All numbers are equal except for one. Try to find it!

findUniq([ 1, 1, 1, 2, 1, 1 ]) === 2
findUniq([ 0, 0, 0.55, 0, 0 ]) === 0.55
It’s guaranteed that array contains at least 3 numbers.

The tests contain some very huge arrays, so think about performance.
*/

export function findUniq(arr: number[]): number {
  let map = new Map<number, number>();
  let res: number | null = null;
  arr.forEach((v) => {
    if (map.has(v)) {
      map.set(v, map.get(v)! + 1);
    } else {
      map.set(v, 1);
    }
  });
  map.forEach((cnt, v) => {
    if (cnt === 1) {
      res = v;
    }
  });
  return res || 0;
}
