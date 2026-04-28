// skills/project-feedback-loop/templates/js/vitest.config.ts
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    globals: true,
    environment: "node",
    coverage: {
      enabled: true,
      provider: "v8",
      reporter: ["text", "lcov"]
    }
  }
});
