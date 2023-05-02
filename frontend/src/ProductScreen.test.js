import React from "react";
import { render } from "@testing-library/react";
import ProductScreen from "./screens/productscreen";

describe("ProductScreen component", () => {
  it("should render without errors", () => {
    const { getByText } = render(<ProductScreen />);
    expect(getByText("Go Back")).toBeInTheDocument();
  });
});
