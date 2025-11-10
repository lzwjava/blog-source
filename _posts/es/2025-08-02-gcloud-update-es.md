---
audio: false
generated: true
image: false
lang: es
layout: post
title: Actualización de la CLI de Google Cloud
translated: true
type: note
---

% gcloud components update
Comenzando la actualización. Este proceso puede tomar varios minutos.


Tu versión actual de Google Cloud CLI es: 507.0.0
Serás actualizado a la versión: 532.0.0

┌─────────────────────────────────────────────────────────────────────────────┐
│                      Estos componentes serán actualizados.                  │
├─────────────────────────────────────────────────────┬────────────┬──────────┤
│                         Nombre                      │  Versión   │  Tamaño  │
├─────────────────────────────────────────────────────┼────────────┼──────────┤
│ BigQuery Command Line Tool                          │     2.1.21 │  1.8 MiB │
│ BigQuery Command Line Tool (Platform Specific)      │     2.1.17 │  < 1 MiB │
│ Cloud Storage Command Line Tool                     │       5.35 │ 12.4 MiB │
│ Cloud Storage Command Line Tool (Platform Specific) │       5.34 │  < 1 MiB │
│ Google Cloud CLI Core Libraries                     │ 2025.07.25 │ 22.1 MiB │
│ Google Cloud CLI Core Libraries (Platform Specific) │ 2025.05.23 │  < 1 MiB │
│ Google Cloud CRC32C Hash Tool (Platform Specific)   │      1.0.0 │  1.4 MiB │
│ gcloud cli dependencies                             │ 2025.04.18 │ 16.1 MiB │
└─────────────────────────────────────────────────────┴────────────┴──────────┘

Mucho ha cambiado desde tu última actualización. Para las últimas notas de la versión completa, visita:
  https://cloud.google.com/sdk/release_notes

Una vez iniciada, cancelar esta operación puede dejar tu instalación del SDK en un estado inconsistente.

¿Quieres continuar (S/n)?  S

Realizando actualización in situ...

╔════════════════════════════════════════════════════════════╗
╠═ Descargando: BigQuery Command Line Tool                  ═╣
╠════════════════════════════════════════════════════════════╣
╠═ Descargando: BigQuery Command Line Tool (Platform Spe... ═╣
╠════════════════════════════════════════════════════════════╣
╠═ Descargando: Cloud Storage Command Line Tool             ═╣
╠════════════════════════════════════════════════════════════╣
╠═ Descargando: Cloud Storage Command Line Tool (Platfor... ═╣
╠════════════════════════════════════════════════════════════╣
╠═ Descargando: Google Cloud CLI Core Libraries             ═╣
╠════════════════════════════════════════════════════════════╣
╠═ Descargando: Google Cloud CLI Core Libraries (Platfor... ═╣
╠════════════════════════════════════════════════════════════╣
╠═ Descargando: Google Cloud CRC32C Hash Tool (Platform ... ═╣
╠════════════════════════════════════════════════════════════╣
╠═ Descargando: gcloud cli dependencies                     ═╣
╠════════════════════════════════════════════════════════════╣
╠═ Desinstalando: BigQuery Command Line Tool                ═╣
╠════════════════════════════════════════════════════════════╣
╠═ Desinstalando: BigQuery Command Line Tool (Platform Sp... ═╣
╠════════════════════════════════════════════════════════════╣
╠═ Desinstalando: Cloud Storage Command Line Tool           ═╣
╠════════════════════════════════════════════════════════════╣
╠═ Desinstalando: Cloud Storage Command Line Tool (Platfo... ═╣
╠════════════════════════════════════════════════════════════╣
╠═ Desinstalando: Google Cloud CLI Core Libraries           ═╣
╠════════════════════════════════════════════════════════════╣
╠═ Desinstalando: Google Cloud CLI Core Libraries (Platfo... ═╣
╠════════════════════════════════════════════════════════════╣
╠═ Desinstalando: Google Cloud CRC32C Hash Tool (Platform... ═╣
╠════════════════════════════════════════════════════════════╣
╠═ Desinstalando: gcloud cli dependencies                   ═╣
╠════════════════════════════════════════════════════════════╣
╠═ Instalando: BigQuery Command Line Tool                   ═╣
╠════════════════════════════════════════════════════════════╣
╠═ Instalando: BigQuery Command Line Tool (Platform Spec... ═╣
╠════════════════════════════════════════════════════════════╣
╠═ Instalando: Cloud Storage Command Line Tool              ═╣
╠════════════════════════════════════════════════════════════╣
╠═ Instalando: Cloud Storage Command Line Tool (Platform... ═╣
╠════════════════════════════════════════════════════════════╣
╠═ Instalando: Google Cloud CLI Core Libraries              ═╣
╠════════════════════════════════════════════════════════════╣
╠═ Instalando: Google Cloud CLI Core Libraries (Platform... ═╣
╠════════════════════════════════════════════════════════════╣
╠═ Instalando: Google Cloud CRC32C Hash Tool (Platform S... ═╣
╠════════════════════════════════════════════════════════════╣
╠═ Instalando: gcloud cli dependencies                      ═╣
╚════════════════════════════════════════════════════════════╝

Realizando pasos de procesamiento posterior...hecho.

¡Actualización completada!

Para revertir tu CLI a la versión previamente instalada, puedes ejecutar:
  $ gcloud components update --version 507.0.0