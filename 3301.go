package main

import (
  "fmt"
)

func getSobrinhoMeio(h int, z int, l int) string {
  if (h > z && h < l) || (h < z && h > l) {
    return "huguinho"
  }

  if (z > h && z < l) || (z < h && z > l) {
    return "zezinho"
  }

  return "luisinho"
}

func main() {
  var h, z, l int
  fmt.Scanf("%d %d %d", &h, &z, &l)
  
  fmt.Printf("%s\n", getSobrinhoMeio(h, z, l))
}