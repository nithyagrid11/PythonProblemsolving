let i;
let j;
let row;
let n = 5;
for(i=1;i<=n;i++){
    row = "";
    for(j=1;j<=n;j++)
    {
        if(i==1||i==5||j==1||j==5)
        {
            row = row + "*"
        }
        else{
            row = row + " "
        }
    }
    console.log(row)
}