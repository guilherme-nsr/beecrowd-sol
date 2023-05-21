// Node.js 12.18.3

function getAno(anosTranscorridos, ano) {
  const diferenca = ano - anosTranscorridos;

  if(diferenca === 0) {
    return '1 A.C.';
  }

  if(diferenca > 0) {
    return `${diferenca} D.C.`;
  }

  return `${diferenca*-1 +1} A.C.`;
}

var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

lines.shift();

for (let line of lines) {
  if(!line) { // prevent reading an empty line
    continue;
  }
  const anosTranscorridos = Number(line);
  console.log(getAno(anosTranscorridos, 2015))
}