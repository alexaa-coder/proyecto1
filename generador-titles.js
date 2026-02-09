const fs = require('fs');
const path = require('path');

const docsPath = path.join(__dirname, 'docs');

function capitalize(str) {
  // Capitaliza cada palabra para el título
  return str
    .split('-')
    .map(word => word.charAt(0).toUpperCase() + word.slice(1))
    .join(' ');
}

function createIndexMd(folderPath) {
  const indexPath = path.join(folderPath, 'index.md');
  if (!fs.existsSync(indexPath)) {
    const folderName = path.basename(folderPath);
    const title = capitalize(folderName);
    const content = `---\ntitle: "${title}"\n---\n`;
    fs.writeFileSync(indexPath, content, 'utf8');
    console.log(`Creado index.md para: ${folderPath}`);
  }
}

function traverseFolders(folder) {
  const entries = fs.readdirSync(folder, { withFileTypes: true });
  let hasMdFiles = false;

  for (const entry of entries) {
    const fullPath = path.join(folder, entry.name);
    if (entry.isDirectory()) {
      traverseFolders(fullPath);
    } else if (entry.isFile() && entry.name.endsWith('.md')) {
      hasMdFiles = true;
    }
  }

  // Si la carpeta tiene subcarpetas o archivos md, asegura que haya un index.md
  if (hasMdFiles || entries.some(e => fs.statSync(path.join(folder, e.name)).isDirectory())) {
    createIndexMd(folder);
  }
}

// Ejecuta sobre la carpeta docs/
traverseFolders(docsPath);

console.log('Proceso completado ✅');
