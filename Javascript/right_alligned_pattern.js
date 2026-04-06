let i;
let j;
let n = 5;
let row;
for(i=1;i<=n;i++){
    row="";
    for(j=1;j<=n-(i-1);j++){
        row = row + "*"
    }
    console.log(row)
}