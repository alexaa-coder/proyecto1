// @ts-check
const prismThemes = require('prism-react-renderer').themes;

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'Portal de Cumplimiento Normativo',
  tagline: 'ISO-13485 · ISO-27001 · VRCardio',
  favicon: 'img/favicon.ico',
  url: 'https://your-docusaurus-site.example.com',
  baseUrl: '/',
  organizationName: 'VRCardio',
  projectName: 'documentacion-proyecto1',
  onBrokenLinks: 'warn',
  i18n: {
    defaultLocale: 'es',
    locales: ['es'],
  },
  plugins: [require.resolve('docusaurus-lunr-search')],
  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          showLastUpdateTime: true,
          showLastUpdateAuthor: false,
        },
        blog: false,
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      },
    ],
  ],
  themeConfig: ({
    colorMode: {
      defaultMode: 'light',
      disableSwitch: false,
      respectPrefersColorScheme: true,
    },
    navbar: {
      title: 'VRCardio Compliance',
      hideOnScroll: true,
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'tutorialSidebar',
          position: 'left',
          label: '📋 Normativas',
        },
        {
          href: 'https://github.com/alexaa-coder/proyecto1',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Normativas',
          items: [
            { label: 'ISO 13485 — Calidad', to: '/docs/calidad-iso13485/introduccion' },
            { label: 'ISO 27001 — Seguridad', to: '/docs/seguridad-iso27001/introduccion' },
          ],
        },
        {
          title: 'Proyecto',
          items: [
            { label: 'Repositorio GitHub', href: 'https://github.com/alexaa-coder/proyecto1' },
          ],
        },
      ],
      copyright: `© ${new Date().getFullYear()} VRCardio · Portal de Cumplimiento Normativo`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
  }),
};

module.exports = config;
