// Node.js 12.18.3
var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

for (let i = 0; i < lines.length; i+= 2) {
  const d = lines[i];
  const s = lines[i+1];

  // avoid runtime error
  if(d === undefined || s === undefined) {
    return;
  }

  if(d.includes(s)) {
    console.log('Resistente');
  } else {
    console.log('Nao resistente');
  }
}
