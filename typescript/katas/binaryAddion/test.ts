import { addBinary } from "./solution";

describe("addBinary(1,2)", function () {
  var results1 = addBinary(1, 2);
  it("Should return something that isn't falsy", function () {
    expect(results1);
  });
  it('Should return "11"', function () {
    expect(results1).toEqual("11");
  });
});
