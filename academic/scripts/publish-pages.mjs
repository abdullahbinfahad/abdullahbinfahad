import { copyFileSync, existsSync, mkdirSync, readdirSync, rmSync } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const projectRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const builtSite = path.join(projectRoot, "dist", "pages");

if (!existsSync(path.join(projectRoot, "client", "index.html"))) {
  throw new Error("Refusing to copy Pages output: client/index.html is missing.");
}
if (!existsSync(builtSite)) {
  throw new Error("Pages build output is missing. Run the Vite build first.");
}

const currentBuildFiles = new Set();

function copyContents(source, destination, relativePath = "") {
  for (const entry of readdirSync(source, { withFileTypes: true })) {
    const childRelative = relativePath ? `${relativePath}/${entry.name}` : entry.name;
    // These are Manus-only development assets, not part of the public study site.
    if (childRelative === "__manus__" || childRelative === "api") continue;
    const from = path.join(source, entry.name);
    const to = path.join(destination, entry.name);
    if (entry.isDirectory()) {
      mkdirSync(to, { recursive: true });
      copyContents(from, to, childRelative);
    } else if (entry.isFile()) {
      copyFileSync(from, to);
      currentBuildFiles.add(childRelative);
    }
  }
}

copyContents(builtSite, projectRoot);

// Remove only obsolete Vite-generated hashed entry bundles; keep any other user asset.
const assetsDir = path.join(projectRoot, "assets");
if (existsSync(assetsDir)) {
  for (const entry of readdirSync(assetsDir, { withFileTypes: true })) {
    const relative = `assets/${entry.name}`;
    if (entry.isFile() && /^index-[A-Za-z0-9_-]+\.(?:js|css)$/.test(entry.name) && !currentBuildFiles.has(relative)) {
      rmSync(path.join(assetsDir, entry.name), { force: true });
    }
  }
}

console.log("GitHub Pages assets copied into the academic/ site root.");
