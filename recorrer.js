const fs = require('fs');
const path = require('path');

//De esta manera, la ruta relativa hará que pueda funcionar donde sea
//const docsRoot = path.join(__dirname, '../documentacion-proyecto1/docs'); // raíz principal de docs
const docsRoot = path.join(__dirname, 'docs');

function prettifyName(folderName) {
  return folderName
    .replace(/^\d+-/, '')      // quita prefijos numéricos
    .replace(/-/g, ' ')        // reemplaza guiones por espacios
    .replace(/\b\w/g, c => c.toUpperCase()); // primera letra mayúscula
}

// Crea o actualiza index.md en subcarpetas, no en la raíz de la normativa
function createIndexMd(folderPath, isRoot) {
  if (!fs.existsSync(folderPath)) {
    fs.mkdirSync(folderPath, { recursive: true });
    console.log(`Carpeta creada: ${folderPath}`);
  }

  if (isRoot) return; // ignora la raíz de la normativa

  const indexPath = path.join(folderPath, 'index.md');
  const folderName = path.basename(folderPath);
  const title = prettifyName(folderName);
  const content = `---\ntitle: "${title}"\n---\n\n`;

  fs.writeFileSync(indexPath, content); // sobrescribe aunque exista
  console.log(`Frontmatter generado: ${indexPath}`);
}

// Recorre carpetas recursivamente
function walkDir(dir, isRoot = false) {
  createIndexMd(dir, isRoot);

  const items = fs.readdirSync(dir, { withFileTypes: true });
  for (const item of items) {
    if (item.isDirectory()) {
      // Para las carpetas dentro de la raíz de docs, marcamos isRoot = true (nueva normativa)
      const isSubRoot = isRoot ? true : false;
      walkDir(path.join(dir, item.name), false); // las subcarpetas no son raíz
    }
  }
}

// Detecta todas las carpetas de nivel 1 dentro de docs (las normativas)
const normativas = fs.readdirSync(docsRoot, { withFileTypes: true })
  .filter(item => item.isDirectory())
  .map(item => path.join(docsRoot, item.name));

for (const normativa of normativas) {
  walkDir(normativa, true); // marcamos la raíz de la normativa
}

console.log('¡Frontmatter generado en todos los subdirectorios de todas las normativas!');
