# Comandos de la prática 02
## Equipo 06
### Integrante 1: Jennifer Erzsebet Olvera Martínez
### Integrante 2: Christian Rodrigo García Gómez
### Integrante 3: Jorge Antonio Ruiz López
### Integrante 4: Azul Itania Rodríguez Ferrer

# Parte I.

**Respuesta 1:**

Plataforma/compañía | Longitud de reads (pb) | # reads x run | Tiempo | Costo x 10^6 bases | Error (%) | Química |
--- | --- | --- | --- | --- | --- | --- |
Primera generación | | | | | | |
Sanger/Life Technologies | 800 | 1 | 2 hrs | 2400 | 0.3 | Dideoxy terminator |
Segunda generación | | | | | | |
Pirosecuenciación (SBS)/454 Life Sciences-Roche | 700 | 1×10^6 | 24-48 hrs | 10 | 1 | Pirosecuenciación |
HiSeq/Illumina | 2x150 | 5x10^9 | 27/240 hrs | 0.1 | 0.8 | Secuenciación por síntesis |
SOLiD/Life Technologies | 50 | 1x10^9 | 14 días | 0.3 | 0.01 | Secuenciación por ligadura de oligonucleótidos |
Ion PGM/Life Technologies | 200 | 5x10^6 | 2-5 hrs | 1 | 1.7 | Secuenciación por la detección de protones liberados por el proceso de polimerización del ADN |
Tercera generación | | | | | | |
Nanoporos (MinION)/Oxford Nanopores Technologies | >5000 | 6x10^4 | 48/72 hrs | <1 | 34 | Secuenciación de moléculas individuales en tiempo real |


Referencias:
[1] Kulski, J. (2016). Next-Generation Sequencing — An Overview of the History, Tools, and “Omic” Applications. Next Generation Sequencing–Advances, Applications and Challenges, 3-60. https://www.intechopen.com/books/next-generation-sequencing-advances-applications-and-challenges/next-generation-sequencing-an-overview-of-the-history-tools-and-omic-applications

# Parte II.

**Respuesta 1:**

Las secuencias están en la sección Associated Data >> Data Availability Statement >>  http://www.ebi.ac.uk/ena/data/view/PRJEB5172

Descomprimir:

unzip ERR486828.fastq.zp

gunzip ERR486828_1.fastq.gz

gunzip ERR486828_2.fastq.gz

Convertir archivo:


**Respuesta 2:**

zcat ERR486828_1.fastq | echo $((`wc -l`/4))

410959

zcat ERR486828_2.fastq | echo $((`wc -l`/4))

410959

**Respuesta 3:**


# Parte III.

**Respuesta 1:**

Descomprimir el archivo:

unzip fastqc_v0.11.9.zip

Moverse a la carpeta creada a partir de descomprimir y cambiar los permisos

cd FastQC

chmod 755 fastqc

Lo volvemos ejecutable desde cualquier lugar de la computadora:

sudo ln -s /home/ruta/archivo/FastQC/fastqc /usr/local/bin/fastqc

**Respuesta 2:**

Creamos el archivo fastqc_run.sh y lo preparamos como se pide:

touch fastqc_run.sh && nano fastqc_run.sh

Ejecutamos el archivo .sh

sh fastqc_run.sh

**Respuesta 3:**

Abrimos los archivos .html de salida.

Describan si las lecturas ¿Son buenas o malas? ¿Por qué?
¿Cómo es el comportamiento de las calidades?

La calidad de ambas lecturas es excelente y se mantienen constantes todo el tiempo,
además ERR486828_1_fastqc tiene un score bastante alto.

**Respuesta 4:**

Calculen y reporten la cobertura del genoma tomando en cuenta que:

covertura = (cantidad de lecturas*longitud de lecturas) / total del tamaño del genoma (bp)

Entonces:



# Parte IV.

**Respuesta 1:**
Se trabajó con Pseudomonas chlororaphis, que es una rizobacteria que se caracteriza por actuar como agente de control biológico contra ciertos patógenos fúngicos de las plantas
 mediante la producción de antibióticos de tipo fenazina

**Respuesta 2:**

Las tecnologías utilizadas en el estudio, en primer lugar se seleccionó el tamaño con BluePippin (10 kb) y se secuenció en la plataforma de secuenciación RSII de Pacific
 Biosciences (PacBio), posteriormente,el ensamblaje de novo del genoma se realizó usando el ensamblador ABruijn. todas las cepas también se secuenciaron con Illumina MiSeq;
 lecturas finales emparejadas de 2 × 300 pb). La información se obtuvo de: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7204214/ 
   
**Respuesta 3:**

covertura = (cantidad de lecturas*longitud de lecturas) / total del tamaño del genoma (bp)
Entonces: 

**Respuesta 4:**


**Respuesta 5:**

**Respuesta 6:**
