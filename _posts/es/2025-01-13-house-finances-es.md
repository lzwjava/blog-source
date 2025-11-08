---
audio: false
generated: false
image: false
lang: es
layout: post
title: Seguimiento de las Finanzas de Nuestra Casa
translated: true
type: post
---

Recientemente, creé un documento en markdown para llevar un registro de las transacciones financieras de nuestra casa.

La casa es propiedad de mi esposa y mía. Mis padres nos dieron dinero, y también pedimos prestado dinero a mi hermana y a mi tío materno. Aunque mi tío materno me envió dinero, mi padre luego devolvió esa cantidad.

Pagamos el 50% del precio total de nuestra casa como pago inicial, y pedimos prestada la otra mitad al Agricultural Bank of China. El contrato tiene una duración de 20 años, y la tasa de interés actual es del 3.65%.

Cuando estaba desempleado, mi esposa y mi padre me proporcionaron fondos para cubrir los pagos mensuales de la hipoteca. Como resultado, hay muchas transacciones involucradas.

Uso China Merchants Bank como mi banco principal. China Merchants Bank permite filtrar las transacciones por si son entrantes o salientes, y por un monto mínimo. También admite filtros por palabras clave, lo cual es muy útil.

Otro aspecto útil es la prevalencia de la IA. También puede ayudar con esta tarea. Usando OCR impulsado por IA, específicamente Grok, pude extraer texto de los registros de transacciones con la Guangzhou Electric Power Bureau.

Como la tabla posterior se basa en números anteriores, es mejor verificar los números primero para asegurarse de que todo esté correcto antes de continuar.

El código a continuación ayuda a generar un PDF a partir del markdown. Tiene algunas configuraciones especiales para admitir la representación de caracteres chinos en PDF.

```python
import os
import subprocess

# Configuración
CJK_FONT = "Heiti SC"
GEOMETRY = "margin=1in"
input_markdown_path = "mortgage.md"  # Reemplaza con tu archivo Markdown de entrada
output_pdf_path = "mortgage.pdf"    # Reemplaza con tu archivo PDF de salida deseado

# Verificar si el archivo de entrada existe
if not os.path.exists(input_markdown_path):
    raise Exception(f"El archivo de entrada no existe: {input_markdown_path}")

# Construir el comando de Pandoc
command = [
    'pandoc',
    input_markdown_path,
    '-o', output_pdf_path,
    '-f', 'markdown',
    '--pdf-engine', 'xelatex',
    '-V', f'CJKmainfont={CJK_FONT}',
    '-V', f'CJKsansfont={CJK_FONT}',
    '-V', f'CJKmonofont={CJK_FONT}',
    '-V', f'geometry:{GEOMETRY}',
    '-V', 'classoption=16pt',
    '-V', 'CJKoptions=Scale=1.1',
    '-V', 'linestretch=1.5'
]

# Ejecutar el comando de Pandoc
try:
    subprocess.run(command, check=True)
    print(f"PDF generado exitosamente: {output_pdf_path}")
except subprocess.CalledProcessError as e:
    print(f"Error al generar el PDF: {e}")
```