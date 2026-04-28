// skills/project-feedback-loop/templates/js/eslint.config.mjs
import js from "@eslint/js";
import tseslint from "typescript-eslint";
import sonarjs from "eslint-plugin-sonarjs";

export default tseslint.config(
  {
    ignores: ["dist/**", "coverage/**", "node_modules/**", "**/*.mjs"]
  },
  js.configs.recommended,
  ...tseslint.configs.recommendedTypeChecked,
  {
    files: ["**/*.{ts,tsx,js,jsx}"],
    languageOptions: {
      parserOptions: {
        project: "./tsconfig.json",
        tsconfigRootDir: process.cwd()
      }
    },
    plugins: {
      sonarjs
    },
    rules: {
      "no-console": "error",
      "complexity": ["error", 10],
      "max-depth": ["error", 3],
      "max-lines-per-function": ["error", 40],
      "max-params": ["error", 4],
      "max-statements": ["error", 15],
      "sonarjs/cognitive-complexity": ["error", 15],
      "@typescript-eslint/no-explicit-any": "error",
      "@typescript-eslint/consistent-type-imports": "error"
    }
  },
  {
    files: ["tests/**/*.ts", "tests/**/*.tsx"],
    rules: {
      "max-lines-per-function": "off"
    }
  }
);
