// See https://www.chaijs.com for how to use Chai.
import { oddOrEven } from "./solution";

// TODO Add your tests here
describe("Fixed tests", () => {
  it("Edge tests", () => {
    expect(oddOrEven([0])).toEqual("even");
    expect(oddOrEven([1])).toEqual("odd");
    expect(oddOrEven([])).toEqual("even");
  });

  it("Even tests", () => {
    expect(oddOrEven([0, 1, 5])).toEqual("even");
    expect(oddOrEven([0, 1, 3])).toEqual("even");
    expect(oddOrEven([1023, 1, 2])).toEqual("even");
  });

  it("Negative Even tests", () => {
    expect(oddOrEven([0, -1, -5])).toEqual("even");
    expect(oddOrEven([0, -1, -3])).toEqual("even");
    expect(oddOrEven([-1023, 1, -2])).toEqual("even");
  });

  it("Odd tests", () => {
    expect(oddOrEven([0, 1, 2])).toEqual("odd");
    expect(oddOrEven([0, 1, 4])).toEqual("odd");
    expect(oddOrEven([1023, 1, 3])).toEqual("odd");
  });

  it("Negative Odd tests", () => {
    expect(oddOrEven([0, -1, 2])).toEqual("odd");
    expect(oddOrEven([0, 1, -4])).toEqual("odd");
    expect(oddOrEven([-1023, -1, 3])).toEqual("odd");
  });
});
