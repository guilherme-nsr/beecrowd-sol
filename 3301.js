function getSobrinhoMeio(h, z, l) {
  if ((h > z && h < l) || (h < z && h > l)) {
    return 'huguinho';
  }

  if ((z > h && z < l) || (z < h && z > l)) {
    return 'zezinho';
  }

  return 'luisinho';
}

function main() {
  var input = require('fs').readFileSync('/dev/stdin', 'utf8');
  var lines = input.split('\n');

  const [h, z, l] = lines.shift().split(' ').map(n => Number(n));

  console.log(getSobrinhoMeio(h, z, l));
}

main();