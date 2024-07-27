import { abbreviate } from "./solution";

describe("Tests", () => {
  it("test", () => {
    expect(abbreviate("internationalization")).toEqual("i18n");
    expect(abbreviate("accessibility")).toEqual("a11y");
    expect(abbreviate("Accessibility")).toEqual("A11y");
    expect(abbreviate("elephant-ride")).toEqual("e6t-r2e");
  });
});
