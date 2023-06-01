<?php
  function getSobrinhoMeio($h, $z, $l) {
    if (($h > $z && $h < $l) || ($h < $z && $h > $l)) {
      return "huguinho" . PHP_EOL;
    }

    if (($z > $h && $z < $l) || ($z < $h && $z > $l)) {
      return "zezinho" . PHP_EOL;
    }
    
    return "luisinho" . PHP_EOL;
  }

  function main() {
    $entrada = trim(fgets(STDIN));
    
    list($h, $z, $l) = explode(" ", $entrada);

    echo(getSobrinhoMeio($h, $z, $l));
  }

  main();
?>