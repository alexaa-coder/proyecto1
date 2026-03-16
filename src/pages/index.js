import React from 'react';
import clsx from 'clsx';
import Layout from '@theme/Layout';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import styles from './index.module.css';

function HomepageHeader() {
  return (
    <header className={clsx('hero hero--primary', styles.heroBanner)}>
      <div className="container">
        <h1 className="hero__title">Portal de Cumplimiento Normativo</h1>
        <p className="hero__subtitle">
          Gestión centralizada de la normativa ISO-13485 e ISO-27001 · VRCardio
        </p>
        <div className={styles.buttons}>
          <Link className="button button--secondary button--lg margin-right--md" to="/docs/calidad-iso13485/introduccion">
            📋 ISO 13485 — Calidad
          </Link>
          <Link className="button button--secondary button--lg" to="/docs/seguridad-iso27001/introduccion">
            🔒 ISO 27001 — Seguridad
          </Link>
        </div>
      </div>
    </header>
  );
}

function NormativaCard({ emoji, title, description, to, color }) {
  return (
    <div className="col col--6 margin-bottom--lg">
      <div className="compliance-card card" style={{ borderLeftColor: color, borderLeftWidth: 4 }}>
        <div className="card__header">
          <h3>{emoji} {title}</h3>
        </div>
        <div className="card__body">
          <p>{description}</p>
        </div>
        <div className="card__footer">
          <Link className="button button--primary button--sm" to={to}>
            Ver documentación →
          </Link>
        </div>
      </div>
    </div>
  );
}

function StatsBar() {
  return (
    <div style={{ background: 'var(--ifm-color-primary)', color: 'white', padding: '1.5rem 0' }}>
      <div className="container">
        <div className="row text--center">
          {[
            { num: '+700', label: 'Documentos indexados' },
            { num: '2', label: 'Normativas ISO' },
            { num: '100%', label: 'Procesamiento local' },
            { num: 'AI-Ready', label: 'Estructura semántica' },
          ].map((s, i) => (
            <div key={i} className="col col--3">
              <div style={{ fontSize: '2rem', fontWeight: 'bold' }}>{s.num}</div>
              <div style={{ fontSize: '0.9rem', opacity: 0.85 }}>{s.label}</div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

export default function Home() {
  return (
    <Layout
      title="Portal de Cumplimiento Normativo"
      description="Gestión documental ISO-13485 e ISO-27001 para VRCardio">
      <HomepageHeader />
      <StatsBar />
      <main className="container margin-top--xl margin-bottom--xl">
        <h2 className="text--center margin-bottom--lg">Normativas disponibles</h2>
        <div className="row">
          <NormativaCard
            emoji="🏥"
            title="ISO 13485 — Calidad"
            description="Sistema de gestión de calidad para productos sanitarios. Procedimientos, registros, auditorías internas y gestión del ciclo de vida del producto."
            to="/docs/calidad-iso13485/introduccion"
            color="#1a6b8a"
          />
          <NormativaCard
            emoji="🔐"
            title="ISO 27001 — Seguridad"
            description="Sistema de gestión de seguridad de la información. Políticas, análisis de riesgos, controles del Anexo A y continuidad de negocio."
            to="/docs/seguridad-iso27001/introduccion"
            color="#0f3460"
          />
        </div>

        <div className="row margin-top--lg">
          <div className="col col--4 margin-bottom--lg">
            <div className="compliance-card card">
              <div className="card__header"><h4>🔍 Búsqueda integrada</h4></div>
              <div className="card__body"><p>Motor de búsqueda local que indexa todo el contenido normativo sin enviar datos a servicios externos.</p></div>
            </div>
          </div>
          <div className="col col--4 margin-bottom--lg">
            <div className="compliance-card card">
              <div className="card__header"><h4>🤖 AI-Ready</h4></div>
              <div className="card__body"><p>Frontmatter estructurado en todos los documentos: responsable, clasificación, tags y fecha de revisión.</p></div>
            </div>
          </div>
          <div className="col col--4 margin-bottom--lg">
            <div className="compliance-card card">
              <div className="card__header"><h4>🐳 Docker</h4></div>
              <div className="card__body"><p>Despliegue reproducible con build multietapa Node.js + Nginx. Un comando para levantar el entorno completo.</p></div>
            </div>
          </div>
        </div>
      </main>
    </Layout>
  );
}
