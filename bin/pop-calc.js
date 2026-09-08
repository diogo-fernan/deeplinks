#!/usr/bin/env node
// Benign test fixture -- pops the platform calculator so an MCP install
// deeplink that fetches and runs this package is directly observable.
// Prints a marker line first so a run that fails to pop calc (headless CI,
// unsupported platform) still leaves evidence in the terminal.
"use strict";

const { spawn } = require("child_process");

const MARKER = "deeplink-test-live-marker";
process.stdout.write(MARKER + "\n");

const plat = process.platform;
if (plat === "darwin") {
  spawn("open", ["-a", "Calculator"], { stdio: "inherit", detached: true }).unref();
} else if (plat === "win32") {
  spawn("cmd.exe", ["/c", "start", "calc.exe"], { stdio: "inherit", detached: true }).unref();
} else {
  process.stdout.write(
    "deeplinks: platform " + plat + " has no default calc; marker printed only\n"
  );
}
