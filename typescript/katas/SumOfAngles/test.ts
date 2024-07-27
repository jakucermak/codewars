import { angle } from "./solution";

describe("basic tests", () => {
  it("angle(3)", () => expect(angle(3)).toBe(180));
  it("angle(4)", () => expect(angle(4)).toBe(360));
});
