with (import <nixpkgs> {});
let
  aoc-2023-packages = python-packages: with python-packages; [
    pytest
    black
  ];
  python-aoc-2023-packages = python3.withPackages aoc-2023-packages;
in
mkShell {
  buildInputs = [
    python-aoc-2023-packages
  ];
}
