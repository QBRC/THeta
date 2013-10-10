#Split Interval file into chromosomes.
for i in {1..22};do awk -v i=$i '{if ($2==i) print $0}' input > output

#Apply interval size cutoff.
#Regions with smaller interval size are prone to higher levels of 
variability.
awk '{diff=$4-$3} {if(diff>=3000000) print $0}' input > output

#Apply filter for removing intervals with minimum |upperbound - 
lowerbound| size.
awk 'function abs(x){return ((x<0.0) ? -x : x)} {diff=$6-$5} 
{if(abs(diff) >=0.04) print $0}' input > output

