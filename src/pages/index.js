import React from 'react';
import clsx from 'clsx';
import Layout from '@theme/Layout';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import styles from './index.module.css';

function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();

  return (
    <header className={clsx('hero hero--primary', styles.heroBanner)}>
      <div className="container">
        <h1 className="hero__title">Portal de Cumplimiento Normativo</h1>

        <p className="hero__subtitle">
          Plataforma documental para la gestión de cumplimiento de las normas
          ISO-13485 e ISO-27001 en la empresa VRCardio
        </p>

        <div className={styles.buttons}>
          <Link
            className="button button--secondary button--lg"
            to="/docs/intro">
            Acceder a la documentación
          </Link>
        </div>
      </div>
    </header>
  );
}

function ProjectInfo() {
  return (
    <section className="container margin-top--lg margin-bottom--lg">

      <h2>Sobre el proyecto</h2>

      <p>
        Este portal forma parte del proyecto de implantación de un sistema
        de gestión documental para el cumplimiento de estándares de calidad
        y seguridad de la información en VRCardio.
      </p>

      <p>
        La plataforma permite organizar, consultar y mantener la
        documentación normativa relacionada con:
      </p>

      <ul>
        <li>ISO 13485 – Sistemas de gestión de calidad para dispositivos médicos</li>
        <li>ISO 27001 – Sistemas de gestión de seguridad de la información</li>
        <li>Procesos de auditoría y cumplimiento</li>
        <li>Documentación corporativa y procedimientos internos</li>
      </ul>

      <h2>Características del sistema</h2>

      <ul>
        <li>Infraestructura documental estructurada y navegable</li>
        <li>Conversión automática de documentación a Markdown</li>
        <li>Portal web generado con Docusaurus</li>
        <li>Despliegue mediante Docker</li>
        <li>Arquitectura reproducible y portable</li>
      </ul>

      <div style={{marginTop: "2rem"}}>
        <Link
          className="button button--primary button--lg"
          to="/docs/intro">
          Explorar documentación
        </Link>
      </div>

    </section>
  );
}

export default function Home() {
  const {siteConfig} = useDocusaurusContext();

  return (
    <Layout
      title="Portal de Cumplimiento Normativo"
      description="Infraestructura documental para la gestión de cumplimiento normativo en VRCardio">

      <HomepageHeader />

      <main>
        <ProjectInfo />
      </main>

    </Layout>
  );
}
