function get_pieces(n) {
  if  (n === 0) 
  return 1;
 else;
  return (n * (n + 1) / 2) + 1; // Решение в замкнутой форме 
 }
console.log ("Если n = 0, то Ln = %s",get_pieces(0));
console.log ("Если n = 6, то Ln = %s",get_pieces(6));
console.log ("Если n = 15, то Ln = %s",get_pieces(15));


