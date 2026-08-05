import { cleanup, render, screen } from "@testing-library/react";
import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import App from "./App";

const { invokeMock } = vi.hoisted(() => ({
  invokeMock: vi.fn(),
}));

vi.mock("@tauri-apps/api/core", () => ({
  invoke: invokeMock,
}));

afterEach(() => {
  cleanup();
});

describe("App", () => {
  beforeEach(() => {
    invokeMock.mockReset();
  });

  it("renders application information returned by the Rust core", async () => {
    invokeMock.mockResolvedValue({
      appName: "Project Integrity OS",
      version: "0.1.0",
      coreStatus: "ready",
      operatingMode: "deterministic-first",
    });

    render(<App />);

    expect(screen.getByText("Loading core information...")).toBeTruthy();
    expect(await screen.findByText("deterministic-first")).toBeTruthy();
    expect(screen.getByText("0.1.0")).toBeTruthy();
    expect(invokeMock).toHaveBeenCalledTimes(1);
    expect(invokeMock).toHaveBeenCalledWith("get_app_info");
  });
});
