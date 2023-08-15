#!/Users/vrindavan/.bun/bin/bun

let n_digits = 100
let l = process.argv.length
if (l == 3){
  n_digits = process.argv[2]
}
async function get_digits(n_digits = 10){

  const response = await fetch(`https://api.pi.delivery/v1/pi?start=0&numberOfDigits=${n_digits}`);
  const json = await response.json()
  const content = json.content
  return content
}

let a = await get_digits(n_digits)
console.log(a)
