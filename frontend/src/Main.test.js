import { render } from "@testing-library/react";
import App from "./App";

// Test that the App renders without crashing

test("renders App component without crashing", () => {
  render(<App />);
});
