# Comandos de la Práctica 01
## Jennifer Erzsebet Olvera Martínez

# Parte I.

**Respuesta 1:**

echo $0 

/bin/bash

**Respuesta 2:**

mkdir {data/,filtered/,raw_data/,meta/,scripts/,figures/,archive/}

**Respuesta 3:**

mv filtered data/

mv raw_data data/

**Respuesta 4:**

Cuando creamos un proyecto en bioinformática es muy importante tener en orden los datos que estamos utilizando. Esto se logra a través de la creación 
de un directorio (carpeta) con subdirectorios, que permiten clasificar los datos: 
Data,contiene los datos crudos y los datos modificados que se colocan en los subdirectorios "raw_data" y "filtered".
Meta,contiene metadatos o documentos para procesar datos.
Scripts,contiene los scripts necesarios que permiten correr el análisis de principio a fin. 
Figures,contiene el código que se utilizó para hacer las figuras.
Archive,contiene scripts y resultados que no se necesitarán para el análisis, pero que no es buena idea borrar. Es por esta razón que no se sube al 
repositorio.
   
# Parte II.

**Respuesta 1:**

chmod u+x delay.sh

**Respuesta 2:**

ls - lth 

./delay.sh

**Respuesta 3:**

echo "Después de la parte I. necesito un descanso de exactamente 30 segundos."
sleep 30 && "Ya puedo continuar!"

**Respuesta 4:**

echo "Después de la parte I. necesito un descanso de exactamente 30 segundos."
sleep 300 && "Ya puedo continuar!"

Ctrl C

# Parte III. 

**Respuesta 1:**

nano SarsCov2.txt

mv GenomicaComputacional/jolvera_p01/meta

**Respuesta 2:**

mv sequence.fasta sarscov2_genome.fasta
mv sequence.gff3 sarscov2_genome.gff3

mv sequence.fasta splike_c.faa
mv sequence1.fasta splike_b.faa
mv sequence2.fasta splike_a.faa

nano SarsCov-2_Spike.txt
mv SarsCov-2_Spike.txt meta/

mv sarscov2_genome.fasta sarscov2_genome.gff3 splike_c.faa splike_b.faa splike_a.faa SRR10971381_R1.fastq.gz SRR10971381_R2.fastq.gz 
sarscov2_assembly.fasta.gz GenomicaComputacional/jolvera_p01/data/raw_data

# Parte IV.

**Respuesta 1:**

ln -s ~/raw_data/splike_c01.faa
ln -s ~/raw_data/splike_b.faa
ln -s ~/raw_data/splike_a.faa

**Respuesta 2:**

nano glycoproteins.faa

**Respuesta 3:**

head -1 splike_a.faa
>pdb|6VYB|A Chain A, spike glycoprotein

head -1 splike_b.faa
>pdb|6VYB|B Chain B, spike glycoprotein

head -1 splike_c.faa
>pdb|6VYB|C Chain C, spike glycoprotein

**Respuesta 4:**

less splike_*.faa >> glycoproteins.faa

**Respuesta 5:**

mv data/raw_data/splike_*.faa archive/

No puedo abrir la ligas simbólicas suaves porque los archivos originales se movieron de carpeta (de raw_data a achive). La liga que existía se rompió debido 
a que cambiamos de lugar lso archivos originales. 

**Respuesta 6:**

-Explorar los archivos:

less sarscov2_genome.fasta
zless sarscov2_assembly.fasta.gz

-Imprimir las 3 primeras líneas:

head -3 sarscov2_genome.fasta

>NC_045512.2 Severe acute respiratory syndrome coronavirus 2 isolate Wuhan-Hu-1, complete genome
ATTAAAGGTTTATACCTTCCCAGGTAACAAACCAACCAACTTTCGATCTCTTGTAGATCTGTTCTCTAAA
CGAACTTTAAAATCTGTGTGGCTGTCACTCGGCTGCATGCTTAGTGCACTCACGCAGTATAATTAATAAC

zless sarscov2_assembly.fasta.gz | head -3

>NODE_1_length_264_cov_161.042781
CACAAATCTTAACACTCTTCCCTACACGACGCTCTTCCGATCTACGCCGGGCCATTCGTA
CGAACCGATACCTGTGGTAAAGGGTCCTACTGTATGGTGGTACACGAGTAGTAGCAAATG

La diferencia entre el número de lecturas de los archivos .fasta, se debe a que uno de los archivos se encuentra comprimido (sarscov2_assembly.fasta.gz) por 
lo que tiene una mayor cantidad de infromación en comparación con el archivo sarscov2_genome.fasta. 

**Respuesta 7:**

grep '>' sarscov2_genome.fasta | wc

1 secuencia

zless sarscov2_assembly.fasta.gz | grep '>' | wc

35 secuencias
 
**Respuesta 8:**

zless SRR10971381_R2.fastq.gz | head -12

@SRR10971381.512_2
CGTGGAGTATGGCTACATACTACTTATTTGATGAGTCTGGTGAGTTTAAAGTGGCTTCACATATGTATTGTTCTTTCTACCCTCCAGATGAGGATGAAGAAGAAGGTGATTGTGAAGAAGAAGAGTTTGAGCCATCAACTCAATATGAGT
+
/FFFA/A/FFFF66FFFFFF/FF/FFFFFFFFFFFFF/AFFF6FFFA6FFFFF/FFFFFFFFFFFFFFFFFF/FF/FFFFFA/FFF/FFF/A/AFA/FFFFF/=F/F/F/AFAFF//A/AFF//FFAF/FFF=FFAFFFA/A/6=///==
@SRR10971381.556_2
TTTGTAAAAATAAAATAAAAAAAATAAAAATAATATATTAAAAAAAGATAAATAAAAAAATGAACAATTAATAAAAAAAAAAAAAAAAAAAAATTAAAAAAAAAAAAAAAAAAAATAAAAAAAAAAAAAAATAAAAAAAAAATTATAAAA
+
6AFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF/FFFAFFFFFF/FFA/FF=F//=FF/FFFFFFFFFFFFFA/FFFF/FF/FA//F/FFFFFFA/=FFFFF/FFFF/F=FFFAFF///FFFFA/FF/6//////=/
@SRR10971381.1428_2
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
+
FFFFFFFFFFFFAFFFAFFFFFF6A//F//FFF


zless SRR10971381_R2.fastq.gz | grep '@SRR10971381' | wc

130022 secuencias

**Respuesta 9:**

`.fasta` : Secuencias de nucleótidos. 
`.faa` : Secuencias de aminoácidos.
`.fastqc` : Secuencias de nucléotidos. Después se presentan letras acompañadas de otros símbolos que nos indica la calidad del genoma, es decir, la 
probabildiad de que el nucléotido mostrado en la secuencia sea el correcto. 

**Respuesta 10:**

Al abrir el archivo con `less sarscov2_genomee.gff3`, la información se presenta por líneas. En cambio, `less -S sarscov2_genome.gff3` acomoda la 
información por columnas y filas, permitiendo tener mayor orden y claridad en los datos presentados. 

**Respuesta 11:**

grep 'gene' sarscov2_genome.gff3 | cut -f3 | sort | uniq -c

13 CDS

11 gene

4 stem_loop

El campo tres corresponde a las regiones del gen. `CDS` son regiones del gen que codifican a una proteína, `gene` corresponde a una región que puede 
codificar proteínas ó RNA. 
 

