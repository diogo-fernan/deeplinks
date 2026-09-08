# deeplinks — MCP install deeplink test fixture

**This is a benign test fixture. Do not install unless you are running Proofpoint's deeplink test suite.**

Installing or running this package opens the platform calculator:

- macOS: `open -a Calculator`
- Windows: `cmd.exe /c start calc.exe`
- Other: a marker line is printed to stdout, nothing else.

The package prints `deeplink-test-live-marker` on stdout before spawning calc, so a headless or unsupported platform still leaves observable evidence.

## Why this exists

Proofpoint Threat Research is auditing the MCP install deeplink surface of AI coding clients (Cursor, Goose, LM Studio, VS Code, Warp, Windsurf/Devin). Several of those clients accept deeplinks that resolve to a fetch from an arbitrary source — a git URL, a user/repo shorthand, a remote tarball, an env var pointing at an interpreter option. Verifying whether the fetch-and-run actually reaches code execution on a click, and observing what confirmation dialogs (if any) intervene, requires a live source that can be fetched by ordinary tools (`npx`, `uvx`, ...) without credentials.

This repository is that source. It is deliberately public, unauthenticated, minimal, and benign. The calculator is the tell; nothing else happens.

## Invocation shapes tested

`npx` variants:

```sh
npx diogo-fernan/deeplinks
npx github:diogo-fernan/deeplinks
npx git+https://github.com/diogo-fernan/deeplinks.git
npx https://github.com/diogo-fernan/deeplinks/archive/refs/heads/main.tar.gz
```

`uvx` variants:

```sh
uvx --from git+https://github.com/diogo-fernan/deeplinks.git deeplinks
```

All shapes should print `deeplink-test-live-marker` and open Calculator on macOS / Windows.

## What it is not

- Not a real MCP server. It does not speak the Model Context Protocol; a client that installs this expecting an MCP server will connect, see no methods, and give up. The point is the install-and-launch phase, not the running server.
- Not a package that will ever be published to a public registry. It stays in this git repo. `npx` and `uvx` variants that pull directly from the repo work; `npx deeplinks` (an npm-registry lookup) does not.
- Not signed, not audited, not versioned for stability. Pin to a commit hash if reproducibility matters.

## Auditing

Everything runs from three short files: `bin/pop-calc.js`, `src/deeplinks/__init__.py`, and this README. Anything else appearing in the repo is out of scope for the fixture.

## License

MIT. See `LICENSE`.
