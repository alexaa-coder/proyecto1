// @ts-check
import {themes as prismThemes} from 'prism-react-renderer';

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'Portal de Cumplimiento Normativo',
  tagline: 'ISO-13485 e ISO-27001',
  favicon: 'img/favicon.ico',

  url: 'https://your-docusaurus-site.example.com',
  baseUrl: '/',

  organizationName: 'VRCardio',
  projectName: 'documentacion-proyecto1',

  onBrokenLinks: 'throw',

  i18n: {
    defaultLocale: 'es',
    locales: ['es'],
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
        },
        blog: false,
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      }),
    ],
  ],

  themeConfig: /** @type {import('@docusaurus/preset-classic').ThemeConfig} */ ({
    navbar: {
      title: 'Portal de Cumplimiento Normativo',
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'iso13485',
          position: 'left',
          label: 'ISO 13485 - Calidad',
        },
        {
          type: 'docSidebar',
          sidebarId: 'iso27001',
          position: 'left',
          label: 'ISO 27001 - Seguridad',
        },
        {
          href: 'https://github.com/aleexa-coder/documentacion-proyecto1',
          label: 'Repositorio',
          position: 'right',
        },
      ],
    },
  }),
};

export default config;

