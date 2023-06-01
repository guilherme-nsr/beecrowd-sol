def get_sobrinho_meio(h, z, l)
  if (h > z and h < l) or (h < z and h > l)
    return "huguinho"
  end

  if (z > h and z < l) or (z < h and z > l)
    return "zezinho"
  end

  return "luisinho"
end

h, z, l = gets.to_s.split(" ")

puts get_sobrinho_meio(h, z, l)