#This is just a demo, you need to modify codes

#Step 1: use modified samtools to get unique reads of each sample

#1-1: Since all the unique reads files are per chrom, and they need to be put in a folder. Create folders beforehand

mkdir 185LT
mkdir 185N
#1-2: Run modified samtools, change path to absolute path
./samtools view -U Bowtie,/home/bchen4/Projects/colonCancer/uniqReads/185LT/,N,N /nexsan/HOME/TaeHyun/CRC.bam_files/10-185LT_CAGATC_L005.sorted.dedup.realign.sorted.fixed.recal.bam
./samtools view -U Bowtie,/home/bchen4/Projects/colonCancer/uniqReads/185N/,N,N /nexsan/HOME/TaeHyun/CRC.bam_files/10-185N_GCCAAT_L005.sorted.dedup.realign.sorted.fixed.recal.bam

#Step 2: Use the path of unique reads to create configure file for BIC-seq, use in-house script in BC_script folder. Use path(end with "/") as input parameters. The third parameter is output prefix which is a string(not end with "/")
python ../BC_script/makeBICSEQconfigFile.py /home/bchen4/Projects/colonCancer/uniqReads/185LT/ /home/bchen4/Projects/colonCancer/uniqReads/185N/ /home/bchen4/Projects/colonCancer/BIC_config/185LT_N

#2-2: Sometimes is necessary to get rid of random chromsome
grep -v _ 185LT_N.BICconfig > 185_LT_N.BICconfig.clean


#Step 3: run BIC-seq. Need to use BIC-seq absolute path
perl BIC-seq.pl /home/bchen4/Projects/colonCancer/BIC_config/185LT_N.BICconfig.clean /home/bchen4/Projects/colonCancer/BIC_config/185LT_N 185LT_N

#Step 4: use in-house script in BC_script folder to transfer bicseg to THetA input format
python ../BC_script/BIC2THetA.py 185LT_N.BICconfig.clean > 185LT_N.interval
	
#Step 5: normalize the result if necessary
python ../BC_script/intervalNormalization.py 185LT_N.interval > 185LT_N.interval.norm
