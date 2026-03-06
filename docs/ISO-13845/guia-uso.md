---
id: guia-uso
title: "Guia Uso"
sidebar_label: "Guia Uso"
---

Gestión Documental y Personal PNT-001: Gestión de Documentos
Nueva versión: Al aprobar un documento, regístralo en el Excel: Cuaderno_registro_distribución_retirada_documentos.xlsx Lectura obligatoria: Todo el personal afectado debe confirmar la lectura en este form: https://forms.office.com/e/xmznGaR6hK
Mantenimiento: Si un documento no cambia en 3 años, haz una revisión de oficio y anótalo en: Cuaderno_revision_oficio.xlsx PNT-011: Descripción de Puestos
Nuevo empleado/cambio de puesto: Rellenar y firmar el Anexo 1 (Descripción del puesto). Debe definir funciones y formación mínima.
PNT-003: Formación Registro: Cada vez que alguien haga una formación (interna, externa, lectura de PNTs), debe registrarla aquí: https://forms.office.com/e/BgZadQ9tu0
PNT-017: Firmas Todas las firmas del sistema son digitales (trazabilidad de usuario/fecha). No imprimir para firmar a mano salvo excepción justificada.
PNT-023: Buenas Prácticas Documentales Corrección de errores: Nunca usar Tipp-ex. Tachar con una línea simple, poner el dato correcto al lado, firmar y fechar.
Integridad: Seguir criterios ALCOA (Atribuible, Legible, Contemporáneo, Original, Exacto).
PNT-022: Infraestructura Referencia de las instalaciones (URJC) y arquitectura lógica (GitHub/Firebase). Mantener actualizado si hay mudanza o cambio de servidores.
Gestión de Incidencias y Mejoras PNT-004: No Conformidades (NC)
Detectar: Si se tiene una no conformidad de un cliente o se detecte de forma interna, notificar aquí: https://forms.office.com/e/6bP0pCnTNR Registrar: Anotar en el Excel: Listado_no_conformidades.xlsx
Evaluar: Rellenar el Anexo 3 (Evaluación de impacto).
Acción: Si es necesario, abrir un CAPA (PNT-006).
PNT-006: Acciones Correctivas y Preventivas (CAPA)
Abrir CAPA: Rellenar el Anexo 2 (Informe CAPA).
Seguimiento: Registrar y actualizar estado en: Base_datos_planes_capa.xlsx PNT-007: Reclamaciones de Clientes
Cuando alguien reciba una reclamación por el medio que sea se sigue el siguiente procedimiento:
Rellenar el formulario para tener constancia: https://forms.office.com/e/cTghRSmCR4 Calidad rellena el Anexo 1 del procedimiento, si no es mayor o critica se para, si no se continua con los siguientes pasos
Se rellena el anexo 2, si es procedente se hace un plan Capa Cuando se cierre la reclamación se avisa a la persona que ha puesto la reclamación mediante correo electrónico
PNT-008: Retirada de Producto Acción: Si hay riesgo grave, deshabilitar acceso a la versión en la base de datos (Bloqueo remoto). Generar informe de retirada (punto 5.6).
PNT-025: Sistema de Vigilancia (Incidentes Graves)
Criterios de Notificación: Notificar a la AEMPS si ocurre: 1) Evento, 2) Producto implicado, 3) Muerte o deterioro grave de salud.
Formulario: Usar el MIR Form (Manufacturer Incident Report).
Plazos: 2 días (Amenaza salud pública), 10 días (Muerte/Deterioro grave), 15 días (Otros incidentes graves).
Ciclo de Vida del Software PNT-026 y PNT-027: Diseño y Desarrollo (SDLC)
Herramienta: Todo se gestiona en Jira (Tablero VR-CARDIO).
Flujo: Requisitos Usuario -> Diseño (Input) -> Verificación -> Validación (Output).
Clasificación de Software: Al iniciar una versión, clasificar (A, B, C) con el Anexo 1 del PNT-027.
PNT-015: Identificación y Versionado Regla: vX.Y.Z
X (Major): Cambio grande (arquitectura/funcionalidad clave). Requiere validación completa.
Y (Minor): Nuevas funciones menores.
Z (Patch): Corrección de bugs.
PNT-005: Control de Cambios Proceso: Abrir ticket en Jira. Evaluar impacto en: MDR, Riesgos y UDI.
Tipos: Clasificar el cambio como Major, Minor o Patch.
PNT-002 y ESP-005: Gestión de Riesgos General (PNT-002): Al crear versión, actualizar:
Análisis: AR-002.01_24.docx Matriz: MR-002.01_24.xlsx
Específico Sanitario (ESP-005): Usar metodología ISO 14971.
Cálculo: RPN = Probabilidad x Severidad (No usar detectabilidad para reducir riesgo).
Riesgo Residual: Evaluar si el beneficio supera al riesgo si el RPN es alto.
PNT-018: Validación Documentar: IQ (Instalación), OQ (Operación), PQ (Funcionamiento). Validar no solo el software médico, sino las herramientas de desarrollo y procesos críticos.
PNT-019: Etiquetado Asegurar que la etiqueta (pantalla "Acerca de") contiene el UDI y datos del fabricante.
PNT-016: Liberación de Producto Checklist obligatorio antes de salir al mercado:
Versiones intermedias aprobadas (Anexo 1).
Reproducibilidad verificada (Anexo 2).
Descarga/Instalación verificada (Anexo 3).
Etiquetado correcto (Anexo 4).
Certificado de Liberación firmado por Técnico Responsable (Anexo 5).
PNT-024: Expediente Técnico Crear y mantener el "Technical File" (Anexo 1) para cada familia de productos. Actualizar con datos de Post-Comercialización.
Compras y Proveedores PNT-020: Compras
Solicitud: Abrir ticket en Jira (Tablero Sistema de Tickets).
Seguridad: Verificar requisitos ISO 27001 (Seguridad Información).
PNT-012: Proveedores Solicitar Nuevo: Formulario: https://forms.office.com/e/TSjDqWwHJ9
Evaluación:
Críticos: Exigir ISO 13485/9001 + Acuerdo de Calidad (Anexo 1).
No Evaluables (Google/AWS): Documentar controles compensatorios.
Registro: Aprobar con Anexo 2 y apuntar en Listado_proveedores_aprobados.xlsx Seguimiento, Medición y Mejora
PNT-009: Satisfacción de Cliente Anual: Enviar cuestionario (Anexo 1) a los clientes de mayor facturación.
PNT-014: Seguimiento Post-Comercialización (PMS)
Semestral: Redactar informe de seguimiento (incidentes, tendencias, bibliografía). Si no hay incidentes en 2 periodos consecutivos, pasar a anual.
ESP-006: Medición de Procesos (KPIs)
Definición: Usar criterio SMART (Específicos, Medibles, Alcanzables, Realistas, Temporales).
Acción: Recopilar datos de los indicadores definidos trimestralmente para la revisión por la dirección.
PNT-029: Análisis de Datos Integradora: Analizar conjuntamente: Feedback clientes + Conformidad producto + KPIs procesos + Proveedores + Auditorías. Buscar tendencias negativas.
PNT-030: Seguimiento Regulatorio Frecuencia: Revisar cada 6 meses.
Fuentes: Web AEMPS, DOUE (Diario Oficial UE), Normas ISO.
Acción: Si cambia una ley/norma, evaluar impacto y abrir control de cambios.
PNT-013: Auditorías Internas: Mínimo 1 al año. Planificar + Cualificar auditor (Anexo 2) + Informe. Nota: No auditarse a uno mismo.
Proveedores: Críticos cada 3 años / No críticos cada 5 años. Usar Anexo 1.
PNT-010: Revisión por la Dirección Anual: Reunión CEO + Calidad.
Inputs: KPIs, Auditorías, Reclamaciones, Cambios Normativos.
Output: Informe de Revisión + Objetivos del año siguiente.
6. Gestión Comercial PNT-021: Clientes y Pedidos
Alta Cliente: Rellenar Anexo 1. Verificar que sea un centro sanitario autorizado (Registro REGCESS) antes de vender.