let row;
let n= 5;
for(let i=1;i<=n;i++){
    row = ""
    for(let j=1;j<=n-i;j++){
        row += " "
    }
    for(let j=1;j<=2*i-1;j++){
        row += "*"
    }
    console.log(row)
}