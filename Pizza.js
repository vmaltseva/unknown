function get_pieces(n) {
  if  (n === 0) 
  return 1;
 else;
  return (n * (n + 1) / 2) + 1; // ������� � ��������� ����� 
 }
console.log ("���� n = 0, �� Ln = %s",get_pieces(0));
console.log ("���� n = 6, �� Ln = %s",get_pieces(6));
console.log ("���� n = 15, �� Ln = %s",get_pieces(15));